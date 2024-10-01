#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Add the following line,unindented, in the styling field section:
include file: /magic-modules.mse-include/foils/styling_fields
#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/foils/card_fields

#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/foils/styling_fields_dfc
include file: /magic-modules.mse-include/foils/card_fields_dfc

include file: /magic-modules.mse-include/foils/styling_fields_tfc
include file: /magic-modules.mse-include/foils/card_fields_tfc

#### The template should either include foil_mask.png, or include this function overwrite
foil_mask_base_image := { "" }

#### foil_mask.png marks the area on the card where the foiling should be applied white
#### and marks where it shouldn't be applied black. It is the same size as the card.
#### you can also define added sections (like a PT box) and removed sections (like a stamp)
#### these will also have foil masks that are the full card size
#### but only the added shape in white or the removed shape in black, with the rest the other color
#### foil_mask_blended_image() will combine these together

#### by default, it expects foil_mask_pt, foil_mask_round, and foil_mask_triangle
#### you can change this by editing these functions
foil_mask_added_sections := {
	output := []
	pt_field := if face == 1 then card.pt else card["pt_" + face]
	if pt_field != "" then output := output + ["foil_mask_pt.png"]
	output
}@(face:1)
foil_mask_removed_sections := {
	output := []
	sh := stamp_shape(field:face)
	if sh == "round" then output := output + ["foil_mask_round.png"]
	else if sh == "triangle" then output := output + ["foil_mask_triangle.png"]
	output
}@(face:1)
