from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_button = page.locator("xpath=//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
        self.add_button = page.locator("xpath=//button[contains(., 'Add')]")
        self.pim_button = page.locator("xpath=//span[text()='PIM']/parent::a")
        self.add_employee_tab = page.locator("xpath=//a[text()='Add Employee']")
        
        # Add Employee fields
        self.first_name_input = page.locator("input[name='firstName']")
        self.middle_name_input = page.locator("input[name='middleName']")
        self.last_name_input = page.locator("input[name='lastName']")
        self.employee_id_input = page.locator("xpath=//label[text()='Employee Id']/parent::div/following-sibling::div/input")
        self.file_input = page.locator("input[type='file']")
        self.save_button = page.locator("button[type='submit']")
    
    def click_admin(self):
        self.admin_button.click()

    def click_add(self):
        self.add_button.click()

    def click_pim(self):
        self.pim_button.click()
        
    def click_add_employee_tab(self):
        self.add_employee_tab.click()

    def fill_employee_details(self, first_name, middle_name, last_name, employee_id):
        self.first_name_input.fill(first_name)
        self.middle_name_input.fill(middle_name)
        self.last_name_input.fill(last_name)
        if employee_id:
            self.employee_id_input.click()
            self.page.keyboard.press("Control+A")
            self.page.keyboard.press("Backspace")
            self.employee_id_input.fill(employee_id)

    def upload_profile_picture(self, photo_path):
        if photo_path:
            self.file_input.set_input_files(photo_path)

    def click_save(self):
        self.save_button.click()