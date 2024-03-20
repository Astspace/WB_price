import requests
from seleniumwire import webdriver
import time
from fake_useragent import UserAgent
import random

url = "https://2ip.ru/"
options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.quit()