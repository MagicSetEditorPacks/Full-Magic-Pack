#### This include contains standardized assets and code that can help with template creation.
#### To add a module, see the detailed instructions in it's folder's readme.

#### Globally, you must respect the following z index conventions:
-100:	hidden			#### Backend things that should never be visible to the user
0000:	backboard		#### Things (other than the main card frame) that layer behind the art
0100:	illustration	#### Main card art
0200:	background		#### Main card frame. Will need a mask to allow clicking the art beneath.
0300:	trim			#### Effects like vehicle, nyx, and snow that don't spill over the border
0400:	pinline			#### Colored pinlines, pride pinlines
0500:	border			#### Border
0600:	plate editing	#### Major frame pieces: Lesson/Spree handling, Adventure pages, movable typelines
0700:	watermarking	#### Watermarks, loyalty ability stripes, flavor bar, pop-under art (ex: WAR JP Tamiyo's popout goes under the rarity symbol)
0800:	attachments		#### Optional frame additions: Crown, ptbox, level arrows, loyalty boxes, stamps, color indicators, transformation symbols, alias box, flash dot
0900:	text			#### Any text, rarity symbol
1000:	overlays		#### Popout art, foiling and other overlay packages
1100:	corners			#### These must always be last


Notes on z index conventions:

z index can't be scripted, so choices made need to be consistent across a wide range of templates
As such, the card frame goes over the card art:
This means normal card frames need to use a frame mask
Because the alternative is frames like devoid must layer the art over the frame, which is untenable

Trim effects can spill over the pinline and frame plates (such as snow's textbox effect).
However, these will be overruled by conflicting effects at the higher z index (such as Adventure pages).

The main functional difference between "plate editing" and "attachments" is how they interact with watermarking.
When that isn't relevant, consider if the effect is editing the standard version of the frame layout, or adding an extra thing on top
Crowns are treated as the later in the code to allow for more custom crown freedom, even though they do more resemble the former

Text can go at lower z indexes if it's meant to be obscured or behind the watermarking
But generally any user input text should be in the 900 level, on top of all the frame elements

Overlays primarily refer to .mse-include packages that add foiling and other effects, as well as the popout art.
Templates sometimes refer to things like the Vehicle trim as overlays, but these don't belong in this z index unless they must layer over text.

Corners are functionally a special kind of overlay to standardize corners, and get their own section to ensure they always apply last.
This has the minor drawback that popout art can't be applied to the most extreme corners for square-corner cards.
The invisible corner option has been added as a workaround for this.

Specific z indexes
100 Image

200 Card Color

300 Standard color trim
310 Vehicle
320 Snow
330 Nyx

400 Color pinlines
420 Pride pinlines

500 Card border
510 The List dot

600 Moveable name/typelines
610 Name/type caps (spree attachment)
620 Adventure page
640 Leveler backgrounds

700 Textbox background
710 Loyalty ability stripes
720 Watermarks
740 Flavor bar
790 Pop-under art

800 Indicators
800 Legend crown
830 Loyalty boxes
840 PT Box, Leveler arrows, Flash dot
850 Color stamp
860 Holofoil stamp
870 Transform symbol
880 Tombstone/alchemy symbol
880 Alias box

900 Loyalty cost colons
900 User text fields
900 Information below the textbox & credit symbols
920 Casting cost
950 Rarity

1010 Popout art
1050 Overlay package

1100 Partition select
1100 Corners