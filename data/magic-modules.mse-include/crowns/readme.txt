#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2024-10-01

#### Add this, unindented in the styling fields section:
include file: /magic-modules.mse-include/crowns/styling_fields
#### And this, unindented, before the card style section:
include file: /magic-modules.mse-include/corners/card_fields
#### For DFC or TFC templates, instead override the faces_coordinates function, and use:
include file: /magic-modules.mse-include/corners/card_fields_dfc
include file: /magic-modules.mse-include/corners/card_fields_tfc

#### Finally, the template script must be adjusted like so:

	template := { 
		if type_name(harder_script[type] or else nil) != type_name(nil)
			then harder_script[type](input, land:false)
		else template_prefix[type] + input + template_suffix[type]
	}
	land_template := {
		if type_name(harder_script[type] or else nil) != type_name(nil)
			then harder_script[type](input, land:true)
		else template_prefix[type] + input + (if input == "a" then "" else "l") + template_suffix[type]
	}

	harder_script := [
		crown: module_crown_template
	]

#### Optionally, the crowns folder can be changed. Default is
crowns_folder := {"/magic-modules.mse-include/crowns/375/"}
