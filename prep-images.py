print("starting")

import os
import shutil
from PIL import Image

# enter the directory with your images here:
basepath = 'F:/Personal/Pictures/Artwork/'

# You can change output folders here:
intermediate = 'intermediate/'
output = 'output/'

# walk through the base diectory and iterate over the files inside it
for dirpath, dirnames, files in os.walk(basepath):
	for file in files:
		#check filetypes to avoid trouble
		if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg') or file.endswith('jfif'):
			img_path = os.path.join(dirpath, file)
			# do something with the files
			with Image.open(img_path) as img:
				# save perfect files to the output folder immediately
				if img.size == (1920, 1080):
					shutil.copy(img_path, output)
				# save perfect height to the intermediate folder immediately
				elif img.height == (1080):
					shutil.copy(img_path, intermediate)
				else:
					# reszise height to 1080 and save to intermediate folder
					ratio = img.height / img.width
					if ratio < 0.5625:
						# do something
						hit = int(1920 * ratio)
						img = img.resize((1920, hit))
						img = img.convert("RGB")
						img.save(output + file)
						print('wide')
					else:
						# do something
						wid = int(1080 / ratio)
						img = img.resize((wid, 1080))
						img = img.convert("RGB")
						img.save(intermediate + file)
						print('portrait')
		else:
			print('this is not an image file')

print("finished")