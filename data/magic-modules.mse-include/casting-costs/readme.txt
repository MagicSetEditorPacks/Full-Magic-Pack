#### Consider using the Namelines module instead of this one.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/casting-costs/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/casting-costs/card_fields_dfc
include file: /magic-modules.mse-include/casting-costs/card_fields_tfc

#### Also add this among the styling field section,
#### (styling fields will appear in the order you place them).
#### This adds a package option to select an alternate mana font for the casting cost.
include file: /magic-modules.mse-include/casting-costs/styling_fields

#### Default Field Placement (@375x523, w=1 h=1)
casting cost:
	right:  346w
	top:    27h
	width:  min(30w, content) + 5w
	height: 21h
#### Customization
#### Optionally, you can define which face of the card the casting cost should snap to,
#### by defining the following function in the init script:
nameline_face_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the casting cost by:

#### To shift the casting cost up/down:
casting_cost_offset_top_1 := { 0 }

#### To shift the casting cost left/right:
casting_cost_offset_left_1 := { 0 }

#### To increase/decrease the width and height of the casting cost:
casting_cost_offset_width_1 := { 0 }
casting_cost_offset_height_1 := { 0 }

#### For DFC or TFC templates, use:
casting_cost_offset_top_2 := { 0 }
casting_cost_offset_left_2 := { 0 }
casting_cost_offset_width_2 := { 0 }
casting_cost_offset_height_2 := { 0 }
casting_cost_offset_top_3 := { 0 }
casting_cost_offset_left_3 := { 0 }
casting_cost_offset_width_3 := { 0 }
casting_cost_offset_height_3 := { 0 }