#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this among the styling field section
#### (styling fields will appear in the order you place them).
#### This will add a boolean to enable custom fonts, and four text
#### options for customizing nameline, typeline, textbox, and pt fonts.
include file: /magic-modules.mse-include/fonts/styling_fields

#### You may also need to redefine the defaults in the style file:
swap_fonts_name_default := [
	name: {"Beleren Bold"},
	size: {16},
	color: {"black"},
	vertical: {0},
	italic: {""}
]
swap_fonts_type_default := [
	name: {"Beleren Bold"},
	size: {13},
	color: {"black"},
	vertical: {0},
	italic: {""}
]
swap_fonts_body_default := [
	name: {"MPlantin"},
	size: {13},
	color: {"black"},
	vertical: {0},
	italic: {"MPlantin-Italic"}
]
swap_fonts_pt_default := [
	name: {"Beleren Bold"},
	size: {16},
	color: {"black"},
	vertical: {0},
	italic: {""}
]

#### For DFC or TFC templates, or just templates with multiple text fields, use:
swap_fonts_name2_default := []
swap_fonts_name3_default := []
swap_fonts_type2_default := []
swap_fonts_type3_default := []
swap_fonts_body2_default := []
swap_fonts_body3_default := []
swap_fonts_pt2_default := []
swap_fonts_pt3_default := []