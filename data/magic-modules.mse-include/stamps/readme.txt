#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/stamps/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/stamps/card_fields_dfc
include file: /magic-modules.mse-include/stamps/card_fields_tfc

#### Customization
#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the stamp by:

#### To shift the stamp up/down:
card_stamp_offset_top := { 0 }

#### To shift the stamp left/right:
card_stamp_offset_left := { 0 }

#### To increase/decrease the size:
card_stamp_offset_width := { 0 }
card_stamp_offset_height := { 0 }

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
card_stamp_disabled := { true }
card_stamp_disabled_2 := { true }
card_stamp_disabled_3 := { true }
