#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2026-10-01

#### Add the following line, indented by one tab, in the init script section:
	include file: /magic-modules.mse-include/levels/init_script

#### Add the following line,unindented, in the styling field section:
include file: /magic-modules.mse-include/levels/styling_fields

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/levels/card_fields

#### Implementation
## Determines if the Leveler fields will be used
leveler_enabled := { true }

## Applies the leveler color stripes to the card image
## integrated with DFC module is_notched and is_back_face scripts
leveler_multiply(input:color_field, image:card_image)

## The level striping area is defined by this image, where black is where stripes can go
leveler_stripes_mask := {
	"/magic-modules.mse-include/levels/multiply_mask_levels"
	+ (if is_notched() then "_notched" else "")
	+ ".png"
}
## Optional nine-sliced masked to apply to the multiplied area. Parameter "level" is provided.
## image: image_to_nine_slice, should be the width of the card, return "" for normal striping
## top_margin and bottom_margin are the nine_slice margins
## top_offset/bottom_offset increase the multiply bounds to allow interleaving layers
leveler_stripe_effect_mask := {
	[
		image: if styling.jagged_stripe then "/magic-modules.mse-include/levels/multiply_mask_jagged.png" else "",
		top_margin: 5,
		bottom_margin: 5
		top_offset: 5,
		bottom_offset: 0,
	]
}

## If this string contains Spacecraft or Planet, Station levelers will be used regardless of styling.level_containers
## set it to "" when you want to disable auto-spacecraft checking
check_auto_spacecraft := { card.sub_type }

## This module updates swap_fonts_pt_default for white text on station, vehicle, and back face pts
## If you change swap_fonts_pt_default, make sure to define it after this script include
## And add the station handling into the size and color definitions
size: {if leveler_station_pt() then 13 else 15},
color: {if leveler_vehicle_containers() or leveler_station_pt() or is_back_face() then "white" else "black"},

## The module defaults to handling small PT boxes, but has compatibility with full-canvas pt boxes some showcases use
leveler_canvas_ptboxes := {
	[
		"pt": [				## box type, generally just pt unless you did station_pt too
			offset_top:	-N	## offset from midline of PT Box from midline of image
			pt_left:	N	## the pt field left coordinate
			pt_top:		N	## the pt field top coordinate
			pt_width:	N	## the pt field width
			pt_height:	N	## the pt field height
		]
	]
}
## use the regular PT box instead of ones for each level. nonlevelers don't worry about this function.
leveler_regular_pt := { false }
## use no PT boxes, perhaps so a template-defined starting loyalty or defense can be used instead
leveler_no_pt := { false }
## left/top when using regular pt. Default height is 38 * leveler_coord_factor()
leveler_pt_normal_left		## default 293w, 0w for canvas_ptbox
leveler_pt_normal_top 		## default 467h, 0h for canvas_ptbox

#### Customization
## default level container label
leveler_label_default_string := { "level" }

## allow containers and pt boxes to use a vehicle variant when this returns true
leveler_vehicle_containers := { match_vehicle(card.sub_type) }

## Offsets
leveler_container_offset_left := { 0 }
leveler_container_offset_top := { 0 }
leveler_ptbox_offset_left := { 0 }
leveler_ptbox_offset_top := { 0 }
leveler_margin_offset_left := { 0 }
leveler_margin_offset_right := { 0 }

## Coordinates
## These maps are referenced for several coordinate operations, and will be scaled by leveler_coord_factor()
## Missing entries use the "fallback" value instead.
## Custom shapes may be added by concatting these arrays instead of redefining half the module

## margins for level_N_text around the level container and ptbox
leveler_margins_left
leveler_margins_right

## coords of level containers
leveler_container_left_coord
leveler_container_width_coord
leveler_container_height_coord
leveler_container_top_correction  ## only use if centered placement if off

## internal offsets for level container textboxes, positive moves towards the center
leveler_container_text_inset_top
leveler_container_text_inset_bottom
leveler_container_text_inset_left
leveler_container_text_inset_width

## coords of pt boxes
leveler_ptbox_left_coord
leveler_ptbox_width_coord
leveler_ptbox_height_coord

## internal offsets for level container textboxes, positive moves towards the center
leveler_ptbox_text_inset_top
leveler_ptbox_text_inset_left
leveler_ptbox_text_inset_width

## parameters for color_multiply
leveler_multiply_dimensions := [
	"arrow": 		[height:90, width:112,	mask:""],
	"box": 			[height:76, width:135,	mask:"/magic-modules.mse-include/pts/375 m15/multiply_mask.png"],
	"pt": 			[height:76, width:135,	mask:"/magic-modules.mse-include/pts/375 m15/multiply_mask.png"],
	"station_pt": 	[height:0, 	width:0, 	mask:""]
]

## LEVEL label height, when used
leveler_label_height := { 10 * leveler_coord_factor() }

## images used for containers and ptboxes
## redefine here to change folders, switch in clear icons, etc
leveler_arrow_template := {
	if leveler_vehicle_containers() then input := "v"
	"/magic-modules.mse-include/levels/arrows/" + input + ".png"
}
leveler_circle_template := {
	"/magic-modules.mse-include/levels/circles/station/" + input + "circle.png"
}
leveler_box_template := {
	if leveler_vehicle_containers() then input := "v"
	"/magic-modules.mse-include/pts/375 m15/" + input + "pt.png"
}
leveler_ptbox_template := leveler_box_template
leveler_station_pt_template := {
	"/magic-modules.mse-include/pts/375 m15/station/" + input + "pt.png"
}
## for complicated blends, these functions may be redefined instead
arrow_container
circle_container
box_container
leveler_ptbox_image
station_ptbox_image

## The gradient used for leveler multiplication
multi_scale := [0, 0.35, 0.55, 0.75, 0.85, 1.0, 1.1]

## Coordinates are written for 375x523 frames, this factor scales them to HD frames
## Set it to 1 instead if you redefine the coordinates to match your canvas size
leveler_coord_factor := { face_factor(1) }

## color_field(input:0_indexed_level)
## determines the color each level uses
color_field := { card.card_color }

## the maximum level supported by the module, for for-loops
max_supported_levels := 6

## the maximum non-empty level
last_active_level()

#### Adding new shapes
## add the shape option to styling.level_containers choice list
## whatever you put here will be your shape name in other scripts

## have this function return the blended (but not multiplied) container images
leveler_custom_container(input:color_field, shape:styling.level_containers)

## concat your shapes details to each coordinate array
leveler_margins_left := leveler_margins_left + ["shape":20]

## if the shape doesn't use labels, such as Station, concat to this array
leveler_unlabeled_shape_array := leveler_unlabeled_shape_array + ["shape"]

## if the shape needs a different font size, concat to this array
leveler_container_font_sizes := leveler_container_font_sizes + ["shape":20]

## Arrow and Box containers will fit their Level field to the whole container when the label is " "
## You can add that effect to your shape by redefining this function
## parameter mana is true when invoked from the symbol font
leveler_blanked_label_font_offset := {
	if (shape == "arrow" and not mana) 	then 2
	else if shape == "box"				then 2
	else									 0
}