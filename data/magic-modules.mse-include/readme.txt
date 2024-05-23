#### This include contains standardized assets and code that can help with template creation.
#### To add a module, see the detailed instructions in it's folder's readme.

#### Globally, you must respect the following z index conventions:
-100:	hidden			#### Stuff that should never be visible to the user
0000:	backboard		#### Sometimes stuff needs to be layered behind the illustration
0100:	illustration	#### Main card art
0200:	background		#### Main card frame
0300:	trim			#### Vehicle, nyx, things that don't spill over the border
0400:	pinline			#### Colored pinlines, pride pinlines
0500:	border			#### Border
0600:	plate editing	#### Adventure pages, movable typelines, transformation symbol, spree, flash dot
0700:	watermarking	#### Watermarks, loyalty ability stripes, flavor bar
0800:	attachments		#### Crown, ptbox, level box, alias box, loyalty boxes, stamp, rarity symbol, color indicators
0900:	text			#### Any text
1000:	overlays		#### Popout art, overlays
1100:	corners			#### These must always be last
