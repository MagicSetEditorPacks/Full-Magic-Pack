#### Consider using the Namelines module instead of this one

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/symbols/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/symbols/card_fields_dfc
include file: /magic-modules.mse-include/symbols/card_fields_tfc

#### Default Field Placement (@375x523, w=1 h=1)
transformation:
	left:   13w, 319 mirrored
	top:    19h
	width:  43w
	height: 43h
#### Customization
#### The symbols default to "none", defaults can be changed with
transform_symbol_default :=
{
	stylesheet ## reload script when template changes
	if		margin_code == "transform1" then	"front triangle"
	else if	margin_code == "transform2" then	"back triangle"
	else										"eldrazi"
}
#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift things by:

#### To shift everything up/down:
transform_symbol_offset_top_1 := { 0 }

#### To shift everything left/right:
transform_symbol_offset_left_1 := { 0 }

#### To increase/decrease the size:
transform_symbol_offset_width_1 := { 0 }
transform_symbol_offset_height_1 := { 0 }

#### To move the symbol to the right of the card:
transform_symbol_mirrored_1 := { true }

#### When the symbol is on the right of the card, transform_symbol_offset_left_1's effect if flipped
#### (Positive numbers will shift to the left)

#### For the other faces on DFCs use:
transform_symbol_offset_top_2 := { 0 }
transform_symbol_offset_left_2 := { 0 }
transform_symbol_offset_width_2 := { 0 }
transform_symbol_offset_height_2 := { 0 }
transform_symbol_offset_mirrored_2 := { 0 }
transform_symbol_offset_top_3 := { 0 }
transform_symbol_offset_left_3 := { 0 }
transform_symbol_offset_width_3 := { 0 }
transform_symbol_offset_height_3 := { 0 }
transform_symbol_offset_mirrored_3 := { 0 }

#### You can disable the symbols on some of the faces,
#### by adding the following functions in the init script:
transform_symbol_disabled_1 := { true }
transform_symbol_disabled_2 := { true }
transform_symbol_disabled_3 := { true }
