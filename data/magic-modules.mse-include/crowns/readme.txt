#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Add this, unindented in the styling fields section:
include file: /magic-modules.mse-include/crowns/styling_fields
#### And this, unindented, before the card style section:
include file: /magic-modules.mse-include/crowns/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/crowns/card_fields_dfc
include file: /magic-modules.mse-include/crowns/card_fields_tfc

#### Finally overwrite the template scripts with the mainframe alternates if you haven't already
	template := template_mainframe
	land_template := land_template_mainframe

#### Optionally, the crowns folder can be changed. Default is
crowns_folder := {"/magic-modules.mse-include/crowns/375/"}
