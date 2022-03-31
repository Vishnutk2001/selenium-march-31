from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

product = input("enter product")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("testcase started")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_name("q").send_keys(product)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(5)
print("test case completed")