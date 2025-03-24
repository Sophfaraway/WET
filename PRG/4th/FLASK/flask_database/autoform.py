from playwright.sync_api import sync_playwright 
from dotenv import load_dotenv
import os 

def main():

    with sync_playwright() as p: 
        #with - provede a ukončí
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000/form")
        