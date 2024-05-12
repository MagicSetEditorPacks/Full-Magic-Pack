#### To use this include in a template, add the following line, not indented, in the card style section:
include file: /magic-corners.mse-include/complete_corners

#### Also add the following in the template headers:
depends on:
	package:			magic-corners.mse-include
	version:			2024-01-29

#### For DFC or TFC templates, dont forget to override the faces_coordinates function.

#### Optionally, you can disable the corners on some of the faces,
#### by adding the following functions in the init script:
corners_disabled := { true }
corners_disabled_2 := { true }
corners_disabled_3 := { true }
