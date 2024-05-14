#### To use this include in a template, add the following line, not indented, in the card style section:
include file: /magic-typelines.mse-include/complete_typelines

#### Also add the following in the template headers:
depends on:
	package:			magic-typelines.mse-include
	version:			2024-01-29

#### Optionally, you can define which face of the card the typeline should snap to,
#### by defining the following function in the init script:
typeline_face := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the typeline by:

#### To shift the entire typeline up/down (type + rarity + color indicator dot):
typeline_offset_top := { 0 }

#### To shift the entire typeline left/right:
typeline_offset_left := { 0 }

#### To increase/decrease the width of the entire typeline (this WILL NOT change the size of the rarity and color indicator):
typeline_offset_width := { 0 }

#### To increase/decrease the height of the entire typeline (this WILL change the size of the rarity and color indicator):
typeline_offset_height := { 0 }

#### You can also adjust each of the components individually:
indicator_offset_top := { 0 }
indicator_offset_left := { 0 }
indicator_offset_size := { 0 }

rarity_offset_top := { 0 }
rarity_offset_left := { 0 }
rarity_offset_size := { 0 }

type_offset_top := { 0 }
type_offset_left := { 0 }
type_offset_right := { 0 }
type_offset_height := { 0 }

#### For the other faces on DFCs or TFCs use:
typeline_offset_top_2 := { 0 }
typeline_offset_left_2 := { 0 }
typeline_offset_width_2 := { 0 }
typeline_offset_height_2 := { 0 }
typeline_offset_top_3 := { 0 }
typeline_offset_left_3 := { 0 }
typeline_offset_width_3 := { 0 }
typeline_offset_height_3 := { 0 }
etc...

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### You can disable the typelines on some of the faces,
#### by adding the following functions:
typeline_disabled := { true }
typeline_disabled_2 := { true }
typeline_disabled_3 := { true }
