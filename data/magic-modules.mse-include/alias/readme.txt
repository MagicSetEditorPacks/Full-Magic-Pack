#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/alias/card_fields
#### For DFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/alias/card_fields_dfc
#### If you need the alias to layer under the card frame, use
include file: /magic-modues.mse-include/alias/card_fields_under
include file: /magic-modues.mse-include/alias/card_fields_under_dfc

#### Default Field Placement (@375x523, w=1 h=1)
alias bar:
	left:   38.5w	# Auto-centers
	top:    57w		# 55w for the text box
	width:  298w
	height: 20h
	z index: 880	# 180 for _under

#### Customization
#### The alias bar is recolored a solid color, using this function in template()
#### This can return a single rgb for mono-color, and is passed a boolean land for the land template
alias_colors := {
	[
		w: rgb(255, 255, 255),
		u: rgb(6, 115, 184),
		b: rgb(39, 38, 36),
		r: rgb(168, 88, 81),
		g: rgb(6, 120, 69),
		a: rgb(239, 238, 236),
		m: rgb(243, 210, 105),
		c: rgb(173, 151, 137)
	][input]
}
#### Pull files from an alternate file. Needs three files that are each the same size:
#### base.png, which will have the solid color printed on top of it
#### mask.png, where Black pixels are recolored and White take from base.png
#### color.png, the red color used for recolor_image(). If you're not doing anything fancy, just make it a #ff0000 rectangle
alias_src := "/magic-modules.mse-include/alias/"

#### Alias expects to blend on pinlines. If you need to change that, redefine module_alias
#### Changing "white" to "black" to blend as artifact, land, or gold
#### If you change card_hybrid to use an image, make a copy and redefine this using the copy
module_alias := {
	template := alias_custom_template
	land_template := alias_custom_land_template
	color_background(
		type: "alias",
		base_hybrid: card_hybrid,
		artifact_blend: "white",
		hybrid_blend: "white",
		multicolor_blend: "white"
	)
}


#### Field Offsets
alias_offset_text(face:1)
#### Change the font size
alias_font_size(face:1)

#### Show the Alias Bar
alias_enabled := 			{ card.alias != "" }
alias_enabled_2 := 			{ card.alias != "" }
#### Move the bar and alias left
alias_offset_top_1 := 		{ 0 }
alias_offset_left_1 := 		{ 0 }
alias_offset_height_1 := 	{ 0 }
alias_offset_width_1 := 	{ 0 }
alias_angle_1 :=			{ 0 }
#### Move the text vertically. Positive moves down
alias_offset_text_top_1 :=	{ 0 }

#### Apply a mask to the Alias Bar. Some are provided in the module:
#### masks/remove_color.png		-> masks to just the gray text area
#### masks/remove_outline.png	-> removes the black outline on the bottom
#### masks/
alias_mask :=				{ "" }
alias_mask_2 :=				{ "" }
