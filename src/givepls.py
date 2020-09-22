from selenium import webdriver
from time import sleep
import os
from selenium.webdriver import ActionChains

# webpage with stuff that's in stock and a 3080 (for testing the beep)
# dest = "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B002VL5IJO&Quantity.1=1&ASIN.2=B08HR3DPGW&Quantity.2=1"

# the 3080s
dest = "https://www.amazon.com/gp/aws/cart/add.html?ASIN.1=B08HR7SV3M&Quantity.1=1&ASIN.2=B08HR3DPGW&Quantity.2=1&ASIN.3=B08HR3Y5GQ&Quantity.3=1&ASIN.4=B08HH5WF97&Quantity.4=1&ASIN.5=B08HHDP9DW&Quantity.5=1&ASIN.6=B08HBR7QBM&Quantity.6=1&ASIN.7=B08HJS2JLJ&Quantity.7=1&ASIN.8=B08HJTH61J&Quantity.8=1&ASIN.9=B08HBTJMLJ&Quantity.9=1&ASIN.10=B08HJNKT3P&Quantity.10=1&ASIN.11=B08HVV2P4Z&Quantity.11=1&ref_=nav_custrec_signin&&"


projectRootDirectory = os.path.abspath(os.path.dirname(__file__))
chromeDriverBinaryPath = os.path.join(projectRootDirectory, "chromedriver")

while (True):
	driver = webdriver.Chrome(executable_path = chromeDriverBinaryPath)
	driver.get(dest)

	while (True):
		try:
			driver.refresh()
		except Exception as e:
			break

		source = driver.page_source
		
		if ("Qty</td>" in source):
			element = driver.find_element_by_xpath("//input[@name='add']")
			hover = ActionChains(driver).move_to_element(element).click().perform()
			while (True):
				os.system('say "Thirty eighty."')

		sleep(1)
	
