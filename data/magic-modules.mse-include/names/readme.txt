#### Consider using the Namelines module instead of this one

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/names/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/names/card_fields_dfc
include file: /magic-modules.mse-include/names/card_fields_tfc

#### Default Field Placement (@375x523, w=1 h=1)
name:
	left:   32w + symbols_width
	top:    27h
	right:  341w - casting_cost
	height: 26h
#### Customization
#### Optionally, you can define which face of the card the name should snap to,
#### by defining the following function in the init script:
nameline_face_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the name by:

#### To shift the name up/down:
name_offset_top_1 := { 0 }

#### To shift the name left/right:
name_offset_left_1 := { 0 }

#### To shift where the name ends:
name_offset_right_1 := { 0 }

#### To increase/decrease the height of the name:
name_offset_height_1 := { 0 }

#### For DFC or TFC templates, use:
name_offset_top_2 := { 0 }
name_offset_left_2 := { 0 }
name_offset_size_2 := { 0 }
name_offset_top_3 := { 0 }
name_offset_left_3 := { 0 }
name_offset_size_3 := { 0 }