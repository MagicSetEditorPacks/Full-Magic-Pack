#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/typelines/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/typelines/card_fields_dfc
include file: /magic-modules.mse-include/typelines/card_fields_tfc

#### Customization
#### Optionally, you can define which face of the card the typeline should snap to,
#### by defining the following function in the init script:
typeline_face_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the typeline by:

#### To shift the entire typeline up/down (type + rarity + color indicator dot):
typeline_offset_top_1 := { 0 }

#### To shift the entire typeline left/right:
typeline_offset_left_1 := { 0 }

#### To increase/decrease the width of the entire typeline (this WILL NOT change the size of the rarity and color indicator):
typeline_offset_width_1 := { 0 }

#### To increase/decrease the height of the entire typeline (this WILL change the size of the rarity and color indicator):
typeline_offset_height_1 := { 0 }

#### You can also adjust each of the components individually:
indicator_offset_top_1 := { 0 }
indicator_offset_left_1 := { 0 }
indicator_offset_size_1 := { 0 }

rarity_offset_top_1 := { 0 }
rarity_offset_left_1 := { 0 }
rarity_offset_size_1 := { 0 }

type_offset_top_1 := { 0 }
type_offset_left_1 := { 0 }
type_offset_right_1 := { 0 }
type_offset_height_1 := { 0 }

#### For DFC or TFC templates, use:
typeline_offset_top_2 := { 0 }
typeline_offset_left_2 := { 0 }
typeline_offset_width_2 := { 0 }
typeline_offset_height_2 := { 0 }
typeline_offset_top_3 := { 0 }
typeline_offset_left_3 := { 0 }
typeline_offset_width_3 := { 0 }
typeline_offset_height_3 := { 0 }
etc...

