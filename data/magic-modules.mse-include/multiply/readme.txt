#### To use this include in a template, add the following in the template headers:
depends on:
	package:			magic-modules.mse-include
	version:			2026-08-28

#### This contains color values to Multiply an image, to darken elements for back faces, levelers, etc.
#### It has two scripts defined in the base game, so nothing needs added to the style file.
color_multiply(
	input,			## card color, or color letter
	image,			## image to multiply
	height,			## height of that image
	width,			## width of that image
	multiply_mask,	## optional mask, only the white sections will be multiplied
	iterate,		## optional number of times to multiply, accepts decimals
)

#### Customization
#### The color swatch to use is defined by the function
blend_multiply_template := {
	resize_image("/magic-modules.mse-include/multiply/{input}.png", width:width, height:height)
}
#### You can choose different colors by redefining this to point to a different folder.
#### It needs to contain new images for wubrgacm, and a white pixel named "white"