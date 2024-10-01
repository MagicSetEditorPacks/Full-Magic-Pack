#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Add the following line, indented by one tab, in the init script section:
	include file: /magic-modules.mse-include/loyalty/init_script

#### Add the following line,unindented, in the styling field section:
include file: /magic-modules.mse-include/loyalty/styling_fields

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/loyalty/card_fields

#### Sub-include files are also available for
#### Only the ability fields
include file: /magic-modules.mse-include/loyalty/ability_fields
#### Only the ability separator fields
include file: /magic-modules.mse-include/loyalty/separator_fields
#### Only the ability background striping fields
include file: /magic-modules.mse-include/loyalty/stripe_fields
#### Only the ability formatting styling options
include file: /magic-modules.mse-include/loyalty/styling_formatting
#### Only the ability recoloring styling options
include file: /magic-modules.mse-include/loyalty/styling_recoloring

#### Customization
#### Optionally, you can adjust appearance by defining the following functions in the init script:

#### To conditionally enable loyalty boxes, for combined planeswalker/nonwalker templates
loyalty_has_abilities_1 := { mainframe_walker() }

#### To change which face of the card the boxes go on:
loyalty_face_1 := { 1 }

#### To change which card field the boxes snap to,
#### 1 is for card.text, 2 for card.text_2, and 3 for card.text_3
loyalty_text_field_1 := { 1 }

#### This text field's font color should be:
color: { styling.rule_text_color }

#### To move the starting loyalty up/down:
loyalty_offset_top_1 := { 0 }

#### To move the starting loyalty left/right:
loyalty_offset_left_1 := { 0 }

#### To increase/decrease the starting loyalty size:
loyalty_offset_width_1 := { 0 }
loyalty_offset_height_1 := { 0 }

#### Similarly for loyalty costs of abilities:
loyalty_cost_offset_top_1 := { 0 }
loyalty_cost_offset_left_1 := { 0 }
loyalty_cost_offset_width_1 := { 0 }
loyalty_cost_offset_height_1 := { 0 }

#### To increase/decrease by how much the text becomes indented when a loyalty cost is active:
loyalty_cost_offset_text_margin_1 := { 0 }

#### To change where the stripes separating the abilities appear on the face:
#### This must return the path of a mask with the same dimensions as the face the boxes go on.
#### It must have white pixels where the stripes are visible, and black where they are not visible
loyalty_textbox_mask_1 :=
{
	if is_stamped()
	then "/magic-modules.mse-include/loyalty/default_textbox_stamp_mask.png"
	else "/magic-modules.mse-include/loyalty/default_textbox_mask.png"
}
