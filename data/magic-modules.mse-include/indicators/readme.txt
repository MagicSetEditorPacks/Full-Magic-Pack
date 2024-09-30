#### Consider using the Typelines module instead of this one.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/indicators/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/indicators/card_fields_dfc
include file: /magic-modules.mse-include/indicators/card_fields_tfc

#### Default Field Placement (@375x523, w=1 h=1)
indicator:
	left:   31w
	top:    301h
	width:  17w
	height: 17h
#### Customization
#### Optionally, you can define which face of the card the color indicator should snap to,
#### by defining the following function in the init script:
typeline_face_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the color indicator by:

#### To shift the color indicator up/down:
indicator_offset_top_1 := { 0 }

#### To shift the color indicator left/right:
indicator_offset_left_1 := { 0 }

#### To increase/decrease the width and height of the color indicator:
indicator_offset_size_1 := { 0 }

#### For DFC or TFC templates, use:
indicator_offset_top_2 := { 0 }
indicator_offset_left_2 := { 0 }
indicator_offset_size_2 := { 0 }
indicator_offset_top_3 := { 0 }
indicator_offset_left_3 := { 0 }
indicator_offset_size_3 := { 0 }
