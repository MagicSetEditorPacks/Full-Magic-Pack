#### Consider using the Namelines module instead of this one.
#### It encompasses transformation symbols, card symbols, names and casting costs, all at once.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/symbols/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/symbols/card_fields_dfc
include file: /magic-modules.mse-include/symbols/card_fields_tfc

#### Default Field Placement
#### For 375x523 templates, w = h = 1
#### For 750x1046 templates, w = h = 2
#### etc...
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

#### By default, the symbol moves to the right when the card is a back face
#### (that is, when it is linked to a front face). To override this behavior:
transform_symbol_mirrored_1 := { get_front_face(card) != nil }

#### When the symbol is on the right of the card, transform_symbol_offset_left_1's effect is flipped
#### (Positive numbers will shift to the left)

#### When a symbol is present on the card, the name or casting cost need to move.
#### You can increase/decrease the amount by which they do:
name_transform_symbol_offset_left_1 := { 0 }
casting_cost_transform_symbol_offset_left_1 := { 0 }

#### To change the folder from which the symbol images are taken:
#### You must write the path of the folder starting from the data folder
#### The image files must have the same names as the ones in the default folder (/magic-modules.mse-include/symbols/)
#### You can omit some images and it will use the default ones instead
transform_symbol_image_folder := { "/magic-modules.mse-include/symbols/" }

#### For the other faces on DFCs use:
transform_symbol_offset_top_2 := { 0 }
transform_symbol_offset_left_2 := { 0 }
transform_symbol_offset_width_2 := { 0 }
transform_symbol_offset_height_2 := { 0 }
transform_symbol_mirrored_2 := { true }
transform_symbol_offset_top_3 := { 0 }
transform_symbol_offset_left_3 := { 0 }
transform_symbol_offset_width_3 := { 0 }
transform_symbol_offset_height_3 := { 0 }
transform_symbol_mirrored_3 := { true }
etc...

#### You can disable the symbols on some of the faces,
#### by adding the following functions in the init script:
transform_symbol_disabled_1 := { true }
transform_symbol_disabled_2 := { true }
transform_symbol_disabled_3 := { true }
