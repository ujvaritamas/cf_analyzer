from selenium import webdriver
import time


url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



#selenium container shall run with this command 
server_url = 'http://sel:4444/wd/hub"'
server_url = 'http://sel:4444/wd/hub'

from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = FirefoxOptions()
cloud_options = {}
cloud_options['build'] = "build_1"
cloud_options['name'] = "test_abc"
options.set_capability('cloud:options', cloud_options)
driver = webdriver.Remote(server_url, options=options)

try:
    driver.implicitly_wait(10) # seconds
    driver.get(url)

    time.sleep(10)
    page_source = driver.page_source

    #inputElem = driver.find_element("xpath",'//*[@id="leaderboardSponsorVisible"]/div/div[2]/table/tbody/tr[1]/td[2]/div/div[1]/div[2]/div')
    #implicitly_wait means, wait until the element is found
    #driver.implicitly_wait(10)

    # Open the file for writing
    with open('file.txt', 'w') as f:
        f.write(page_source)
    driver.quit()
except:
    driver.quit()
