import os
import random
from PIL import Image

intermediate = 'intermediate/'
output = 'output/mixed/'

# change your max image width here:
sizex = 1920

# the functions used to combine images, max 4
def concat_2(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def concat_3(im1, im2, im3):
    dst = Image.new('RGB', (im1.width + im2.width + im3.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    return dst

# walk through the base diectory and iterate over the files inside it
image_list = []
for dirpath, dirnames, files in os.walk(intermediate):
    for file in files:
        img_path = os.path.join(dirpath, file)
        image_list.append(img_path)
exists_list = []
for dirpath, dirnames, files in os.walk(output):
    for file in files:
        exists_path = os.path.join(dirpath, file)
        exists_list.append(exists_path)

# 	make list of remaining files and put in random order
random.shuffle(image_list)

# count array items and process if more than 1
i = len(exists_list) + 1
x = 1
place = 0
# check if there are more images left
while place <= len(image_list) - 1:
    if place < len(image_list) - 2:
        im1 = Image.open(image_list[place])
        im2 = Image.open(image_list[place + 1])
        im3 = Image.open(image_list[place + 2])
        # check if 3 works
        if im1.width + im2.width + im3.width <= sizex:
            concat_3(im1, im2, im3).save('output/mixed/mixed' + str(i) + '.jpg')
            im1.close()
            im2.close()
            im3.close()
            os.remove(image_list[place])
            os.remove(image_list[place + 1])
            os.remove(image_list[place + 2])
            i += 1
            place += 3
            print('saved 3')
        # check if 2 works
        elif im1.width + im2.width <= sizex:
            concat_2(im1, im2).save('output/mixed/mixed' + str(i) + '.jpg')
            im1.close()
            im2.close()
            os.remove(image_list[place])
            os.remove(image_list[place + 1])
            i += 1
            place += 2
            print('saved 2')
        # give up and leave it alone
        else:
            x += 1
            place += 1
            print('left 1 alone')
    elif place < len(image_list) - 1:
        im1 = Image.open(image_list[place])
        im2 = Image.open(image_list[place + 1])
        # check if 2 works
        if im1.width + im2.width <= sizex:
            concat_2(im1, im2).save('output/mixed/mixed' + str(i) + '.jpg')
            im1.close()
            im2.close()
            os.remove(image_list[place])
            os.remove(image_list[place + 1])
            i += 1
            place += 2
            print('saved 2')
        # give up and leave it alone
        else:
            x += 1
            place += 1
            print('left 1 alone')
    else:
        x += 1
        place += 1
        print('left 1 alone')

print("finished")