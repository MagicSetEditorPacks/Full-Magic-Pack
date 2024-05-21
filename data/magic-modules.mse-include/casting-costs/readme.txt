#### Consider using the Namelines module instead of this one.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20
#### Use the highest date version needed among modules

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/casting-costs/card_fields
#### For DFC or TFC templates, instead use:
include file: /magic-modules.mse-include/casting-costs/card_fields_dfc
include file: /magic-modules.mse-include/casting-costs/card_fields_tfc

#### Customization
#### Optionally, you can define which face of the card the casting cost should snap to,
#### by defining the following function in the init script:
nameline_face := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the casting cost by:

#### To shift the casting cost up/down:
casting_cost_offset_top := { 0 }

#### To shift the casting cost left/right:
casting_cost_offset_left := { 0 }

#### To increase/decrease the width and height of the casting cost:
casting_cost_offset_width := { 0 }
casting_cost_offset_height := { 0 }

#### And move the casting costs with:
casting_cost_offset_top_2 := { 0 }
casting_cost_offset_left_2 := { 0 }
casting_cost_offset_width_2 := { 0 }
casting_cost_offset_height_2 := { 0 }
casting_cost_offset_top_3 := { 0 }
casting_cost_offset_left_3 := { 0 }
casting_cost_offset_width_3 := { 0 }
casting_cost_offset_height_3 := { 0 }