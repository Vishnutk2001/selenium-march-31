from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

username = input("enter username")
password = input("enter password")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("testcase started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
driver.find_element_by_name("username").send_keys(username)
time.sleep(3)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_class_name("L3NKy").click()
time.sleep(5)
driver.close()
print("testcase completed")



