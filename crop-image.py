from os import listdir
from os.path import isfile, join
from PIL import Image

img_path = 'C:\\Users\\Public\\Downloads\\screenshots\\'
output_path = 'C:\\Users\\Public\\Pictures\\cropped\\'
crop_size = (0, 34, 750, 1334)
resize_w = 282 #int(input('width: '))
resize_h = 502 #int(input('height: '))
onlyfiles = [f for f in listdir(img_path) if isfile(join(img_path, f))]
#print(onlyfiles)
for f in onlyfiles:
    print('current image: ' + f)
    img = Image.open(img_path + f)
    cropped_img = img.crop(crop_size)
    cropped_img = cropped_img.resize((resize_w, resize_h), Image.ANTIALIAS)
    print('save path:' + output_path + f)
    cropped_img.save(output_path + f)

print('End')

