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
#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift things by:

#### To shift everything up/down:
transform_symbol_offset_top_1 := { 0 }

#### To shift everything left/right:
transform_symbol_offset_left_1 := { 0 }

#### To increase/decrease the size:
transform_symbol_offset_width_1 := { 0 }
transform_symbol_offset_height_1 := { 0 }

#### The symbol is composed of three parts: the background, the rim and the icon.

#### The symbol icon defaults to "none".
#### To override this behavior, redefine this function, for example like so:
transform_symbol_default :=
{
	if		margin_code == "transform1" then	"front triangle"
	else if	margin_code == "transform2" then	"back triangle"
	else										"eldrazi"
}

#### There are also a number of rendering options.
#### By default, the symbol is on the right when the card is both a back face (that is, when it is linked to a front face),
#### and at the same time is not a modal DFC. In all other cases the symbol is on the left.
#### To override this behavior, redefine this function. It must output either "left" or "right".
transform_symbol_default_position :=
{
	if get_front_face(card) != nil
	and not contains(transform_symbol_field(face), match: "modal")
	then "right" else "left"
}

#### When the symbol is on the right of the card, transform_symbol_offset_left_1's effect is flipped
#### (Positive numbers will shift to the left)

#### By default, the background of the symbol is colored if the card is a modal DFC,
#### and black otherwise. To override this behavior, redefine this function.
#### It must output either "colored", "black", "white" or "none".
transform_symbol_default_background :=
{
	if contains(transform_symbol_field(face), match: "modal")
	then "colored" else "black"
}

#### By default, the symbol has a white rim around it. To override this behavior, redefine this function.
#### It must output either "colored", "black", "white" or "none".
transform_symbol_default_rim :=
{
	"white"
}

#### By default, the symbol has a black icon if the card is the front of a modal DFC,
#### and a white one otherwise. To override this behavior, redefine this function.
#### It must output either "colored", "black" or "white".
transform_symbol_default_icon :=
{
	if contains(transform_symbol_field(face), match: "modal front")
	then "black" else "white"
}

#### By default, the symbol rim and icon have no bevel effect, and no shadow.
#### To override this behavior, redefine these functions. they must output either true or false.
transform_symbol_default_rim_bevel := { false }
transform_symbol_default_rim_shadow := { false }
transform_symbol_default_icon_bevel := { false }
transform_symbol_default_icon_shadow := { false }
#### To change the shadow color:
transform_symbol_default_rim_shadow_color := { if transform_symbol_background() == "black" then rgb(128,128,128) else rgb(0,0,0) }
transform_symbol_default_icon_shadow_color := { if transform_symbol_background() == "black" then rgb(128,128,128) else rgb(0,0,0) }

#### To change the folder from which the symbol images are taken:
#### You must write the path of the folder starting from the data folder.
#### The image files must have the same names, and be placed in the same subfolders as the
#### ones in the default folder (/magic-modules.mse-include/symbols/), and must all be PNGs.
#### You can omit some images and it will use the default ones instead.
transform_symbol_image_folder := { "/magic-modules.mse-include/symbols/" }

#### If there is only one color for all the frames, then instead of
#### making a folder containing the 8 variants (w u b r g m c a),
#### make a single PNG image file with the same name as that folder.

#### If the modal symbols need to use the same background as the normal ones:
transform_symbol_modal_uses_normal_background := { true }

#### If you need to move the icon placement within the symbol image:
transform_symbol_icon_offset_top := { 0 }
transform_symbol_icon_offset_left := { 0 }
transform_symbol_icon_offset_width := { 0 }
transform_symbol_icon_offset_height := { 0 }

#### When a symbol is present on the card, the name or casting cost need to move.
#### You can increase/decrease the amount by which they do:
name_transform_symbol_offset_left_1 := { 0 }
casting_cost_transform_symbol_offset_left_1 := { 0 }

#### For the other faces on DFCs use:
transform_symbol_offset_top_2 := { 0 }
transform_symbol_offset_left_2 := { 0 }
transform_symbol_offset_width_2 := { 0 }
transform_symbol_offset_height_2 := { 0 }
transform_symbol_offset_top_3 := { 0 }
transform_symbol_offset_left_3 := { 0 }
transform_symbol_offset_width_3 := { 0 }
transform_symbol_offset_height_3 := { 0 }
etc...

#### You can disable the symbols on some of the faces,
#### by adding the following functions in the init script:
transform_symbol_disabled_1 := { true }
transform_symbol_disabled_2 := { true }
transform_symbol_disabled_3 := { true }
