import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url",
                     default="https://www.mantisbt.org/bugs/my_view_page.php",
                     help="input your target url")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    """ Фикстура инициализации браузера """
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome()
    driver.implicitly_wait(23)
    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture
def user_name_valid():
    return 'irina123'


@pytest.fixture
def email_valid():
    return 'ivira7@yandex.ru'


@pytest.fixture
def password_valid():
    return 'mantis'
