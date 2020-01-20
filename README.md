# wallpaper-muxer
Takes input images and resizes and combines them as close as possible to 1920 x 1080 for use as wallpapers

Usage:

Edit the "pre-images.py" file to choose your input images folder and desired image size (default is 1920 x 1080) or leave as is and copy your images to the "samples" folder.

Run "pre-images.py" to do the initial sizing and image sorting. Images that are already 1920 x 1080 will be moved immediately to the output folder. Images different than those dimensions will be scaled down or up respectively, then saved to the intermediate folder.

Once the pre-processing is done, edit "collage.py" with your desired image size (if different than the default) and run and desired method. It will take images from the "intermediate" folder, and collage them together into groupings that fit within 1920px wide. The resulting image will be saved to the output folder, and the used images will be deleted from the intermediate folder.

There are two methods for combining images: smallest + biggest, or random. Set the preferred method in collage.py. Smallest to biggest tends to create more evenly sized images and won't leave un-matched items.

And voila: perfectly sized images that make use of more of your monitor's space for wallpapers, and can be tiled without cropping.

