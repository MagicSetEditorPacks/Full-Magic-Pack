#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/separators/card_fields
#### For DFC, TFC, or multiple textbox templates, instead use:
include file: /magic-modules.mse-include/separators/card_fields_dfc
include file: /magic-modules.mse-include/separators/card_fields_tfc

#### Customization
#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the flavor bar by:

#### To shift the bar up/down:
flavor_bar_offset_top_1 := { 0 }

#### To shift the bar left/right:
flavor_bar_offset_left_1 := { 0 }

#### To increase/decrease the size:
flavor_bar_offset_width_1 := { 0 }
flavor_bar_offset_height_1 := { 0 }

#### For the other faces on DFC or TFC templates, use:
flavor_bar_offset_top_2 := { 0 }
flavor_bar_offset_left_2 := { 0 }
flavor_bar_offset_width_2 := { 0 }
flavor_bar_offset_height_2 := { 0 }
flavor_bar_offset_top_3 := { 0 }
flavor_bar_offset_left_3 := { 0 }
flavor_bar_offset_width_3 := { 0 }
flavor_bar_offset_height_3 := { 0 }