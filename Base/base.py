import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base():
    def __init__(self,driver):
        self.driver=driver
    # 查找元素单独封装，给以下方法使用 click\input
    def base_find_element(self,loc,timeout=3,poll=0.5):
        """
        :param loc: 查找元的方法和值，格式：为元祖  如：(By.XPATH,"//*.....")
        :return: 查找到的元素
        """
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 点击元素封装
    def base_click(self,loc):
        # 调用查找元素方法
        self.base_find_element(loc).click()
    # 元素输入封装
    def base_input(self,loc,text):
        # 调用查找元素方法 获取元素在进行点击
        el=self.base_find_element(loc)
        # 清空操作
        el.clear()
        # 输入元素内容
        el.send_keys(text)
    # 获取toast消息 --》单独讲解
    def base_get_toast(self,message):
        # 方式1 拼接字符串
        msg=By.XPATH,"//*[contains(@text,'"+message+"')]"
        # 方式2
        # msg=By.XPATH,"//*[contains(@text,'%s')]"%message
        """
            str1="//*[contains(@text,'"
            str2="')]"
            str=str1+message+str2
        """
        # 调用查找元素方法 获取元素
        el=self.base_find_element(msg,poll=0.1)
        # 返回元素文本
        return el.text
    # 截图方法 封装
    def base_get_screen(self):
        """由于：失败截图后，我们动态写入allure报告，所有在这里可以把图片的路径和名称写成固定"""
        img_path=os.getcwd()+os.sep+"Image"+os.sep+"faild.png"
        self.driver.get_screenshot_as_file(img_path)
