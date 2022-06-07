import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_chrome_options():
    """Setup chrome options and return this"""
    options = Options()
    options.add_argument('chrome')  # Run in "headless" mode, if not need a UI or display server dependencies.
    options.add_argument('--start-maximized')  # Starts the browser maximized, regardless of any previous settings.
    options.add_argument('--window-size=1100,800')  # 1100 x 800 window size
    return options


@pytest.fixture
def get_web_driver(get_chrome_options):
    """Making web driver with our setup options"""
    options = get_chrome_options  # get chrome options
    driver = webdriver.Chrome(options=options, executable_path=r'../webdriver/chromedriver.exe')
    return driver


@pytest.fixture(scope='function')
def setup(request, get_web_driver):
    """Get request and our web driver and """
    driver = get_web_driver  # get driver
    url = 'https://segway.vercel.app'
    if request.cls is not None:  # if our test written in class
        request.cls.driver = driver
    driver.get(url)  # get request to start page
    yield driver
    driver.quit()  # close chrome
