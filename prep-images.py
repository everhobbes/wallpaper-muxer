import os
import shutil
from PIL import Image

# enter the directory with your images here:
basepath = 'samples/'

# You can change output folders here:
intermediate = 'intermediate/'
output = 'output/'

# change your desired image size here:
sizex = 1920
sizey = 1080
aspect_ratio = sizey / sizex

# walk through the base diectory and iterate over the files inside it
for dirpath, dirnames, files in os.walk(basepath):
	for file in files:
		#check filetypes to avoid trouble
		if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg') or file.endswith('jfif'):
			img_path = os.path.join(dirpath, file)
			# do something with the files
			with Image.open(img_path) as img:
				# save perfect files to the output folder immediately
				if img.size == (sizex, sizey):
					shutil.copy(img_path, output)
				# save perfect height files to the intermediate folder immediately
				elif img.height == (sizey):
					shutil.copy(img_path, intermediate)
				else:
					# reszise height to desired height and save to intermediate folder
					ratio = img.height / img.width
					# 1920 x 1080 apect ratio is 0.5625
					if ratio < aspect_ratio:
						hit = int(sizex * ratio)
						img = img.resize((sizex, hit))
						img = img.convert("RGB")
						img.save(output + file)
						print('wide')
					else:
						wid = int(sizey / ratio)
						img = img.resize((wid, sizey))
						img = img.convert("RGB")
						img.save(intermediate + file)
						print('portrait')
		else:
			print('not an image file')

print("finished")