from selenium import webdriver
driver = webdriver.Firefox(executable_path='/home/colab/geckodriver')
driver.get("http://www.google.com")
