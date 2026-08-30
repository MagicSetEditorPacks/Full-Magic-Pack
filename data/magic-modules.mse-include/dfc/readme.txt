#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2026-08-28

#### Also add this, indented, near the top of the init script section
include file: /magic-modules.mse-include/dfc/init_script
#### This, unindented, within the styling section:
include file: /magic-modules.mse-include/dfc/styling_fields
#### And this, unindented, before the card style section:
include file: /magic-modules.mse-include/dfc/card_fields

#### Default Field Placement (@375x523, w=1 h=1)
node:
	left:   0
	top:    0
	width:  card_width
	height: card_height
	z index: 610
meld_bar
	left: 	0
	top:	0
	width:	card_width
	height: card_height
	z index: 1100
back face hint:
	right:	card_width - 28w
	top: 	card_height - 77h
	width:	30w
	height:	12h
	z index: 650
	font color: rgb(45, 45, 45)

#### Additional script
	is_notched() determines if the card should have a transform notch
	force_notched can be defined for a template-specific way to enforce notched, like a styling option
	notch images are not presently supported
	
	is_back_face() determins if the card is a back face
	back face multiply effects are not part of this module
	
	node_mask() returns a card-sized mask where black pixels are where the node is presently
	used for masking around semi-transparent images or dealing with higher-index images
	
	hidden_back_rarity() true if the card is a back face and styilng.hide_back_rarity is true
	currently not integrated into the rarity module

#### Customization
#### The node is built from a folder of card-sized images, with a subfolder "modal" for the pointed variant
#### Mirroring is done by the module
#### Future updates will let you just reuse alias_colors to color the node from a base image

#### The folder of node images. This should have a modal/ subfolder
node_folder := { "/magic-modules.mse-include/dfc/nodes/" }
#### The color to use for the node. Returning "clear" will use "x" as the template letter
node_color := { card.card_color }
#### Turn off the node entirely, for templates that only want the other DFC utility
#### This is not used for turning the node off because the transform symbol is empty
node_disabled := { false }

#### The Meld Bar adds a high z-index bar to give the appearance of two cards
#### It uses the corners module to match the simulated corners in the middle
#### The bar goes across the narrower dimension of the card, no offset is needed for rotated canvases.
#### Is the meld bar active?
use_meld_bar := {
	styling.meld_bar == "yes"
	or (styling.meld_bar == "for melds" and length(get_cards_from_link(card, linked_relation:"Meld Base")) > 0)
}

#### Back face hint determination
#### Prioritizes the back face loyalty/defense if the user has that selected.
back_face_hint := {
	if styling.back_face_hint == "none" then "" else (
		back := get_back_face(card) or else nil
		if back == nil then back := get_cards_from_link(card, linked_relation:"Meld Result").0 or else nil
		if back == nil then ""
		else if styling.back_face_hint == "PT, Loyalty, Defense" and back.loyalty != ""
			then back.loyalty
		else back.pt
	)
}



#### Field Offsets
back_face_hint_offset_left   := { 0 }
back_face_hint_offset_top    := { 0 }
back_face_hint_offset_width  := { 0 }
back_face_hint_offset_height := { 0 }
back_face_hint_disabled		 := { false }

back_face_hint_color 		 := { rgb(45,45,45) }
back_face_stroke_radius 	 := { 0 }
back_face_hint_stroke_color  := { "black" }
