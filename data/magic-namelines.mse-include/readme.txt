#### To use this include in a template, add the following line, not indented, in the card style section:
include file: /magic-namelines.mse-include/complete_namelines

#### Also add the following in the template headers:
depends on:
	package:			magic-namelines.mse-include
	version:			2024-01-29

#### Optionally, you can define which face of the card the nameline should snap to,
#### by defining the following function in the init script:
nameline_face := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the nameline by:

#### To shift the entire nameline up/down (name + casting cost):
nameline_offset_top := { 0 }

#### To shift the entire nameline left/right:
nameline_offset_left := { 0 }

#### To increase/decrease the width of the entire nameline:
nameline_offset_width := { 0 }

#### To increase/decrease the height of the entire nameline:
nameline_offset_height := { 0 }

#### You can also adjust each of the components individually:
name_offset_top := { 0 }
name_offset_left := { 0 }
name_offset_right := { 0 }
name_offset_height := { 0 }

casting_cost_offset_top := { 0 }
casting_cost_offset_left := { 0 }
casting_cost_offset_width := { 0 }
casting_cost_offset_height := { 0 }

#### For the other faces on DFCs or TFCs use:
nameline_offset_top_2 := { 0 }
nameline_offset_left_2 := { 0 }
nameline_offset_width_2 := { 0 }
nameline_offset_height_2 := { 0 }
nameline_offset_top_3 := { 0 }
nameline_offset_left_3 := { 0 }
nameline_offset_width_3 := { 0 }
nameline_offset_height_3 := { 0 }
etc...

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### You can disable the namelines on some of the faces,
#### by adding the following functions:
nameline_disabled := { true }
nameline_disabled_2 := { true }
nameline_disabled_3 := { true }
