#### This include covers the saga textboxes, including the separators between textboxes,
#### chapter icons, and the watermark.

#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Add the following line, unindented, in the styling field section:
include file: /magic-modules.mse-include/chapters/styling_fields

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/chapters/card_fields

#### Customization
#### Optionally, you can adjust appearance by defining the following functions in the init script:

#### To change which face of the card the boxes go on:
saga_face_1 := { 1 }

#### To change where the bounds of the reminder textbox are:
saga_reminder_text_offset_left_1 :=		{ 0 }
saga_reminder_text_offset_top_1 :=		{ 0 }
saga_reminder_text_offset_width_1 :=	{ 0 }
saga_reminder_text_offset_height_1 :=	{ 0 }
#### By default, the reminder text ends where the ability textboxes start.

#### To change where the bounds of the ability textboxes are:
saga_text_offset_left_1 :=				{ 0 }
saga_text_offset_top_1 :=				{ 0 }
saga_text_offset_width_1 :=				{ 0 }
saga_text_offset_height_1 :=			{ 0 }

#### To change the position of the chapter icons:
saga_chapter_offset_left_1 :=			{ 0 }
saga_chapter_offset_top_1 :=			{ 0 }
saga_chapter_offset_width_1 :=			{ 0 }
saga_chapter_offset_height_1 :=			{ 0 }

#### To change how much space there is between chapter icons:
saga_chapter_offset_spacing_1 :=		{ 0 }

#### To change the position of all the textbox separators (grey bars):
saga_separator_offset_left_1 :=			{ 0 }
saga_separator_offset_top_1 :=			{ 0 }
saga_separator_offset_width_1 :=		{ 0 }
saga_separator_offset_height_1 :=		{ 0 }

#### To additionaly change the position of the first textbox separator,
#### which is between the reminder text and the first ability:
saga_first_separator_offset_left_1 :=	{ 0 }
saga_first_separator_offset_top_1 :=	{ 0 }
saga_first_separator_offset_width_1 :=	{ 0 }
saga_first_separator_offset_height_1 :=	{ 0 }

#### To change how much space there is around the separators:
saga_text_offset_padding_1 :=			{ 0 }

#### To change where the separators between the abilities appear on the face:
#### This must return the path of a mask with the same dimensions as the face the boxes go on.
#### It must have white pixels where the separators are visible, and black where they are not visible
saga_bookmark_mask_1 :=
{
	if	styling.transformation_reminder
	then "/magic-modules.mse-include/bookmarks/744x1039/m15/saga/small/default_bookmark_mask.png"
	else "/magic-modules.mse-include/bookmarks/744x1039/m15/saga/base/default_bookmark_mask.png"
}

#### To move the watermark:
watermark_offset_top_1 := { 0 }
watermark_offset_left_1 := { 0 }
watermark_offset_width_1 := { 0 }
watermark_offset_height_1 := { 0 }

#### To disable the watermark:
watermark_disabled_1 := { true }
