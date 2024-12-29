from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://onpointgroup--opgsit.sandbox.lightning.force.com/lightning/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("oluwasegun.ojeyinka@onpointgroup.com.opg.sit")
driver.find_element(By.XPATH, "//input[@name='pw']").send_keys("Welcome@2024")

driver.find_element(By.XPATH, "//input[@name='Login']").click()

# time.sleep(3)
# quote_home=driver.find_element(By.XPATH, "//span[normalize-space()='CPQ Quotes']")
# driver.execute_script("arguments[0].click();", quote_home)
# time.sleep(5)
#
account_tab=driver.find_element(By.XPATH, "//span[normalize-space()='Accounts']")
driver.execute_script("arguments[0].click();", account_tab)

time.sleep(5)
#
account_name=driver.find_element(By.LINK_TEXT, "Miner")
driver.execute_script("arguments[0].click();", account_name)
time.sleep(5)

# outerframe=driver.find_element(By.XPATH, "//slot[@name='sidebar']//flexipage-component2//slot//div[@class='slds-tabs_card']")
# driver.switch_to.frame(outerframe)
# time.sleep(3)


#related_record=driver.find_element(By.XPATH, "//a[@id='collaborateTab__item']")
#driver.execute_script("arguments[0].click();", related_record)

# loc_record=driver.find_element(By.XPATH, "//span[@title='Location - Customer Relationships']")
# driver.execute_script("arguments[0].scrollIntoView(true)", loc_record)
# driver.execute_script("arguments[0].click();", loc_record)
# driver.execute_script("return window.pageYOffset;")
#
# time.sleep(5)

location=driver.find_element(By.XPATH, "//span[normalize-space()='National Sales']")
driver.execute_script("arguments[0].click();", location)
time.sleep(5)
#
# loc_icon=driver.find_element(By.XPATH, "//a[contains(@title,'Show 7 more actions')]//lightning-primitive-icon")
# driver.execute_script("arguments[0].click();", loc_icon)
# time.sleep(5)
#
new_opp=driver.find_element(By.XPATH, "//a[@title='New Opportunity']")
driver.execute_script("arguments[0].click();", new_opp)
time.sleep(5)

windowsIDs = driver.window_handles

parentwindowid=windowsIDs[0] # D188312C40AB8D0198A899FE2F5E00EC
#
# driver.switch_to.window(parentwindowid)
#
# time.sleep(5)
#
# min_sales=driver.find_element(By.XPATH, "//flowruntime-lwc-body/div[1]/flowruntime-list-container[1]/div[1]/flowruntime-base-section[1]/div[1]/flowruntime-screen-field[1]/flowruntime-lwc-field[1]/div[1]/flowruntime-radio-button-input-lwc[1]/fieldset[1]/div[1]/span[1]/label[1]/span[1]")
# driver.execute_script("arguments[0].click();", min_sales)

time.sleep(5)