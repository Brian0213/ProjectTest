from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver=webdriver.Chrome(r"C:\Users\oluse\Downloads\chromedriver_win32 (11)\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed()
        if status==True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLogo", attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_listemployees(self):
        pytest.skip("I will implement later....")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        act_title=self.driver.title

        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False