# server 启动参数
from appium import webdriver

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# 指定appium框架版本
# desired_caps['automationName'] = 'Uiautomator2'
# 设置中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# app的信息 com.vcooline.aike/.umanager.LoginActivity
desired_caps['appPackage'] = 'com.vcooline.aike'
desired_caps['appActivity'] = '.umanager.LoginActivity'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 测试隐式等待是否可用
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[contains(@text,'登1录')]").click()
driver.get_screenshot_as_file()