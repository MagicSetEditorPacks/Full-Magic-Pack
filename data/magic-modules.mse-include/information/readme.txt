#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/information/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/information/card_fields_dfc
include file: /magic-modules.mse-include/information/card_fields_tfc

#### Customization
#### Optionally, you can adjust global alignment by redefining the following functions after the scripts include statement
#### which must return an int corresponding to the number of pixels you want to shift things by
#### positive numbers move right and down, negative move left and up

#### To shift everything up/down:
information_offset_top := { 0 }

#### To shift the card number, set code and artist credit left/right:
information_codes_offset_left := { 0 }

#### To shift the actual copyright lines left/right:
information_copyright_offset_right := { 0 }

#### To shift the copyright up/down on creatures/walkers, if the pt/loyalty box is very short/tall:
information_copyright_offset_pt_top := { 0 }

#### To shift the secondary copyright left/right on creatures/walkers, if the pt/loyalty box is very narrow/wide:
information_secondary_offset_pt_left := { 0 }

#### For the other faces on DFC or TFC templates, use:
information_offset_top_2 := { 0 }
information_codes_offset_left_2 := { 0 }
information_copyright_offset_right_2 := { 0 }
information_copyright_offset_pt_top_2 := { 0 }
information_secondary_offset_pt_left_2 := { 0 }
information_offset_top_3 := { 0 }
information_codes_offset_left_3 := { 0 }
information_copyright_offset_right_3 := { 0 }
information_copyright_offset_pt_top_3 := { 0 }
information_secondary_offset_pt_left_3 := { 0 }

#### These work the same on 90° rotated cards, but you need to imagine the card is upright

#### You can disable the copyright on some of the faces,
#### by adding the following functions in the init script:
information_disabled := { true }
information_disabled_2 := { true }
information_disabled_3 := { true }
