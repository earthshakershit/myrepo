from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options
from PIL import Image

ch_options = Options()
ch_options.add_argument("--headless")
ch_options.add_argument("--disable-gpu")
ch_options.add_argument("window-size=1500x300")

driver = webdriver.Chrome(options=ch_options)
wait = WebDriverWait(driver, 10)
driver.get("https://www.baidu.com/")
# driver.find_element_by_id('kw').send_keys("Python" + Keys.RETURN)
# first_result = wait.until(presence_of_element_located((By.ID, "content_left")))
# print(first_result.get_attribute("textContent"))
driver.save_screenshot("sb.png")
driver.quit()

img = Image.open('sb.png')
img.show()