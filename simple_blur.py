from gimpfu import *

def simple_blur(image, drawable):
    """Applies a Gaussian blur to the active image."""
    pdb.gimp_image_undo_group_start(image)  # Start an undo group
    pdb.plug_in_gauss(image, drawable, 5.0, 5.0, 0)  # Apply Gaussian Blur
    pdb.gimp_image_undo_group_end(image)  # End the undo group
    pdb.gimp_displays_flush()  # Refresh the display

# Register the plugin in GIMP
register(
    "python_fu_simple_blur",
    "Simple Gaussian Blur",
    "Applies a Gaussian blur effect to the active image",
    "Your Name", "Your Name", "2025",
    "<Image>/Filters/Custom/Simple Gaussian Blur",  # Location in the GIMP menu
    "*",  # Works on all image types
    [],
    [],
    simple_blur
)

main()
