import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    extensions = ("load-extension=C://Users//danik//AppData//Local//Google//Chrome//User Data//Default//Extensions//jajikjbellknnfcomfjjinfjokihcfoi//3.0.15_0")
    options = Options()
    options.add_argument(f"{extensions}")
    options.add_argument("--no=sandbox")
    options.add_argument("--windows-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
