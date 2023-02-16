def check_exists_by_xpath(xpath, driver):
    timeout = 3
    try:
        driver.implicitly_wait(1)
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True
  
#driver is the selenium driver which is on the page
countxhr=0
loader_xpath = "//div[contains(@data-testid,'primaryColumn')]//div[@role='progressbar']//div[@style='height: 26px; width: 26px;']" #This is an example for the twitter following page
while check_exists_by_xpath(loader_xpath,driver):
    # print("Yes there is a loader",countxhr)
    countxhr+=1
