from os import listdir
from os.path import isfile, join
from PIL import Image

crop_size = (0, 0, 0, 0) # top-left, top-right, bottom-left, bottom-right
img_path = ''
output_path = ''
phone = int(input('XR or SE? XR = 1, SE = 2 : '))
if phone == 1:
    crop_size = (0, 0, 828, 1620)
    img_path = 'C:\\Users\\Public\\Pictures\\iphoneXR\\raw\\'
    output_path = 'C:\\Users\\Public\\Pictures\\iphoneXR\\output\\cropped\\'
else:
    crop_size = (0, 140, 750, 1245)
    img_path = 'C:\\Users\\Public\\Pictures\\iphoneSE\\raw\\'
    output_path = 'C:\\Users\\Public\\Pictures\\iphoneSE\\output\\cropped\\'

#resize_w = 282 #int(input('width: '))
#resize_h = 502 #int(input('height: '))
onlyfiles = [f for f in listdir(img_path) if isfile(join(img_path, f))]
#print(onlyfiles)
for f in onlyfiles:
    print('current image: ' + f)
    img = Image.open(img_path + f)
    cropped_img = img.crop(crop_size)
    #cropped_img = cropped_img.resize((resize_w, resize_h), Image.ANTIALIAS)
    cropped_img.save(output_path + f)

print('save path:' + output_path)
print('End')

