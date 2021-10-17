from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/home/colab/geckodriver')
driver.get("https://story-ify.blogspot.com/2021/10/make-1250-worldwide-for-each-image-make.html")
time.sleep(15)
driver.get("https://story-ify.blogspot.com/2021/09/earn-100-every-5-minutes-in-free-paypal.html")
time.sleep(5)
clk = driver.find_element_by_xpath("/html/body/div/div[2]/div/a/img")
clk.click()
