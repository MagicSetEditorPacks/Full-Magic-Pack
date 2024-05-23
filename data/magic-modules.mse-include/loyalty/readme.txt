#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Add the following line, indented by one tab, in the init script section:
	include file: /magic-modules.mse-include/loyalty/init_script

#### Add the following line,unindented, in the styling field section:
include file: /magic-modules.mse-include/loyalty/styling_fields

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/information/card_fields

#### Customization
#### Optionally, you can adjust appearance by defining the following functions in the init script:

#### To change which face of the card the boxes go on:
loyalty_face := { 1 }

#### To change which card field the boxes snap to,
#### 1 is for card.text, 2 for card.text_2, and 3 for card.text_3
#### This text field and it's watermark should have z index greater than 1100
loyalty_text_field := { 1 }

#### This text field's font color should be:
color: { styling.rule_text_color }

#### To move the starting loyalty up/down:
loyalty_offset_top := { 0 }

#### To move the starting loyalty left/right:
loyalty_offset_left := { 0 }

#### To increase/decrease the starting loyalty size:
loyalty_offset_width := { 0 }
loyalty_offset_height := { 0 }

#### Similarly for loyalty costs of abilities:
loyalty_cost_offset_top := { 0 }
loyalty_cost_offset_left := { 0 }
loyalty_cost_offset_width := { 0 }
loyalty_cost_offset_height := { 0 }

#### To increase/decrease by how much the text becomes indented when a loyalty cost is active:
loyalty_cost_offset_text_margin := { 0 }

#### To change where the stripes separating the abilities appear on the face:
#### This must return the path of a mask with the same dimensions as the face the boxes go on.
#### It must have white pixels where the stripes are visible, and black where they are not visible
loyalty_textbox_mask :=
{
	if is_stamped()
	then "/magic-modules.mse-include/loyalty/default_textbox_stamp_mask.png"
	else "/magic-modules.mse-include/loyalty/default_textbox_mask.png"
}
