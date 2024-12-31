# import options as options
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# import chromedriver_autoinstaller as chromedriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(ChromeDriverManager().install())


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

chrome_options = Options() 

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return driver

# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# @pytest.fixture()
# def browser(browser):
#     global web_driver
#     if browser.param == "chrome":
#         web_driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
#     if browser.param == "firefox":
#         web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     browser.cls.driver = web_driver
#     yield
#     web_driver.close()

# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def driver(request):
#     global driver
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Unsupported browser: {request.param}")
#
#     yield driver
#     driver.quit()



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

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html('<div style="background:yellow;">Additional HTML</div>'))
#         report.extra = extra










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
