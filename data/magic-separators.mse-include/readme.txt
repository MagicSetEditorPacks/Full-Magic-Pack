#### To use this include in a template, add the following line, not indented, in the card style section:
include file: /magic-separators.mse-include/complete_flavor_bar

#### Also add the following in the template headers:
depends on:
	package:			magic-separators.mse-include
	version:			2024-01-29

#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the flavor bar by:

#### To shift the bar up/down:
flavor_bar_offset_top := { 0 }

#### To shift the bar left/right:
flavor_bar_offset_left := { 0 }

#### To increase/decrease the size:
flavor_bar_offset_width := { 0 }
flavor_bar_offset_height := { 0 }

#### For the other faces on DFCs or TFCs use:
flavor_bar_offset_top_2 := { 0 }
flavor_bar_offset_left_2 := { 0 }
flavor_bar_offset_width_2 := { 0 }
flavor_bar_offset_height_2 := { 0 }
flavor_bar_offset_top_3 := { 0 }
flavor_bar_offset_left_3 := { 0 }
flavor_bar_offset_width_3 := { 0 }
flavor_bar_offset_height_3 := { 0 }

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### You can disable the flavor bar on some of the faces,
#### by adding the following functions in the init script:
flavor_bar_disabled := { true }
flavor_bar_disabled_2 := { true }
flavor_bar_disabled_3 := { true }
