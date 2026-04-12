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
#### The symbol is composed of three parts: the background, the rim and the icon.
#### You can query the values selected by the user with the following functions:

#### Shape of the icon (for example: "lesson", "compass", "front triangle", "back triangle", etc...)
transform_symbol_shape()

#### Render options for the icon ("colored", "black", or "white")
transform_symbol_icon()

#### Render options for the rim ("colored", "black", "white", or "none")
transform_symbol_rim()

#### Render options for the background ("colored", "black", "white", or "none")
transform_symbol_background()

#### Bevel and shadow options for the rim and icon (true or false)
transform_symbol_rim_has_bevel()
transform_symbol_rim_has_shadow()
transform_symbol_icon_has_bevel()
transform_symbol_icon_has_shadow()

#### Is the symbol on the right of the card (true or false)
transform_symbol_is_mirrored()

#### Each part of the symbol has default values.
#### The icon shape defaults to "front triangle" if it's a front face (that is, when it is linked to a back face),
#### "back triangle" if it's a back face, and "none" otherwise. To override this behavior, redefine this function:
transform_symbol_default :=
{
	if		get_back_face(card) != nil	then	"front triangle"
	else if	get_front_face(card) != nil	then	"back triangle"
	else										"none"
}

#### By default, the symbol is on the right when the card is both a back face,
#### and at the same time is not a modal DFC. In all other cases the symbol is on the left.
#### To override this behavior, redefine this function. It must output either "left" or "right".
transform_symbol_default_position :=
{
	if get_front_face(card) != nil
	and not contains(transform_symbol_shape(), match: "modal")
	then "right" else "left"
}

#### By default, the background of the symbol is colored if the card is a modal DFC,
#### and black otherwise. To override this behavior, redefine this function.
#### It must output either "colored", "black", "white" or "none".
transform_symbol_default_background :=
{
	if contains(transform_symbol_shape(), match: "modal")
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
	if transform_symbol_shape() == "modal front"
	then "black" else "white"
}

#### By default, the rim and icon have no bevel effect, and no shadow.
#### To override this behavior, redefine these functions. They must output either true or false.
transform_symbol_default_rim_bevel := { false }
transform_symbol_default_rim_shadow := { false }
transform_symbol_default_icon_bevel := { false }
transform_symbol_default_icon_shadow := { false }
#### To change the shadow color:
transform_symbol_default_rim_shadow_color := { if transform_symbol_background() == "black" or transform_symbol_icon() == "black" then rgb(100,100,100) else rgb(0,0,0) }
transform_symbol_default_icon_shadow_color := { if transform_symbol_background() == "black" or transform_symbol_icon() == "black" then rgb(100,100,100) else rgb(0,0,0) }

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

#### Optionally, you can adjust global alignment of the entire symbol by defining the following functions,
#### which must return an int corresponding to the number of pixels you want to shift things by:
transform_symbol_offset_top_1 := { 0 }
transform_symbol_offset_left_1 := { 0 }
transform_symbol_offset_width_1 := { 0 }
transform_symbol_offset_height_1 := { 0 }

#### When the symbol is on the right of the card, transform_symbol_offset_left_1's effect is flipped
#### (Positive numbers will shift to the left)

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



#### A GIMP script is provided to turn normal symbol images into the kind of images this module uses.

#### To Install this script, open GIMP 3.X or later, go to "Edit" menu > "Preferences", then under "Folders", select "Plug-ins".
#### Select one of the folders in the list, then click on the icon to the right labeled "Show file location in the file manager".
#### It will open the system explorer, navigate inside the folder named "plug-ins", then copy the folder (not the contents)
#### "data/magic-modules.mse-include/symbols/mse-transformation-symbols/" into this "plug-ins" folder. Restart GIMP.

#### To use this script, open the blank symbol image "data/magic-modules.mse-include/symbols/blank.png", and add your symbol in the circle.
#### Your symbol must be white on the image's black background. Save this image in a folder, then go to "Tools" menu > "Transformation Symbols...".
#### Select the folder you saved your image in. (You can save multiple different images if you want.) Click OK. The script will create
#### a sub folder called "shape", where it will store the results. Save these in "data/magic-modules.mse-include/symbols/icon/shape/".
