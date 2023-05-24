## Purpose
This programme is used for making mobile device screencaptures.  
It will visit desired website in mobile mode, and capture the screenshots automatically.  
The screenshots will then be cropped into desired size as to fit the image frame of the mobile device.  
Finally, the cropped images will be merged to the mobile device frame 

## Usage
1. update the `url` in 1-capture-node-screenshot.py
2. update the `playwright.devices['iPhone XR']` device value in 1-capture-node-screenshot.py to fit your need
3. update the playwright behaviour in 1-capture-node-screenshot.py, so that it can visit the website automatically
4. update the cropping size in 2-crop-image.py to desired values
5. prepare the image file of the mobile device, update the image path and image position in 3-merge-to-frame.py
6. run the python scripts in sequence, i.e. from 1 to 3

## Requirement
1. Python 3.10.10
2. Playwright
3. Pillow
