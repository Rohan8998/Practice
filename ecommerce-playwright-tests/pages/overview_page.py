from playwright.sync_api import Page

class OverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("xpath=//*[@id='finish']")

    def finish(self):
        self.finish_button.click()

    def test_finish(self, page):
        self.finish()
        assert page.title() == "Swag Labs"  
        print("Finish successful")