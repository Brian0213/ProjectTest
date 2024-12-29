import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilis.readProperties import ReadConfig
from utilis.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******** Verifying Login test ********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(10)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(8)
        self.logger.info("******** Login Test is successful *******")
        self.driver.quit()
        # act_title = self.driver.title
        # # assert =1 ,2
        # if act_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot("/Users/oluse/PycharmProjects/ProjectTest/Screenshots/Failed.png")
        #     self.driver.close()
        #     assert False
        # self.driver.assert_text()
        # self.driver.save_screenshot("/Users/oluse/PycharmProjects/ProjectTest/Screenshots/LoginPage.png")
        # self.driver.close()
        # self.driver.quit()














    # @pytest.mark.regression
    # def test_homePageTitle(self, setup):
    #     self.logger.info("******** Test_001_Login *******")
    #     self.logger.info("******** Verifying Home Page Title *******")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     self.driver.quit()
    #     print(act_title)
    #     self.driver.save_screenshot("/Users/ooojeyin/PycharmProjects/SDET/Screenshots/test_homepagetitle.png")
    #     # if act_title == "CLEO Dashboard":
        #     assert True
        #     self.driver.quit()
        #     self.logger.info("******** Home page title passed *******")
        # else:
        #     self.logger.error("******** Home page title failed *******")
        #     assert False
        #     # self.driver.save_screenshot("/Users/ooojeyin/PycharmProjects/SDET/Screenshots/test_homePageTitle.png")
        #     # self.driver.close()



        #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

            # self.driver.close()

# baseURL = "https://dev.cleodv.xyz"
# username = "ooojeyinka@armstrongceilings.com"
# password = "Armstrong1$"

# ReadConfig.getApplicationURL()