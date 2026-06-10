from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    try:
        print("Navigating to login page...")
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Page title:", page.title())
        print("Page URL:", page.url)
        
        # Fill credentials
        print("Filling credentials...")
        page.locator("xpath=//input[@name='username']").fill("Admin")
        page.locator("xpath=//input[@name='password']").fill("admin123")
        
        # Click login and wait for navigation
        print("Clicking login...")
        page.locator("xpath=//*[@type='submit']").click()
        
        # Wait for a bit
        time.sleep(5)
        print("After click URL:", page.url)
        print("After click Title:", page.title())
    except Exception as e:
        print("Error occurred:", e)
        # Take a screenshot if possible
        try:
            page.screenshot(path="screenshot.png")
            print("Screenshot saved to screenshot.png")
        except Exception as se:
            print("Failed to save screenshot:", se)
    finally:
        browser.close()
