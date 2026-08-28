#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2026-08-28

#### Add the following line, unindented, before the card style section:
include file: /magic-modules.mse-include/reminders/card_fields

#### Customization
#### Optionally, you can adjust appearance by defining the following functions in the init script:

#### To move the entire reminder box up/down:
reminder_offset_top := { 0 }

#### To move the entire reminder box left/right:
reminder_offset_left := { 0 }

#### To increase/decrease the reminder box size:
reminder_offset_width := { 0 }
reminder_offset_height := { 0 }

#### Similarly for the type and cost fields within the box:
reminder_type_offset_top := { 0 }
reminder_type_offset_left := { 0 }
reminder_type_offset_width := { 0 }
reminder_type_offset_height := { 0 }
reminder_cost_offset_top := { 0 }
reminder_cost_offset_left := { 0 }
reminder_cost_offset_width := { 0 }
reminder_cost_offset_height := { 0 }

#### To change the folder from which the reminder box images are taken:
#### You must write the path of the folder starting from the data folder.
#### The image files must have the same names, and be placed in the same subfolders as the
#### ones in the default folder (/magic-modules.mse-include/reminders/), and must all be PNGs.
#### You can omit some images and it will use the default ones instead.
reminder_image_folder := { "/magic-modules.mse-include/reminders/" }

#### To change when the box uses the light variant:
reminder_uses_light_variant := { get_front_face(card) != nil }

#### To change how blending works for multicolor cards:
#### This should return either "white" (colored), black (gold), or "mask".
#### If mask, add a mask image file in the template folder (not the reminder_image_folder)
#### called "multicolor_blend_reminder.png". It must have the same dimensions as the box images.
reminder_multicolor_blend := { "white" }

#### Same for artifact and hybrid:
reminder_hybrid_blend := { "white" }
reminder_artifact_blend := { "white" }

#### To define when the box is visible, or to query if it is,
#### for example if other things need to move as a result:
reminder_box_is_visible := { (remove_tags(card.reminder_type) != "" or remove_tags(card.reminder_cost) != "") and not reminder_disabled() }

#### To disable all or part of the reminder box:
reminder_disabled := { true }
reminder_type_disabled := { true }
reminder_cost_disabled := { true }