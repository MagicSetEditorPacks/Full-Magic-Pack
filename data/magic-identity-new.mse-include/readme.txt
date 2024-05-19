#### To use this include in a template, add the following line, not indented, in the card style section:
include file: /magic-identity-new.mse-include/card_fields

#### Also add the following in the template headers:
depends on:
	package:			magic-identity-new.mse-include
	version:			2024-01-29

#### Optionally, you can define which face of the card the color indicator should snap to,
#### by defining the following function in the init script:
typeline_face := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the color indicator by:

#### To shift the color indicator up/down:
indicator_offset_top := { 0 }

#### To shift the color indicator left/right:
indicator_offset_left := { 0 }

#### To increase/decrease the width and height of the color indicator:
indicator_offset_size := { 0 }

#### For DFC or TFC templates, instead use:
include file: /magic-identity-new.mse-include/card_fields_dfc
include file: /magic-identity-new.mse-include/card_fields_tfc

#### And move the color indicators with:
indicator_offset_top_2 := { 0 }
indicator_offset_left_2 := { 0 }
indicator_offset_size_2 := { 0 }
indicator_offset_top_3 := { 0 }
indicator_offset_left_3 := { 0 }
indicator_offset_size_3 := { 0 }

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### (Consider using the /magic-typelines.mse-include/ instead of this one.)
