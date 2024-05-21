#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20
#### Use the highest date version needed among modules

#### For each styling option you want to use, put its include file line in the styling fields section unindented
#### It will appear in the order you place it with the others

#### alt-rarity
#### Adds a text option for customizing the colors used by the rarity symbol
include file: /magic-modules.mse-include/styling-options/alt-rarity

#### casting-cost-mana-symbols
#### Adds an package option to select an alternate mana font for the casting cost and similar fields
include file: /magic-modules.mse-include/styling-options/casting-cost-mana-symbols

#### custom-fonts
#### Adds a boolean to enable custom fonts
#### Adds four text options for customizing nameline, typeline, textbox, and pt fonts
include file: /magic-modules.mse-include/styling-options/custom-fonts
#### You may also need to redefine the defaults in the style file:
swap_fonts_name_default := [
	name: {"Beleren Bold"},
	size: {16},
	color: {"black"},
	vertical: {0},
	italic: {""}
]
swap_fonts_name2_default := [
	name: {"Beleren Bold"},
	size: {16},
	color: {"black"},
	vertical: {0},
	italic: {""}
]
swap_fonts_name3_default := [
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
swap_fonts_type2_default := [
	name: {"Beleren Bold"},
	size: {13},
	color: {"white"},
	vertical: {0},
	italic: {""}
]
swap_fonts_type3_default := [
	name: {"Beleren Bold"},
	size: {13},
	color: {"white"},
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

