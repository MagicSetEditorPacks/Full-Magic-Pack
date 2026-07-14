#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/namelines/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/namelines/card_fields_dfc
include file: /magic-modules.mse-include/namelines/card_fields_tfc

#### Customization
#### The transform symbols default to "none", defaults can be changed with
transform_symbol_default :=
{
	stylesheet ## reload script when template changes
	if		margin_code == "transform1" then	"front triangle"
	else if	margin_code == "transform2" then	"back triangle"
	else										"eldrazi"
}

#### Optionally, you can define which face of the card the nameline should snap to,
#### by defining the following function in the init script:
nameline_face_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the nameline by:

#### To shift the entire nameline up/down (name + casting cost + transformation symbol):
nameline_offset_top_1 := { 0 }

#### To shift the entire nameline left/right:
nameline_offset_left_1 := { 0 }

#### To increase/decrease the width of the entire nameline (this WILL NOT change the size of the transformation symbol):
nameline_offset_width_1 := { 0 }

#### To increase/decrease the height of the entire nameline (this WILL change the size of the transformation symbol):
nameline_offset_height_1 := { 0 }

#### You can also adjust each of the components individually:
name_offset_top_1 := { 0 }
name_offset_left_1 := { 0 }
name_offset_right_1 := { 0 }
name_offset_height_1 := { 0 }

casting_cost_offset_top_1 := { 0 }
casting_cost_offset_left_1 := { 0 }
casting_cost_offset_width_1 := { 0 }
casting_cost_offset_height_1 := { 0 }

transform_symbol_disabled_1 := { true }
transform_symbol_mirrored_1 := { true }
transform_symbol_offset_top_1 := { 0 }
transform_symbol_offset_left_1 := { 0 }
transform_symbol_offset_width_1 := { 0 }
transform_symbol_offset_height_1 := { 0 }

#### You can increase/decrease the amount by which the name shifts left
#### when a card symbol or a transformation symbol is present on the card:
name_card_symbol_offset_left_1 := { 0 }
name_transform_symbol_offset_left_1 := { 0 }

#### For DFC or TFC templates, use:
nameline_offset_top_2 := { 0 }
nameline_offset_left_2 := { 0 }
nameline_offset_width_2 := { 0 }
nameline_offset_height_2 := { 0 }
nameline_offset_top_3 := { 0 }
nameline_offset_left_3 := { 0 }
nameline_offset_width_3 := { 0 }
nameline_offset_height_3 := { 0 }
etc...

