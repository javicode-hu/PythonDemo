from selenium import webdriver

brower = webdriver.Chrome()

brower.get('https://www.taobao.com/')
brower.get_cookies()