#### Consider using the Namelines module instead of this one

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/card-symbols/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/card-symbols/card_fields_dfc
include file: /magic-modules.mse-include/card-symbols/card_fields_tfc

#### Default Field Placement (@375x523, w=1 h=1)
card symbol:
	left:   (8, +18 if used, +28 with transform symbol)w
	top:    21h
	width:  23w
	height: 21h
#### Customization
#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift things by:

#### To shift everything up/down:
card_symbol_offset_top_1 := { 0 }

#### To shift everything left/right:
card_symbol_offset_left_1 := { 0 }

#### To increase/decrease the size:
card_symbol_offset_width_1 := { 0 }
card_symbol_offset_height_1 := { 0 }

#### For the other faces on DFCs use:
card_symbol_offset_top_2 := { 0 }
card_symbol_offset_left_2 := { 0 }
card_symbol_offset_width_2 := { 0 }
card_symbol_offset_height_2 := { 0 }
card_symbol_offset_top_3 := { 0 }
card_symbol_offset_left_3 := { 0 }
card_symbol_offset_width_3 := { 0 }
card_symbol_offset_height_3 := { 0 }

#### You can disable the symbols on some of the faces,
#### by adding the following functions in the init script:
card_symbol_disabled_1 := { true }
card_symbol_disabled_2 := { true }
card_symbol_disabled_3 := { true }
