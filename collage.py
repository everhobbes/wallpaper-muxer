import os
import shutil
import random
from PIL import Image

# change your max image width here:
sizex = 1920
# choose your matching method: options are 'random' or 'simple'
method = 'simple'

# the functions used to combine images
def concat_2(im1, im2):
    order = [im1, im2]
    random.shuffle(order)
    ord1 = order[0]
    ord2 = order[1]
    dst = Image.new('RGB', (ord1.width + ord2.width, ord1.height))
    dst.paste(ord1, (0, 0))
    dst.paste(ord2, (ord1.width, 0))
    return dst

def concat_3(im1, im2, im3):
    dst = Image.new('RGB', (im1.width + im2.width + im3.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    return dst

# walk through the base diectory and make a list of the files and their widths as a 2d array
image_list = []
for dirpath, dirnames, files in os.walk('intermediate/'):
    for file in files:
        img_path = os.path.join(dirpath, file)
        img_width = Image.open(img_path).size[0]
        image_list.append([img_path, img_width])
# Get number of existing files in the output directory so we don't overwrite them
if not os.path.exists('output/mixed/'):
    os.makedirs('output/mixed/')
exists_list = []
for dirpath, dirnames, files in os.walk('output/mixed/'):
    for file in files:
        exists_path = os.path.join(dirpath, file)
        exists_list.append(exists_path)

if method == 'simple':
    # METHOD 1: Simple match smallest to biggest - tends to produce more evenly sized images, and won't leave leftover images.
    # put list into order by width, smallest to largest
    image_list.sort(key=lambda x:x[1])

    # Add first and last width, if last is too wide, save it and remove from list and repeat
    i = len(exists_list) + 1
    while image_list:
        if image_list[0][1] + image_list[-1][1] > sizex:
            # save last image in output and remove
            shutil.copy(image_list[-1][0], 'output/')
            os.remove(image_list[-1][0])
            image_list.pop()
            print('saved 1')
        else:
            # concat and save first and last
            im1 = Image.open(image_list[0][0])
            im2 = Image.open(image_list[-1][0])
            concat_2(im1, im2).save('output/mixed/mixed' + str(i) + '.jpg')
            im1.close()
            im2.close()
            os.remove(image_list[0][0])
            os.remove(image_list[-1][0])
            image_list.pop(0)
            image_list.pop(-1)
            i += 1
            print('saved 2')
# end method 1


elif method == 'random':
    # METHOD 2: Alternate method to match images randomly:
    # make list of remaining files and put in random order
    random.shuffle(image_list)

    # count array items and process if more than 1
    i = len(exists_list) + 1
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
                place += 1
                print('left 1 alone')
        else:
            place += 1
            print('left 1 alone')
# end method 2

else:
    print('please choose a method, either simple or random')

print("finished")