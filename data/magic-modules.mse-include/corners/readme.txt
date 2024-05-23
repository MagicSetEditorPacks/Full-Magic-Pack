#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-05-20

#### Also add this, unindented, before the card style section:
include file: /magic-modules.mse-include/corners/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/corners/card_fields_dfc
include file: /magic-modules.mse-include/corners/card_fields_tfc
