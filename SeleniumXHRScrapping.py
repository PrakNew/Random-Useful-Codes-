
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
import chromedriver_autoinstaller
import time
caps = DesiredCapabilities.CHROME
options = ChromeOptions()
driver_path = chromedriver_autoinstaller.install()
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(options=options, executable_path=driver_path,desired_capabilities=caps)
driver.get('https://twitter.com/elonmusk')

time.sleep(8)


def process_browser_log_entry(entry):
    return json.loads(entry['message'])['message']


browser_log = driver.get_log('performance')
events = [process_browser_log_entry(entry) for entry in browser_log if 'manifest.json' in entry['message']]

response_list = [event for event in events if 'json' in event['params'].get('response',{}).get('mimeType','abcd')]
final_response = [json.loads(driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': qw["params"]["requestId"]})['body']) for qw in response_list]
#print(browser_log)
#Following?variables
#manifest.json
