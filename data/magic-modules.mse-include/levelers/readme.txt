#### This include covers the leveler textboxes, including the separators between textboxes,
#### levels, level labels, and pts.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Add the following line,unindented, in the styling field section:
include file: /magic-modules.mse-include/levelers/styling_fields

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/levelers/card_fields

#### Customization
#### Optionally, you can adjust appearance by defining the following functions in the init script:

#### To change which face of the card the boxes go on:
leveler_face_1 :=									{ 1 }

#### To change which text field the boxes go on:
leveler_text_field_1 :=								{ 1 }
leveler_stamp_field_1 :=							{ 1 }

#### To change the position of all the textboxes, labels and separators:
#### In these functions you have access to the input variable which will
#### hold the number of the ability making the call. To know the shape of
#### the corresponding box, use "leveler_level_box_field(input)" or
#### "leveler_pt_box_field(input)".
leveler_level_offset_top_1 :=						{ 0 }
leveler_level_offset_left_1 :=						{ 0 }
leveler_level_offset_width_1 :=						{ 0 }
leveler_level_offset_height_1 :=					{ 0 }

leveler_level_box_offset_top_1 :=					{ 0 }
leveler_level_box_offset_left_1 :=					{ 0 }
leveler_level_box_offset_width_1 :=					{ 0 }
leveler_level_box_offset_height_1 :=				{ 0 }

leveler_level_label_offset_top_1 :=					{ 0 }
leveler_level_label_offset_left_1 :=				{ 0 }
leveler_level_label_offset_width_1 :=				{ 0 }
leveler_level_label_offset_height_1 :=				{ 0 }

leveler_pt_offset_top_1 :=							{ 0 }
leveler_pt_offset_left_1 :=							{ 0 }
leveler_pt_offset_width_1 :=						{ 0 }
leveler_pt_offset_height_1 :=						{ 0 }

leveler_pt_box_offset_top_1 :=						{ 0 }
leveler_pt_box_offset_left_1 :=						{ 0 }
leveler_pt_box_offset_width_1 :=					{ 0 }
leveler_pt_box_offset_height_1 :=					{ 0 }

leveler_separator_offset_top_1 :=					{ 0 }
leveler_separator_offset_left_1 :=					{ 0 }
leveler_separator_offset_width_1 :=					{ 0 }
leveler_separator_offset_height_1 :=				{ 0 }

#### If you want to remove the separators between textboxes:
leveler_separator_disabled_1 :=						{ false }

#### To change how much space there is between the text and boxes:
leveler_level_offset_text_margin_1 :=				{ 0 }
leveler_pt_offset_text_margin_1 :=					{ 0 }
#### (You can for example make this dependent on the box being station:)
leveler_pt_offset_text_margin_1 :=					{ if leveler_pt_box_field(input) == "station" then -10 else 0 }

#### If you want to use a custom image for the pt box or level box, supply it's path:
leveler_level_box_image_1 :=						{ "" }
leveler_level_box_land_image_1 :=					{ "" }
leveler_pt_box_image_1 :=							{ "" }
leveler_pt_box_land_image_1 :=						{ "" }

#### If you want to use custom images but you have variants for each color, instead put these variants in a folder.
#### You must have 8 of them, for artifact, black, colorless, green, multicolor, red, blue and white.
#### The image file names must start with the first letter of the color, followed by "levelbox" or "ptbox",
#### and end with ".png". Point to the folder with these functions:
leveler_level_box_image_folder_1 :=					{ "/magic-modules.mse-include/levelboxes/744x1039/m15/" + leveler_pt_box_field(input) + "/base/" }
leveler_level_box_land_image_folder_1 :=			{ "/magic-modules.mse-include/levelboxes/744x1039/m15/" + leveler_pt_box_field(input) + "/base/" }

leveler_pt_box_image_folder_1 :=					{ "/magic-modules.mse-include/ptboxes/744x1039/m15/" + leveler_pt_box_field(input) + "/base/" }
leveler_pt_box_land_image_folder_1 :=				{ "/magic-modules.mse-include/ptboxes/744x1039/m15/" + leveler_pt_box_field(input) + "/base/" }

#### If you have further variants for each level, put them in subfolders named 1 to up to 6.

#### You can also add to these folders a mask named "hybrid_blend_mask.png".
#### It will be used to blend on two colors cards if the hybrid scheme is selected from the style tab.

#### If you want the level label to be on the side instead of the top, or outright disabled:
leveler_level_label_on_side_1 :=					{ false }
leveler_level_label_disabled_1 :=					{ false }
