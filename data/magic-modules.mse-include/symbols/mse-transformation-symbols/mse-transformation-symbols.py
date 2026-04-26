#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script takes normal symbol images and outputs images that can be used by MSE's transformation symbol module.
#
# To Install this script, open GIMP 3.X or later, go to "Edit" menu > "Preferences", then under "Folders", select "Plug-ins".
# Select one of the folders in the list, then click on the icon to the right labeled "Show file location in the file manager".
# It will open the system explorer, navigate inside the folder named "plug-ins", then copy the folder (not the contents)
# named "mse-transformation-symbols" found in "data/magic-modules.mse-include/symbols/" inside this "plug-ins" folder. Restart GIMP.
#
# To use this script, open the blank symbol image "data/magic-modules.mse-include/symbols/blank.png", and add your symbol in the circle.
# Your symbol must be white on the image's black background. Save this image in a folder, then go to "Tools" menu > "Transformation Symbols...".
# Select the folder you saved your image in. (You can save multiple different images if you want.) Click OK. The script will create
# a sub folder called "shape", where it will store the results. Save these in "data/magic-modules.mse-include/symbols/icon/shape/".
#
# Thanks to Ofnuts for the helper scripts.

import gi
gi.require_version('Gimp', '3.0')
gi.require_version('Gegl', '0.4')
from gi.repository import Gimp, Gegl, GLib, Gio
import sys, os, time, re, math
from gimphelpers import *

def _(text): return GLib.dgettext(None, text)

directoryArg = File('directory',
					_('Directory'),
					_('Directory where files are loaded'),
					action = Gimp.FileChooserAction.CREATE_FOLDER,
					noneOK = False)

runMode = Gimp.RunMode.INTERACTIVE

def cleanName(name):
	name = name.strip()
	name = re.sub(r'( copy| \#[0-9]+)+$', '', name)
	name = re.sub(r'.jpeg|.jpg|.png|.webp$', '', name)
	return name

def fileFromPathComponents(path:list[str]) -> Gio.File:
	return Gio.file_new_for_path(GLib.build_filenamev(path))

def run(procedure: Gimp.ImageProcedure,
		run_mode: Gimp.RunMode,
		image: Gimp.Image,
		drawables: list[Gimp.Drawable],
		config: Gimp.ProcedureConfig,
		data: Any) -> Gimp.ValueArray:

	#### Read user input
	directory = directoryArg.getArgValue(config)
	directory_path = directory.get_path()
	directory_name = os.path.basename(directory_path)

	#### Create save directory
	save_directory: Gio.File = fileFromPathComponents([directory_path]+['shape'])
	save_directory_path = save_directory.get_path()
	save_directory_type = save_directory.query_file_type(Gio.FileQueryInfoFlags.NONE)
	match save_directory_type:
		case Gio.FileType.DIRECTORY: #### Already there
			pass;
		case Gio.FileType.UNKNOWN: #### Not already there
			save_directory.make_directory_with_parents(None)
		case _:
			raise Exception(f'{save_directory_path} is not a directory')

	#### Set up context
	pdb = Gimp.get_pdb()

	image = Gimp.Image.new(706, 706, Gimp.ImageType.RGB_IMAGE)
	display = Gimp.Display.new(image)

	curve_points = [0.0, 0.0, 0.478, 0.227, 0.517, 0.662, 1.0, 1.0]
	black = Gegl.Color.new("black")
	grey = Gegl.Color.new("#808080")
	
	load_layer_group = Gimp.GroupLayer.new(image)
	load_layer_group.set_name(directory_name)
	image.insert_layer(load_layer_group, None, 0)

	#### Load image files
	file_names = os.listdir(directory_path)
	for file_name in file_names:
		file_path = os.path.join(directory_path, file_name)
		file_path_lower = file_path.lower()
		if (not os.path.isdir(file_path)) and (file_path_lower.endswith('.png') or file_path_lower.endswith('.webp') or file_path_lower.endswith('.jpg') or file_path_lower.endswith('.jpeg')):
			file = Gio.File.new_for_path(file_path)
			layer = Gimp.file_load_layer(Gimp.RunMode.NONINTERACTIVE, image, file)
			layer.set_name(file_name)
			image.insert_layer(layer, load_layer_group, 0)
			width = layer.get_width()
			height = layer.get_height()
			if width != 706 or height != 706:
				Gimp.message(f'ERROR: Image {file_name} is not 706x706 pixels!')
				return
			Gimp.displays_flush()
			layer.set_visible(False)
	layers = load_layer_group.get_children()

	#### Erase the rim
	image.select_ellipse(Gimp.ChannelOps.REPLACE, 137, 137, 432, 432)
	Gimp.Selection.invert(image)
	Gimp.context_set_foreground(black)
	for layer in layers:
		layer.set_visible(True)
		Gimp.displays_flush()
		layer.edit_fill(Gimp.FillType.FOREGROUND)
		Gimp.displays_flush()
		layer.set_visible(False)

	Gimp.context_set_foreground(grey)
	for layer in layers:
		layer.set_visible(True)
		image.set_selected_layers([layer])
		Gimp.displays_flush()

		#### Turn black/white mask into grey/transparent
		mask = layer.create_mask(Gimp.AddMaskType.COPY)
		layer.add_mask(mask)
		image.select_item(Gimp.ChannelOps.REPLACE, layer)
		Gimp.Selection.all(image)
		layer.edit_fill(Gimp.FillType.FOREGROUND)
		layer.remove_mask(Gimp.MaskApplyMode.APPLY)
		Gimp.Selection.none(image)
		Gimp.displays_flush()

		#### Rotate -90°
		rotate_270_procedure = pdb.lookup_procedure('gimp-item-transform-rotate-simple')
		rotate_270_config = rotate_270_procedure.create_config()
		rotate_270_config.set_property('item', layer)
		rotate_270_config.set_property('rotate-type', Gimp.RotationType.DEGREES270)
		rotate_270_config.set_property('auto-center', True)
		rotate_270_result = rotate_270_procedure.run(rotate_270_config)
		layer = rotate_270_result.index(1)
		Gimp.displays_flush()

		#### Add bevel
		bevel_procedure = pdb.lookup_procedure('script-fu-add-bevel')
		bevel_config = bevel_procedure.create_config()
		bevel_config.set_property('run-mode', Gimp.RunMode.NONINTERACTIVE)
		bevel_config.set_property('image', image)
		bevel_config.set_core_object_array('drawables', [layer])
		bevel_config.set_property('adjustment', 24)
		bevel_config.set_property('toggle', False)
		bevel_config.set_property('toggle-2', False)
		bevel_procedure.run(bevel_config)
		Gimp.Selection.none(image)
		Gimp.displays_flush()

		#### Rotate 90°
		rotate_90_procedure = pdb.lookup_procedure('gimp-item-transform-rotate-simple')
		rotate_90_config = rotate_90_procedure.create_config()
		rotate_90_config.set_property('item', layer)
		rotate_90_config.set_property('rotate-type', Gimp.RotationType.DEGREES90)
		rotate_90_config.set_property('auto-center', True)
		rotate_90_result = rotate_90_procedure.run(rotate_90_config)
		layer = rotate_90_result.index(1)
		Gimp.displays_flush()

		#### Increase contrast
		layer.curves_spline(Gimp.HistogramChannel.VALUE, curve_points)
		Gimp.displays_flush()

		#### Save
		save_file: Gio.File = fileFromPathComponents([save_directory_path]+[cleanName(layer.get_name()) + '.png'])
		export_image = Gimp.Image.new(layer.get_width(), layer.get_height(), image.get_base_type())
		export_layer = Gimp.Layer.new_from_drawable(layer, export_image)
		export_layer.set_offsets(0, 0)
		export_image.insert_layer(export_layer, None, 0)
		global runMode
		ok = Gimp.file_save(runMode, export_image, save_file, None)
		runMode = Gimp.RunMode.WITH_LAST_VALS
		export_image.delete()
		if not ok:
			Exception('Failed to save')
		Gimp.displays_flush()
		layer.set_visible(False)

	time.sleep(0.5)
	display.delete()
	Gimp.displays_flush()
	return successReturn(procedure)

class DescriptionClass(HelpedPlugin):
	procedures = [
		ProcedureDescription(
			'mse-transformation-symbols',
			'*',
			Gimp.ProcedureSensitivityMask.ALWAYS,
			run,
			args = [
				directoryArg,
			],
			menuLabel = _('Transformation Symbols...'),
			menuPath = ['<Image>/Tools/[MSE]'],
			descShort = _('Create beveled versions of transformation symbols'),
			descLong = _('Load all the image files in directoryArg. Create beveled versions for use in the MSE transformation symbol module.'),
		)
	]
	domain = getDomain(__file__)
	icon = getIcon(__file__)
	author = 'GenevensiS'
	year = '2026'

Gimp.main(DescriptionClass.__gtype__, sys.argv)
