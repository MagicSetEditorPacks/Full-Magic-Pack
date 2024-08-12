#### This include covers the class textboxes, including the separators between textboxes,
#### level label, level costs, and the watermark.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Add the following line,unindented, in the styling field section:
include file: /magic-modules.mse-include/levels/styling_fields

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/levels/card_fields

#### Customization
#### Optionally, you can adjust appearance by defining the following functions in the init script:

#### To change which face of the card the boxes go on:
class_face_1 := { 1 }

#### To change where the bounds of the reminder textbox are:
class_reminder_text_offset_left_1 :=		{ 0 }
class_reminder_text_offset_top_1 :=			{ 0 }
class_reminder_text_offset_width_1 :=		{ 0 }
class_reminder_text_offset_height_1 :=		{ 0 }
#### By default, the reminder text ends where the ability textboxes start.

#### To change where the bounds of the ability textboxes are:
class_text_offset_left_1 :=					{ 0 }
class_text_offset_top_1 :=					{ 0 }
class_text_offset_width_1 :=				{ 0 }
class_text_offset_height_1 :=				{ 0 }

#### To change the position of all the textbox separators (level boxes or grey bars):
class_separator_offset_left_1 :=			{ 0 }
class_separator_offset_top_1 :=				{ 0 }
class_separator_offset_width_1 :=			{ 8 }
class_separator_offset_height_1 :=			{ 0 }

#### To additionaly change the position of the first textbox separator,
#### which is between the reminder text and the first ability:
class_first_separator_offset_left_1 :=		{ 0 }
class_first_separator_offset_top_1 :=		{ 0 }
class_first_separator_offset_width_1 :=		{ 0 }
class_first_separator_offset_height_1 :=	{ 0 }

#### To change how much space there is around the separators:
class_text_offset_padding_1 :=				{ 0 }

#### To change the position of the level cost textboxes:
class_level_cost_offset_left_1 :=			{ 0 }
class_level_cost_offset_top_1 :=			{ 0 }
class_level_cost_offset_width_1 :=			{ 0 }
class_level_cost_offset_height_1 :=			{ 0 }

#### To change the position of the level label textboxes:
class_level_offset_left_1 :=				{ 0 }
class_level_offset_top_1 :=					{ 0 }
class_level_offset_width_1 :=				{ 0 }
class_level_offset_height_1 :=				{ 0 }
