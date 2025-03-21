#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pencil Drawing Plugin for GIMP 2
# This plugin creates a pencil sketch effect by desaturating the image,
# inverting a blurred copy, blending layers, and optionally enhancing edges.
#
# Author: Your Name
# License: Public Domain or CC0 (whichever you prefer)

from gimpfu import *

def pencil_drawing(img, drawable):
    # GIMP boilerplate: must set image as current context
    gimp.context_push()
    gimp.image_list()
    pdb.gimp_image_undo_group_start(img)
    
    # 1) Duplicate the original layer
    base_layer = pdb.gimp_layer_copy(drawable, True)
    img.add_layer(base_layer, 0)
    
    # 2) Convert the duplicated layer to grayscale
    pdb.gimp_desaturate(base_layer)
    
    # 3) Duplicate the grayscale layer
    invert_layer = pdb.gimp_layer_copy(base_layer, True)
    img.add_layer(invert_layer, 0)
    
    # 4) Invert the duplicate
    pdb.gimp_invert(invert_layer)
    
    # 5) Apply a Gaussian Blur to the inverted layer
    #    (Adjust these blur values for a softer or sharper look.)
    pdb.plug_in_gauss_rle(img, invert_layer, 10.0, 10.0, 1)
    
    # 6) Set the inverted blurred layer to Dodge mode
    #    Depending on your GIMP version, you might have to use LAYER_MODE_DODGE
    invert_layer.mode = LAYER_MODE_DODGE
    
    # 7) Merge the two grayscale layers together for a unified “sketch” look
    merged_layer = pdb.gimp_image_merge_down(img, invert_layer, EXPAND_AS_NECESSARY)
    
    # 8) (Optional) Enhance edges with a slight “Unsharp Mask”
    #    Tweak radius/amount for a stronger or subtler effect
    pdb.plug_in_unsharp_mask(img, merged_layer, 2.0, 0.5, 0)
    
    # 9) (Optional) Adjust contrast/brightness if desired (comment out if not needed)
    #    pdb.gimp_brightness_contrast(merged_layer, 10, 30)
    
    # Finish up
    pdb.gimp_image_undo_group_end(img)
    gimp.context_pop()
    
    # Update display
    pdb.gimp_displays_flush()

# Register plugin with GIMP
register(
    "python_fu_pencil_drawing",
    "Pencil Drawing",
    "Convert an image into a pencil sketch/drawing style",
    "Your Name",
    "Your Name",
    "2025",
    "Pencil Drawing...",
    "*",  # Image types: can use "*" or "RGB*, GRAY*, INDEXED*"
    [
        (PF_IMAGE,    "img",      "Input image",  None),
        (PF_DRAWABLE, "drawable", "Input layer",  None)
    ],
    [],
    pencil_drawing,
    menu="<Image>/Filters/Custom/"  # Where it appears in the menu
)

main()
