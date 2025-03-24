from playwright.sync_api import sync_playwright 
from dotenv import load_dotenv
import os 

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

def main():

    with sync_playwright() as p: 
        #with - provede a ukončí
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz/")

        page.click('span[class="login pl-2"]')

        page.fill('input[id="username"]', login)
        page.fill('input[id="password"]', password)

        page.click('button[id="loginbtn"]')

        # page.locator('span:has_text=("PRG - 4G - 24/25")').click()
        page.goto("https://www.moodle-trebesin.cz/course/view.php?id=277")

        page.goto("https://www.moodle-trebesin.cz/mod/quiz/view.php?id=20378")
        
        # page.click('button[id="single_button6799e4ea749094"]')
        page.click('button[class="btn btn-primary"]')
        submitprint = page.click('input[id="id_submitbutton"]')
        print(submitprint)

        # page.wait_for_timeout(1000)
        # page.click('input[name="q2957:1_answer"]:nth-of-type(1)')
        page.click('div[class="r0"]')
        page.get_by_text("Další stránka")

        input("Klikni na cokoliv pro zavření prohlížeče")
        browser.close()

if __name__ == "__main__":
    main()