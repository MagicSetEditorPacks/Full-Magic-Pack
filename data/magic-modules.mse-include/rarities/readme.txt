#### Consider using the Typelines Module instead of this one

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20
#### Use the highest date version needed among modules

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/rarities/card_fields
#### For DFC or TFC templates, instead use:
include file: /magic-modules.mse-include/rarities/card_fields_dfc
include file: /magic-modules.mse-include/rarities/card_fields_tfc

#### Customization
#### Optionally, you can define which face of the card the rarity should snap to,
#### by defining the following function in the init script:
typeline_face := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the rarity by:

#### To shift the rarity up/down:
rarity_offset_top := { 0 }

#### To shift the rarity left/right:
rarity_offset_left := { 0 }

#### To increase/decrease the width and height of the rarity:
rarity_offset_size := { 0 }

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.
#### And move the rarities with:
rarity_offset_top_2 := { 0 }
rarity_offset_left_2 := { 0 }
rarity_offset_size_2 := { 0 }
rarity_offset_top_3 := { 0 }
rarity_offset_left_3 := { 0 }
rarity_offset_size_3 := { 0 }