from selenium import webdriver
from selenium.webdriver.common.by import By
import  time







browser = webdriver.Chrome()
browser.get('http://www.taobao.com')

#单个元素
input_first = browser.find_element_by_id('q')
input_second= browser.find_all_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id=q]')
input_fourth= browser.find_element(By.ID,'q')
print(input_first,input_second,input_third,input_fourth)
#多个元素
lis_0 = browser.find_elements_by_css_selector('.service-bd li')
lis_1 =browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis_0)
print(lis_1)
browser.close()

# 对获取的元素调用交互方法
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# browser.close()

# 将动作附加到动作链中串行执行
from selenium.webdriver import ActionChains

# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-example-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

#  执行JavaScript
# browser.get('http://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


# 获取元素信息
# url = 'http://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# print(logo)
# print(logo.get_attribute('class'))
# browser.close()

# 获取ID，位置，标签名，大小
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# 隐式等待
# url = 'http://www.zhihu.com/explore'
# browser.get(url)
# browser.implicitly_wait(10)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

# 显示等待
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser.get('http://www.taobao.com/')
# wait = WebDriverWait(browser,10)
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input,button)


# 前进后退
# browser.get('http://www.baidu.com/')
# browser.get('http://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

# Cookies
# browser.get('http://www.zhihu.com/explore')
# print(browser.get_cookies())
# print('\n')
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# print('\n')
# browser.delete_all_cookies()
# print(browser.get_cookies())


# 选项卡管理

# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com/')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://www.runoob.com/')


# 异常处理


# from selenium.common.exceptions import TimeoutException,NoSuchElementException
# try:
#     browser.get('https://www.baidu.com/')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()
#






#
# browser.find_element_by_xpath()
# browser.find_element_by_id()
# browser.find_element_by_name()
# browser.find_element_by_class_name()
# browser.find_element_by_css_selector()
# browser.find_element_by_link_text()
# browser.find_element_by_partial_link_text()
# browser.find_element_by_tag_name()