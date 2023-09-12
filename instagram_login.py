from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = "username"
password = "password"


def init_driver(
    headless=True, proxy=None, show_images=False, option=None, firefox=False, env=None
):
    """initiate a chromedriver or firefoxdriver instance
    --option : other option to add (str)
    """

    options = ChromeOptions()
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}
    if headless is True:
        options.add_argument("--disable-gpu")
        options.headless = True
    else:
        options.headless = False
    options.add_argument("log-level=3")
    options.add_argument("--no-sandbox")

    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    if proxy is not None:
        options.add_argument(f"--proxy-server={proxy}")
    if show_images == False and firefox == False:
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
    if option is not None:
        # options.add_argument("--incognito")
        options.add_argument(option)

    if firefox:
        driver = webdriver.Firefox(options=options)
    else:
        driver = driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
            desired_capabilities=caps,
        )

    driver.set_page_load_timeout(100)
    return driver


# Initialize the WebDriver
driver = init_driver(headless=False, firefox=False, option="--incognito")
# driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the page to load (you can adjust the time as needed)
driver.implicitly_wait(10)
# print(dir(driver))
# time.sleep(10)
find_element_timeout = 5
# Locate the username and password input fields and the login button
username_input = WebDriverWait(driver, find_element_timeout).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
)
username_input.send_keys(username)
password_input = WebDriverWait(driver, find_element_timeout).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
)
password_input.send_keys(password + Keys.RETURN)

# username_input = WebDriverWait(driver, find_element_timeout).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
# )


# Wait for the login to complete (you can add more logic to check for successful login)
# driver.implicitly_wait(10)
time.sleep(10)
save_info_button = WebDriverWait(driver, find_element_timeout).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='button']"))
)
save_info_button.click()
turn_off_notification = WebDriverWait(driver, find_element_timeout).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "._a9--._a9_1"))
)
turn_off_notification.click()
# Close the browser (you can remove this line if you want to keep the browser open)
driver.quit()
# driver.get("https://www.instagram.com")
# print(1 / 0)
