from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable((By.XPATH, "//input[@id='Email']"))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Email']"))).send_keys(username)

    def setContinue(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).click()

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Password']"))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Password']"))).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log in')]"))).click()
        # self.driver.find_element(By.CLASS_NAME, "self.button_class_name").click()

    def clickDown(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/div[2]/div[3]/button[1]/span[1]/div[2]/*[1]"))).click()

    def clickLogout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//body/div[2]/div[3]/ul[1]/li[1]"))).click()

    def clickProject(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Project Leads')]"))).click()

    def clickFilterNav(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/div[1]/button"))).click()

    def clickShownonlynew(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-disabled='false']//span[1]"))).click()

    def confirmlogo(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//img[@alt='Cleo']"))).click()
