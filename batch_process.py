#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import os

def batch_process_images(timg, tdrawable, input_folder, output_folder):
    """
    Resize, sharpen, and grayscale all images in 'input_folder',
    saving them to 'output_folder'.
    """
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            # 1. Load image
            in_path = os.path.join(input_folder, filename)
            img = pdb.gimp_file_load(in_path, filename)
            layer = pdb.gimp_image_get_active_layer(img)

            # 2. Resize to 800x800
            pdb.gimp_image_scale(img, 800, 800)

            # 3. Apply sharpening
            pdb.plug_in_unsharp_mask(img, layer, 5.0, 0.5, 0)

            # 4. Convert to Grayscale
            pdb.gimp_desaturate_full(layer, 0)

            # 5. Save
            out_path = os.path.join(output_folder, filename)
            pdb.gimp_file_save(img, layer, out_path, out_path)

            pdb.gimp_image_delete(img)  # free memory

register(
    "python-fu-batch-process-images",
    "Batch Process Images",
    "Resize, sharpen, and grayscale images in a folder",
    "Your Name",
    "Your Name",
    "2025",
    "<Image>/Filters/Custom/Batch Process Images...",
    "",
    [
        (PF_DIRNAME, "input_folder",  "Input Folder",  ""),
        (PF_DIRNAME, "output_folder", "Output Folder", "")
    ],
    [],
    batch_process_images
)

main()
