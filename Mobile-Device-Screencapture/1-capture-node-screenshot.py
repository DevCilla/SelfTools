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
        now = "-" + datetime.now().strftime('%Y-%m-%d-%H_%M')
        save_path = img_folder + str(cnt) + now + ".png"
        print('URL: ' + i)

        page = context.new_page()
        page.goto(i)
        page.wait_for_load_state()
        handle_agreement_page(page)
        hide_html_element(page)
        page.locator("body").screenshot(path = save_path)
        #print('saved in: ' + save_path)
        cnt += 1

def handle_agreement_page(page):
    checkbox = page.locator("input[type=\"checkbox\"]#agreement").nth(0)
    nextBtn = page.locator("button#btnNext").nth(0)
    if checkbox.is_visible():
        page.evaluate('const btn = document.getElementById("btnNext"); '
                      'btn.removeAttribute("disabled");')
        nextBtn.click()
    page.wait_for_load_state()

def hide_html_element(page):
    page.evaluate('document.getElementsByClassName("ui-grid-b")[1].style.display = "none";'
                  'document.getElementsByTagName("legend")[0].style.display = "none";')

with sync_playwright() as playwright:
    run(playwright)