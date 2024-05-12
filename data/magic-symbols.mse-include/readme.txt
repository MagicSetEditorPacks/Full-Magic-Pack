#### To use this include in a template, add the following line, not indented, in the card style section:
include file: /magic-symbols.mse-include/complete_transforms

#### Also add the following in the template headers:
depends on:
	package:			magic-symbols.mse-include
	version:			2024-01-29

#### Optionally, you can adjust global alignment by defining the following functions in the init script,
#### which must return an int corresponding to the number of pixels you want to shift things by:

#### To shift everything up/down:
transform_symbol_offset_top := { 0 }

#### To shift everything left/right:
transform_symbol_offset_left := { 0 }

#### To increase/decrease the size:
transform_symbol_offset_width := { 0 }
transform_symbol_offset_height := { 0 }

#### To move the symbol to the right of the card:
transform_symbol_mirrored := { true }

#### For the other faces on DFCs use:
transform_symbol_offset_top_2 := { 0 }
transform_symbol_offset_left_2 := { 0 }
transform_symbol_offset_width_2 := { 0 }
transform_symbol_offset_height_2 := { 0 }
transform_symbol_offset_mirrored_2 := { 0 }
transform_symbol_offset_top_3 := { 0 }
transform_symbol_offset_left_3 := { 0 }
transform_symbol_offset_width_3 := { 0 }
transform_symbol_offset_height_3 := { 0 }
transform_symbol_offset_mirrored_3 := { 0 }

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### You can disable the symbols on some of the faces,
#### by adding the following functions in the init script:
transform_symbol_disabled := { true }
transform_symbol_disabled_2 := { true }
transform_symbol_disabled_3 := { true }
