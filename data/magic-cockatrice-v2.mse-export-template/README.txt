MSE to Cockatrice Exporter - README
By K'yoril, using code from Pichoro, Idle Muse, Innuendo and Seeonee
Updated by Reuben Covington

Make sure you have updated cockatrice!

To install, simply copy and paste the magic-cockatrice.mse-export-template into the MSE data folder

To export, open MSE and select HTML in the export dropdown

To use standalone, save the export into the Cockatrice folder located in Users (C:\\Users\[ACCOUNT_NAME]\App Data\Local; App Data may be hidden!)
	change the file path to your file under settings in Cockatrice (Cockatrice will need to restart!)
	
To use images, make a new folder in Cockatrice\pics\downloadedPics (name it your set code) and places you card images in it
 
To use with other cards, simply place the new .xml file in the customsets folder (C:\\Users\[ACCOUNT_NAME]\App Data\Local\Cockatrice\Cockatrice\customsets)
then restart cockatrice


Exporter Options:
Cockatrice Set Type
The description of the set under “Set Type” in Cockatrice, such as Promo or Core. Custom is recommended.

Export Images
Whether to export images and at what quality. JPG images are lower quality but smaller file sizes. PNG images can’t be uploaded to Planesculptors anymore.

Tokens in Separate XML
Separates the tokens into their own file. This is no longer necessary but is still supported.

Append Set Code to Tokens
Enabling this will put your set code at the beginning of all token names. This is highly recommended if you will be combining your set with canon or other custom sets to prevent name conflicts.

Append String to Names
Similar to above, but puts the given string at the beginning of all nontoken names. To do this for specific cards rather than all of them, see !exportname in the next section.

Rarities to Export
Restrict which rarities to export for easier to build commons-draft builds and similar. By default all cards will be exported.


Card Note Tags
This exporter can also check the Card Notes section of each of your cards for a handful of card-specific functions:

!exportname
Within Cockatrice, the card will be referred to by the replacement name given here. Useful for cards that have multiple versions, like basic lands or differently sized tokens.
Examples:
	!exportname Mountain 2
	!exportname 5/5 Zombie

!tapped
This card will enter the battlefield tapped.

!related
Used on tokens. After the related tag, list the card names that produce this token separated by semicolons. You can specify multiple tokens by adding <#> after the card name, or <x> for creating a variable amount. You can repeat card names to create multiple scripts for different values.
Examples:
	!related Ironroot Warlord;Raise the Alarm<2>;
	!related Reckless Endeavor<x>
	!related Increasing Devotion<5>; Increasing Devotion<10>;
	!related Sarkhan, Wanderer to Shiv<conjure>

!tokens
Used primarily for nontoken cards, but otherwise works similarly to above, just in the reverse direction.

!tokens and !related can both use the <conjure> or <persistent> tag, which will cause the token created by this script to not be destroyed when it leaves the battlefield, ideal for supporting Conjure cards. 
Examples:
	!tokens Soldier<2>
	!tokens Shivan Dragon<conjure>



