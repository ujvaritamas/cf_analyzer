import os
from selenium import webdriver
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions


server_url = os.environ.get('SELENIUM_ADDR')

def save_html_to_file(url, file_path):
    options = FirefoxOptions()
    cloud_options = {}
    cloud_options['build'] = "build_1"
    cloud_options['name'] = "test_abc"
    options.set_capability('cloud:options', cloud_options)
    driver = webdriver.Remote(server_url, options=options)
    logger = logging.getLogger()
    try:
        driver.implicitly_wait(2) # seconds
        driver.get(url)

        time.sleep(2)
        page_source = driver.page_source

        logger.info("Page source saved")

        # Open the file for writing, overwrite if exists
        with open(file_path, 'w') as f:
            f.write(page_source)
        logger.info("Html saved to file: {}".format(file_path))
        driver.quit()
    except:
        driver.quit()
