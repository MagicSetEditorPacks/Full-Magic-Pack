#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/stamps/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/stamps/card_fields_dfc
include file: /magic-modules.mse-include/stamps/card_fields_tfc

#### Default Field Placement (@375x523, w=1 h=1)
card stamp:
	left:   166w
	top:    473h
	width:  43w
	height: 43h
#### Customization
#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the stamp by:

#### To shift the stamp up/down:
card_stamp_offset_top_1 := { 0 }

#### To shift the stamp left/right:
card_stamp_offset_left_1 := { 0 }

#### To increase/decrease the size:
card_stamp_offset_width_1 := { 0 }
card_stamp_offset_height_1 := { 0 }

#### For the other faces on DFCs use:
card_stamp_offset_top_2 := { 0 }
card_stamp_offset_left_2 := { 0 }
card_stamp_offset_width_2 := { 0 }
card_stamp_offset_height_2 := { 0 }
card_stamp_offset_top_3 := { 0 }
card_stamp_offset_left_3 := { 0 }
card_stamp_offset_width_3 := { 0 }
card_stamp_offset_height_3 := { 0 }

#### You can disable the stamp on some of the faces,
#### by adding the following functions in the init script:
card_stamp_disabled_1 := { true }
card_stamp_disabled_2 := { true }
card_stamp_disabled_3 := { true }
