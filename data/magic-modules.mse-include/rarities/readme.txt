#### Consider using the Typelines module instead of this one

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/rarities/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/rarities/card_fields_dfc
include file: /magic-modules.mse-include/rarities/card_fields_tfc

#### Also add this among the styling field section,
#### (styling fields will appear in the order you place them):
#### This will add a text option for customizing the colors used by the rarity symbol,
#### and another to further tweak the positioning of the rarity symbol.
include file: /magic-modules.mse-include/rarities/styling_fields

#### Inverted common and olduncommon/oldrare can be added with these after the styling fields
include file: /magic-modules.mse-include/rarities/set_info
include file: /magic-modules.mse-include/rarities/set_info_old

#### Default Field Placement (@375x523, w=1 h=1)
rarity:
	left:   317w
	top:    297h
	width:  24w
	height: 24h
#### Customization
#### Optionally, you can define which face of the card the rarity should snap to,
#### by defining the following function in the init script:
typeline_face_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the rarity by:

#### To shift the rarity up/down:
rarity_offset_top_1 := { 0 }

#### To shift the rarity left/right:
rarity_offset_left_1 := { 0 }

#### To increase/decrease the width and height of the rarity:
rarity_offset_size_1 := { 0 }

#### For DFC or TFC templates, use:
rarity_offset_top_2 := { 0 }
rarity_offset_left_2 := { 0 }
rarity_offset_size_2 := { 0 }
rarity_offset_top_3 := { 0 }
rarity_offset_left_3 := { 0 }
rarity_offset_size_3 := { 0 }