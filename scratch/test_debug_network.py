from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Listeners
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.on("requestfailed", lambda request: print("FAIL >>", request.url, request.failure))
    
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
        
        # Wait for dashboard URL or timeout
        print("Waiting for URL: **/dashboard/index")
        page.wait_for_url("**/dashboard/index", timeout=15000)
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
