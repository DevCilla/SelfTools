from playwright.sync_api import sync_playwright
from datetime import datetime

# currently only support XR
#phone = int(input('XR or SE? XR = 1, SE = 2 : '))
url = [""]
img_folder = 'C:\\Users\\Public\\Pictures\\iphoneXR\\raw\\'
def run(playwright):
    phone = playwright.devices['iPhone XR']
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(**phone)
    browse_and_capture(context, url)
    print('End')

def browse_and_capture(context, links):
    cnt = 0
    for i in links:
        print('URL: ' + i)
        page = context.new_page()
        page.goto(i)
        now = "-" + datetime.now().strftime('%Y-%m-%d-%H_%M')
        save_path = img_folder + str(cnt) + now + ".png"
        page.locator("body").screenshot(path = save_path)
        #print('saved in: ' + save_path)
        cnt += 1

with sync_playwright() as playwright:
    run(playwright)