from os import listdir
from os.path import isfile, join
from PIL import Image

phone_frame = ''
img_path = ''
output_path = ''
position = (0, 0) # x,y coordinate of top-left
phone = int(input('XR or SE? XR = 1, SE = 2 : '))
if phone == 1:
    phone_frame = Image.open('C:\\Users\\Public\\Pictures\\iphoneXR\\iphone-xr-frame-2.png')
    img_path = 'C:\\Users\\Public\\Pictures\\iphoneXR\\output\\cropped\\'
    output_path = 'C:\\Users\\Public\\Pictures\\iphoneXR\\output\\merged\\'
    position = (68, 140)
else:
    phone_frame = Image.open('C:\\Users\\Public\\Pictures\\iphoneSE\\iphone-se-frame2.png')
    img_path = 'C:\\Users\\Public\\Pictures\\iphoneSE\\output\\cropped\\'
    output_path = 'C:\\Users\\Public\\Pictures\\iphoneSE\\output\\merged\\'
    position = (40, 345)

onlyfiles = [f for f in listdir(img_path) if isfile(join(img_path, f))]
for f in onlyfiles:
    print('current image: ' + f)
    img = Image.open(img_path + f)
    phone_frame.paste(img, position)
    phone_frame.save(output_path + f)

print('save path:' + output_path)
print('End')
