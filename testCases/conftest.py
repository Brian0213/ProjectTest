import options as options
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_options = Options()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    # if browser == 'Firefox':
    #     driver1 = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return driver

# s = Service("/Users/ooojeyin/PycharmProjects/SDET/Driver/chromedriver 4")
# webdriver.Chrome(service=s)



# webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome(service=s)
#     # if browser == 'Firefox':
#     #     driver1 = webdriver.Firefox(service=s)
#     return driver




# @pytest.fixture()
# def setup(browser):
#     if browser == 'firefox':
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# #     # if browser == 'Firefox':
# #     #     driver1 = webdriver.Firefox(service=s)
#     return driver



def pytest_addoption(parser):      # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    # This will return the Browser value to the setup method.
    return request.config.getoption("--browser")










# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = ChromeDriverManager(ChromeDriverManager().install())
#         # if browser == 'Firefox':
#         #     driver1 = webdriver.Firefox(service=s)
#     return driver

# driver = webdriver.Chrome(ChromeDriverManager().install())
# s = Service(webdriver.Chrome(ChromeDriverManager().install()))
# ChromeDriverManager(service=s)

# s = Service("/Users/ooojeyin/PycharmProjects/CLEO/Dr/geckodriver")
# webdriver.Firefox(service=s)














    # if browser == 'chrome':
    #     driver = webdriver.Chrome(service=s)
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox(service=f)
    # return driver

    # # m = Service("/Users/ooojeyin/PycharmProjects/CLEO/Driver/msedgedriver")
    # webdriver.Ie(service=m)
    #     print("Launching Chrome browser.......")
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox()
    #     print("Launching Firefox browser.......")
    # # else:
    # #     driver = webdriver.Ie(service=m)






###### PyTest HTML Report #######
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'CLEO'
#     config.metadata['Tester'] = 'Oluwasegun'
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)