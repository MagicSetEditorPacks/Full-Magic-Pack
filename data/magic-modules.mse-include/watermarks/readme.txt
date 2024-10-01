#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/watermarks/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/watermarks/card_fields_dfc
include file: /magic-modules.mse-include/watermarks/card_fields_tfc

#### Default Field Placement (@375x523, w=1 h=1)
set code:
	left:   text_left - 10w
	top:    text_top + 3h
	width:  text_width + 20w
	height: text_height - 6h
#### Customization
#### Optionally, you can define which face of the card the watermark should snap to,
#### by defining the following function in the init script:
watermark_face_1 := { 1 }

#### Similarly, you can define which textbox the watermark should snap to:
#### 1 is for card.text, 2 for card.text_2, and 3 for card.text_3
watermark_text_field_1 := { 1 }

#### And which stamp field it should move out of the way for:
watermark_stamp_field_1 := { 1 }

#### You can also adjust global alignment by defining the following functions, again in the init script,
#### which must return an int corresponding to the number of pixels you want to shift the watermark by:

#### To shift the watermark up/down:
watermark_offset_top_1 := { 0 }

#### To shift the watermark left/right:
watermark_offset_left_1 := { 0 }

#### To increase/decrease the width and height of the watermark:
watermark_offset_width_1 := { 0 }
watermark_offset_height_1 := { 0 }

#### To change by how much it moves when a stamp is present:
watermark_offset_stamp_1 := { 0 }

#### If the textbox is very dark, you can use white watermarks instead of black:
invert_watermark_1 := { true }

#### For DFC or TFC templates, use:
watermark_text_field_2 := { 2 }
watermark_stamp_field_2 := { 2 }
watermark_offset_top_2 := { 0 }
watermark_offset_left_2 := { 0 }
watermark_offset_width_2 := { 0 }
watermark_offset_height_2 := { 0 }
watermark_text_field_3 := { 3 }
watermark_stamp_field_3 := { 3 }
watermark_offset_top_3 := { 0 }
watermark_offset_left_3 := { 0 }
watermark_offset_width_3 := { 0 }
watermark_offset_height_3 := { 0 }
etc...