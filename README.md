# wallpaper-muxer
Takes input images and resizes and combines them as close as possible to 1920 x 1080 for use as wallpapers

Usage:
Edit the "pre-images.py" file to choose your input images folder, or leave as is and copy your images to the "samples" folder.

Run "pre-images.py" to do the initial sizing and image sorting. Images that are already 1920 x 1080 or are already exactly 1080px tall will be moved immediately to the output folder. Images different than those dimensions will be scaled down or up respectively, then saved to the intermediate folder.

Once the pre-processing is done, run "collage.py". It will randomize the list of images from the "intermediate" folder, and collage them together into groupings that fit within 1920px wide. Usually this means 2 images will be combined (max is 3). The resulting image will be saved to the output folder, and the used images will be deleted from the intermediate folder.

Multiple runs can be done of "collage.py" back to back to re-randomize the remaining images to try to combine them. After a few runs, you should be left with images that are too wide to combine together. You can then cut and paste those remaining images into the output folder manually (or do whatever you want with them, I'm not your mom).

