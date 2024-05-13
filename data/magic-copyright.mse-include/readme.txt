#### To use this mse-include in a template, add the following into your style file:

#### In the template headers:
depends on:
	package:			magic-copyright.mse-include
	version:			2024-01-29
#### In the init script: section:
include file: /magic-copyright.mse-include/script
#### Before the card fields: section:
include file: /magic-copyright.mse-include/card_fields
#### For DFC frames, instead add
include file: /magic-copyright.mse-include/card_fields_dfc

#### You can adjust global alignment by redefining the following functions after the scripts include statement
#### which must return an int corresponding to the number of pixels you want to shift things by
#### positive numbers move right and down, negative move left and up

#### To shift everything up/down:
copyright_offset_top := { 0 }

#### To shift the card number, set code and artist credit left/right:
copyright_offset_left := { 0 }

#### To shift the actual copyright lines left/right:
copyright_offset_right := { 0 }

#### To shift the copyright up/down on creatures/walkers, if the pt/loyalty box is very short/tall:
copyright_offset_pt_top := { 0 }

#### To shift the secondary copyright left/right on creatures/walkers, if the pt/loyalty box is very narrow/wide:
copyright_offset_pt_left := { 0 }

#### For the other faces on DFCs use:
copyright_offset_top_2 := { 0 }
copyright_offset_left_2 := { 0 }
copyright_offset_right_2 := { 0 }
copyright_offset_pt_top_2 := { 0 }
copyright_offset_pt_left_2 := { 0 }
copyright_offset_top_3 := { 0 }
copyright_offset_left_3 := { 0 }
copyright_offset_right_3 := { 0 }
copyright_offset_pt_top_3 := { 0 }
copyright_offset_pt_left_3 := { 0 }

#### These work the same on 90° rotated cards, but you need to imagine the card is upright

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### You can disable the copyright on some of the faces,
#### by adding the following functions in the init script:
copyright_disabled := { true }
copyright_disabled_2 := { true }
copyright_disabled_3 := { true }
