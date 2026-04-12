#
# Library that attempts to make it easier/less verbose to define Gimp plugins
# v0.0.00: 2024-11-19:  First published version
# v0.0.01: 2024-11-21:  Make undo and exception handling optional
#                       Return error as Gimp/GLib error
# v0.0.02: 2024-11-28:  Add getArgValue() method and getArgValues() function
# v0.0.03: 2024-11-28:  Fix initialisation of Choice values
# v0.0.04: 2024-11-28:  Use less cutting-edge calls in getIcon()
# v0.0.05: 2024-12-01:  Add context push/pop,
# v0.0.06: 2024-12-01:  Add callProcedure
#                       Change GIMP_HELPERS_DEBUG to GIMPHELPERS_TRACE
# v0.0.07: 2024-12-02:  Add GIMPHELPERS_PROCEDURES to narrow down debugging
#                       (automatic addition to <Image>/Test for the time being)
# v0.0.08: 2024-12-02:  Skip showing dialog when no arguments
#                       Add procedure-level tracing
# v0.0.09: 2025-01-12:  Add Aux/Result argument
#                       callProcedure: return results or throw exception
#                       Add I18N
# v0.0.11: 2025-01-13:  Fix image marked dirty even if nothing happened
# v0.0.12: 2025-03-22:  Fix File option to work with new Gimp File widget

__version__ = (0, 0, 12)  # Make it easier to check with code

#   © Copyright Ofnuts, 2024

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import gi

gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
gi.require_version('Gegl', '0.4')
from gi.repository import Gegl
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gio

import os
import traceback
from dataclasses import dataclass, field
from typing import Callable, Any
from enum import IntEnum

def _(msg: str) -> str: return GLib.dgettext(None, msg)

debug = 'GIMPHELPERS_TRACE' in os.environ

def trace(fmt, *args):
    if debug:
        print(fmt.format(*args) if args else fmt)

def isTraceEnabledFor(name: str):
    if 'GIMPHELPERS_PROCEDURES' in os.environ:
        return name in os.environ['GIMPHELPERS_PROCEDURES'].split(':')
    else:
        return False

def enableTraceFor(name: str):
    global debug
    state=isTraceEnabledFor(name)
    if state is not None: # something set at procedure level
        debug=state
        print(f'Debug for {name}: {debug}')

# Makes it simpler to issue a translatable msg
# (f-strings don't work for this)
def message(fmt, *args):
    Gimp.message(fmt.format(*args) if args else fmt)

#
# Simple-minded GEGL helper for the time being
#
# Sample function to apply a GEGL operation on one drawable
def applyGeglOnBuffers(bufferIn,bufferOut,opName,**kwargs):
    graph=Gegl.Node()
    source=graph.create_child("gegl:buffer-source")
    source.set_property('buffer',bufferIn)
    sink=graph.create_child("gegl:write-buffer")
    sink.set_property('buffer',bufferOut)
    operation=graph.create_child(opName)
    # Iterate named arguments, converting names_with_underscores to names-with-dashes
    for name,value in kwargs.items():
        operation.set_property(name.replace('_','-'),value)
    source.link(operation)
    operation.link(sink)
    sink.process()
    bufferOut.flush()

# Domain is root name of plugin
def getDomain(file):
    return os.path.splitext(os.path.basename(file))[0]

# Icon assumed to be in same directory with same name as plugin .py:
def getIcon(file):
    return Gio.File.new_for_path(os.path.join(os.path.dirname(file), getDomain(file)+'.png'))

#
# Closure to wrap provided function into one that handles dialog, exception, and undo
#

# Short function to determine if it's worth showing the argument dialog
# Experimentally it seems that without arguments there is a single 'procedure'
# argument in the config.
# An alternative implementation would be to count the args and generate
# an alternative wrapper
def hasArgumentsInConfig(config: Gimp.ProcedureConfig) -> bool:
    return len(GObject.list_properties(config)) > 1

def wrap(implementation: Callable, beforeDialog: Callable | None, afterDialog: Callable | None, catchErrors: bool):
    implementationName = str(implementation)
    trace(f'Wrapping {implementationName}')

    def wrapped(procedure: Gimp.ImageProcedure,
                 run_mode: Gimp.RunMode,
                 image: Gimp.Image,
                 drawables: list[Gimp.Drawable],
                 config: Gimp.ProcedureConfig, data: Any):
        enableTraceFor(procedure.get_name())
        trace(f'entering wrapped({procedure=!r}, {run_mode=!r}, {image=!r}, {drawables=!r}, {config=!r}, {data=!r})')
        if beforeDialog:
            beforeDialog(procedure, run_mode, image, drawables, config, data)
        if run_mode == Gimp.RunMode.INTERACTIVE and hasArgumentsInConfig(config):
            GimpUi.init('AutoGeneratedDialog')
            dialog = GimpUi.ProcedureDialog(procedure=procedure, config=config)
            dialog.fill(None)
            if not dialog.run():
                dialog.destroy()
                return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())
            else:
                dialog.destroy()
        if afterDialog:
            afterDialog(procedure, run_mode, image, drawables, config, data)
        trace(f'Returned from dialog in {procedure.get_name()}')
        if catchErrors:
            Gimp.context_push()
            if image:
                # starting a group marks the image dirty, even if nothing else is done
                isCleanOnEntry: bool = not image.is_dirty()
                image.undo_group_start()
                if isCleanOnEntry:
                    image.clean_all() # restore clean state
            try:
                trace(f'executing wrapped({procedure=!r}, {run_mode=!r}, {image=!r}, {drawables=!r}, {config=!r}, {data=!r})')
                result=implementation(procedure, run_mode, image, drawables, config, data)
            except Exception as e:
                traceback.print_exc()
                result=procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, GLib.Error(e.args[0]))
            if image:
                isCleanOnExit: bool = not image.is_dirty()
                image.undo_group_end()
                if isCleanOnExit:
                    image.clean_all() # restore clean state

            Gimp.context_pop()
            return result
        else: # Simplified
            return implementation(procedure, run_mode, image, drawables, config, data)

    return wrapped

#
# Plugin argument description classes
#
# Not implemented so far:
# * All 'aux' arguments
# * All 'return' arguments
# * No support for GUI dialog in current Gimp:
#   * bytes
#   * core_object_array
#   * display
#   * double_array
#   * group_layer
#   * int32_array
#   * item
#   * layer_mask
#   * param
#   * parasite
#   * scaledColorPath
#   * resource
#   * selection
#   * string_array
#   * text_layer
#   * uint
# * color_from_string: what is the point since it shows a palette like plain color?
#   Color can already be initialized with Gegl.Color('red')

# Base class, do not use directly!
@dataclass
class __BaseArg__:
    name: str
    label: str
    blurb: str

    # Extract value directly from config object
    # The benefit is that the implementation code doesn't need
    # to know the name of the variable, and we replace a string
    # (that cannot be checked by the IDE) by a variable name.
    # Subclasses can also do their own thing (see Choice)
    def getArgValue(self,config: Gimp.ProcedureConfig):
        configValue=config.get_property(self.name)
        return configValue

@dataclass
class Boolean(__BaseArg__):
    value: bool
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Brush(__BaseArg__):
    value: str
    noneOK: bool = False
    defaultToContext: bool = False
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Channel(__BaseArg__):
    noneOK: bool = True
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

# Slightly more complicated class to handle Choice because we want to be able
# to store some non-UI data as well
@dataclass
class Option:
    name: str
    label: str
    blurb: str = ''
    value: Any = None
    sensitive: bool = True

class Choice(__BaseArg__):
    def __init__(self, name: str, label: str, blurb: str, value: str,
             options: list[Option],
             flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE):
        self.name=name
        self.label=label
        self.value=value
        self.options=options
        self.blurb=blurb
        self.flags=flags
        self.values=dict()

        # Careful because value can be something "falsy" like "False" or empty string
        # This forbids "None" from being an explicit value, but well???
        for option in self.options:
            if option.value is not None: #
                trace(f'{self.name}: Adding "{option.name}": {option.value}')
                self.values[option.name]=option.value

    def __getitem__(self,name):
        return self.values[name]

    # Get/set value directly from config object
    # The benefit is that the implementation code doesn't
    # need to know the name of the choice variable nor the names of the choices
    def getArgValue(self,config: Gimp.ProcedureConfig):
        option,=config.get_properties(self.name)
        trace(f'Value for choice {self.name}: {option=}, {self.values=}')
        return self.values[option] if option in self.values else option

@dataclass
class Color(__BaseArg__):
    value: Gegl.Color
    hasAlpha: bool = False
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Double(__BaseArg__):
    valueMin: float
    valueMax: float
    valueDefault: float
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Drawable(__BaseArg__):
    noneOK: bool = True
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class File(__BaseArg__):
    action: Gimp.FileChooserAction = Gimp.FileChooserAction.ANY
    noneOK: bool = False
    default: str | list[str] | Gio.File | None = None
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Font(__BaseArg__):
    value: Gimp.Font
    noneOK: bool = False
    defaultToContext: bool = False
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Gradient(__BaseArg__):
    value: Gimp.Gradient
    noneOK: bool = False
    defaultToContext: bool = False
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class GroupLayer(__BaseArg__):
    noneOK: bool = True
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Image(__BaseArg__):
    noneOK: bool = True
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Int(__BaseArg__):
    valueMin: int
    valueMax: int
    valueDefault: int
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Layer(__BaseArg__):
    noneOK: bool = True
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class LayerMask(__BaseArg__):
    noneOK: bool = True
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Palette(__BaseArg__):
    value: Gimp.Palette
    noneOK: bool = False
    defaultToContext: bool = False
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class Pattern(__BaseArg__):
    value: Gimp.Pattern
    noneOK: bool = False
    defaultToContext: bool = False
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

@dataclass
class String(__BaseArg__):
    value: str = ''
    flags: GObject.ParamFlags = GObject.ParamFlags.READWRITE

#
# Mapping of argument declaration type to add_{}_argument calls
# Could possibly just use add_{}_argument(dataclasses.astuple(argDesc))
def traceResourceArg(name: str, value: Gimp.Resource):
    if value:
        trace(f'++++ Adding {type(value)}: {value.get_name()}')
    else:
        trace(f'+*** {name} not defined!!!!!!!!!!')

class ArgType(IntEnum):
    ARG=0
    AUX=1
    RES=2

def notImplemented(procedure: Gimp.Procedure, argType: ArgType, argDesc: __BaseArg__):
    raise Exception(f'Adding {argDesc.name}: {type(argDesc)} argument not implemented')

def addBooleanArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Boolean):
    addMethods: list[Callable] = [procedure.add_boolean_argument,
                                  procedure.add_boolean_aux_argument,
                                  procedure.add_boolean_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        argDesc.value,
                        argDesc.flags)

def addBrushArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Brush):
    addMethods: list[Callable] = [procedure.add_brush_argument,
                                  procedure.add_brush_aux_argument,
                                  procedure.add_brush_return_value]
    brush = Gimp.Brush.get_by_name(_(argDesc.value)) if argDesc.value else None
    traceResourceArg(argDesc.label, brush)
    trace(f'Flags: {argDesc.noneOK=}, {argDesc.defaultToContext=}')
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        argDesc.noneOK,
                        brush,
                        argDesc.defaultToContext,
                        argDesc.flags)

def addChannelArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Channel):
    addMethods: list[Callable] = [procedure.add_channel_argument,
                                  procedure.add_channel_aux_argument,
                                  procedure.add_channel_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        argDesc.noneOK,
                        argDesc.flags)

def addChoiceArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Choice):
    addMethods: list[Callable] = [procedure.add_choice_argument,
                                  procedure.add_choice_aux_argument,
                                  procedure.add_choice_return_value]
    choice = Gimp.Choice.new()
    for index, option in enumerate(argDesc.options):
        choice.add(option.name, index, _(option.label), _(option.blurb))
        choice.set_sensitive(option.name, option.sensitive)
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        choice,
                        argDesc.value,
                        argDesc.flags)

def addColorArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Color):
    addMethods: list[Callable] = [procedure.add_color_argument,
                                  procedure.add_color_aux_argument,
                                  procedure.add_color_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        argDesc.hasAlpha, argDesc.value,
                        argDesc.flags)

def addDoubleArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Double):
    addMethods: list[Callable] = [procedure.add_double_argument,
                                  procedure.add_double_aux_argument,
                                  procedure.add_double_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        argDesc.valueMin, argDesc.valueMax, argDesc.valueDefault,
                        argDesc.flags)

def addDrawableArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Drawable):
    addMethods: list[Callable] = [procedure.add_drawable_argument,
                                  procedure.add_drawable_aux_argument,
                                  procedure.add_drawable_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label), _(argDesc.blurb),
                        argDesc.noneOK,
                        argDesc.flags)

def addFileArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: File):
    addMethods: list[Callable] = [procedure.add_file_argument,
                                  procedure.add_file_aux_argument,
                                  procedure.add_file_return_value]
    default: Gio.File | None = None
    match argDesc.default:
        case Gio.File() | None:
            default=argDesc.default
        case str():
            default=Gio.File.new_for_path(_(argDesc.default))
        case [*pathList] if all(isinstance(pathItem,str) for pathItem in pathList):
            default=Gio.File.new_build_filenamev(*[_(p) for p in pathList])
        case _:
            raise Exception(f"Unrecognized file description type {type(argDesc.default)} in File argument descriptor")
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.action,
                        argDesc.noneOK,
                        default,
                        argDesc.flags)

def addFontArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Font):
    addMethods: list[Callable] = [procedure.add_font_argument,
                                  procedure.add_font_aux_argument,
                                  procedure.add_font_return_value]
    font = Gimp.Font.get_by_name(_(argDesc.value)) if argDesc.value else None
    traceResourceArg('Font', font)
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.noneOK,
                        font,
                        argDesc.defaultToContext,
                        argDesc.flags)

def addGradientArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Gradient):
    addMethods: list[Callable] = [procedure.add_gradient_argument,
                                  procedure.add_gradient_aux_argument,
                                  procedure.add_gradient_return_value]
    gradient = Gimp.Gradient.get_by_name(_(argDesc.value)) if argDesc.value else None
    traceResourceArg('Gradient', gradient)
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.noneOK,
                        gradient,
                        argDesc.defaultToContext,
                        argDesc.flags)

# def addGroupLayerArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: GroupLayer):
#     addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
#                                     argDesc.noneOK,
#                                     argDesc.flags)

def addImageArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Image):
    addMethods: list[Callable] = [procedure.add_image_argument,
                                  procedure.add_image_aux_argument,
                                  procedure.add_image_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.noneOK,
                        argDesc.flags)

def addIntArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Int):
    addMethods: list[Callable] = [procedure.add_int_argument,
                                  procedure.add_int_aux_argument,
                                  procedure.add_int_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.valueMin, argDesc.valueMax, argDesc.valueDefault,
                        argDesc.flags)

def addLayerArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Layer):
    addMethods: list[Callable] = [procedure.add_layer_argument,
                                  procedure.add_layer_aux_argument,
                                  procedure.add_layer_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.noneOK,
                        argDesc.flags)

# def addLayerMaskArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: LayerMask):
#     addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
#                                     argDesc.noneOK,
#                                     argDesc.flags)

def addPaletteArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Palette):
    addMethods: list[Callable] = [procedure.add_palette_argument,
                                  procedure.add_palette_aux_argument,
                                  procedure.add_palette_return_value]
    palette = Gimp.Palette.get_by_name(_(argDesc.value)) if argDesc.value else None
    traceResourceArg('Palette', palette)
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.noneOK,
                        palette,
                        argDesc.defaultToContext,
                        argDesc.flags)

def addPatternArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: Pattern):
    addMethods: list[Callable] = [procedure.add_pattern_argument,
                                  procedure.add_pattern_aux_argument,
                                  procedure.add_pattern_return_value]
    pattern = Gimp.Pattern.get_by_name(_(argDesc.value)) if argDesc.value else None
    traceResourceArg('Pattern', pattern)
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.noneOK,
                        pattern,
                        argDesc.defaultToContext,
                        argDesc.flags)

def addStringArg(procedure: Gimp.Procedure, argType: ArgType, argDesc: String):
    addMethods: list[Callable] = [procedure.add_string_argument,
                                  procedure.add_string_aux_argument,
                                  procedure.add_string_return_value]
    addMethods[argType](argDesc.name, _(argDesc.label),_(argDesc.blurb),
                        argDesc.value,
                        argDesc.flags)

# Dictionary of type -> function because this author hates long
# if/elif (or even "match" in Gimp3)
typeToArgProcs: dict[type, Callable]={
                Boolean: addBooleanArg,
                Brush: addBrushArg,
                Channel: addChannelArg,
                Choice: addChoiceArg,
                Color: addColorArg,
                Double: addDoubleArg,
                Drawable: addDrawableArg,
                File: addFileArg,
                Font: addFontArg,
                Gradient: addGradientArg,
                GroupLayer: notImplemented,
                Image: addImageArg,
                Int: addIntArg,
                Layer: addLayerArg,
                LayerMask: notImplemented,
                Palette: addPaletteArg,
                Pattern: addPatternArg,
                String: addStringArg,
             }

#
# Plugin procedure description
#
@dataclass
class ProcedureDescription:
    id: str
    imageTypes: str
    sensitivity: Gimp.ProcedureSensitivityMask
    implementation: Callable[[Gimp.ImageProcedure,Gimp.RunMode,Gimp.Image,
                              list[Gimp.Drawable],Gimp.ProcedureConfig,Any],Gimp.ValueArray]
    menuLabel: str | None = None
    menuPath: str | list [str]  | None  = None
    descShort: str | None  = None
    descLong: str | None  = None
    args: list[__BaseArg__] = field(default_factory=lambda: [])
    auxArgs: list[__BaseArg__] = field(default_factory=lambda: [])
    resArgs: list[__BaseArg__] = field(default_factory=lambda: [])
    run_data: Any = None
    beforeDialog: Callable[[Gimp.ImageProcedure,Gimp.RunMode,Gimp.Image,list[Gimp.Drawable],Gimp.ProcedureConfig,Any],None] | None  = None
    afterDialog: Callable[[Gimp.ImageProcedure,Gimp.RunMode,Gimp.Image,list[Gimp.Drawable],Gimp.ProcedureConfig,Any],None] | None  = None
    catchErrors: bool=True

class HelpedPlugin(Gimp.PlugIn):

    # These class data are replaced by the data set in the derived plugin
    procedures : list[ProcedureDescription]=[]
    icon: Gio.File = None
    author: str = ''
    copyright: str = ''
    year: str = ''
    domain: str | None = None

# Methods defined by the Gimp interface
    def do_set_i18n(self, procname):
        print(f'** do_set_i18n({procname=!r}): {self.domain} **')
        if self.domain:
            trace(f'{procname}: setting I18N domain to "{self.domain}"')
            return True, self.domain, 'locale'
        else:
            return False,None,None

    def do_query_procedures(self):
        trace(f'** do_query_procedures() **')
        return [procDesc.id for procDesc in self.procedures]  # convert to list

    def do_create_procedure(self, procName):
        trace(f'Creating procedure {procName}')
        matches = [procDesc for procDesc in self.procedures if procDesc.id==procName]
        if not matches or len(matches) > 1:
            return None
        procDesc: ProcedureDescription = matches[0]
        procedure: Gimp.Procedure = Gimp.ImageProcedure.new(self, procName,
                                                            Gimp.PDBProcType.PLUGIN,
                                                            wrap(procDesc.implementation,
                                                                 procDesc.beforeDialog,
                                                                 procDesc.afterDialog,
                                                                 procDesc.catchErrors),
                                                            procDesc.run_data)
        procedure.set_image_types(procDesc.imageTypes)
        procedure.set_sensitivity_mask(procDesc.sensitivity)
        if procDesc.menuLabel:
            procedure.set_menu_label(_(procDesc.menuLabel))
            if procDesc.menuPath is None:
                trace(f'No menu path defined for {procDesc.id}, skipped')
            elif isinstance(procDesc.menuPath,list):
                for p in procDesc.menuPath:
                    procedure.add_menu_path(_(p))
            else:
                procedure.add_menu_path(_(procDesc.menuPath))
            # To <Image>/Test for quick access when debugging
            if isTraceEnabledFor(procName):
                trace(f'{procDesc.id} added to menu <Image>/Test)')
                procedure.add_menu_path('<Image>/Test')
        else:
            trace(f'No menu label defined for {procDesc.id}, skipped')
        if procDesc.descShort:
            procedure.set_documentation(_(procDesc.descShort), _(procDesc.descLong),procName)
        if self.icon:
            procedure.set_icon_file(self.icon)
        if self.author:
            procedure.set_attribution(self.author,self.copyright,self.year)

        for arg in procDesc.args:
            typeToArgProcs[type(arg)](procedure, ArgType.ARG, arg)
        for aux in procDesc.auxArgs:
            typeToArgProcs[type(aux)](procedure, ArgType.AUX, aux)
        for res in procDesc.resArgs:
            typeToArgProcs[type(res)](procedure, ArgType.RES, res)

        trace(f'End of creation for procedure {procName}')
        return procedure

# Get arguments from config object
def getConfigArgs(config: Gimp.ProcedureConfig, *argNames: str):
    return [config.get_properties(arg)[0] for arg in argNames ]

# Get arguments from config object
def getArgsValues(config: Gimp.ProcedureConfig, *args: __BaseArg__):
    return [arg.getArgValue(config) for arg in args ]

def callProcedure(procId: str, run_mode=Gimp.RunMode.NONINTERACTIVE, **kwargs):
    procedure=Gimp.get_pdb().lookup_procedure(procId)
    if procedure is None:
        raise Exception(f'Procedure "{procId}" no found')
    config: Gimp.ProcedureConfig = procedure.create_config()
    #config.set_property('run-mode',run_mode)
    for name,value in kwargs.items():
        if isinstance(value,list):
            config.set_core_object_array(name.replace('_','-'),value)
        else:
            config.set_property(name.replace('_','-'),value)
    result=procedure.run(config)
    results = [result.index(i) for i in range(result.length())]
    if results[0] is not Gimp.PDBStatusType.SUCCESS:
        raise Exception(f'Error returned from procedure "{procId}": {results[0].value_name}')
    return results[1:]

def successReturn(procedure: Gimp.Procedure, *args) -> Gimp.ValueArray:
    values: Gimp.ValueArray = procedure.new_return_values(Gimp.PDBStatusType.SUCCESS,GLib.Error())
    values.truncate(1)
    for v in args:
        values.append(v)
    return values

def errorReturn(procedure: Gimp.Procedure) -> Gimp.ValueArray:
    values: Gimp.ValueArray = procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR,GLib.Error())
    return values





