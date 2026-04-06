#### Process to create the symbols, in GIMP 3.0

Create a mask from the symbol, where the symbol is pure white, and the background is pure black
Right click layer > Add layer mask > grayscale copy of layer
Select all pixels, select the layer (not the mask), fill all the layer's pixels with pure red (255,0,0)
Export this to /magic-modules.mse-include/symbols/symbol/flat/
Right click layer > New from visible
Make this newly created layer the only one visible and selected
Rotate layer by negative 45 degrees with interpolation set to cubic
Right click layer > Alpha to selection
Filters menu > Decor > Add bevel... with thickness set to 20, work on copy and keep bump layer unchecked
Select all pixels
Colors menu > Curves... > Click and hold on the center of the graph, then drag that point to coordinates x:250 y:130
Click on the "fx" next to the layer > Merge all active filters down
Rotate by positive 45 degrees
Right click layer > Layer to image size
Export this to /magic-modules.mse-include/symbols/symbol/bevel/

For colors, use whatever texture image you want, it will automatically take the shape of the symbol