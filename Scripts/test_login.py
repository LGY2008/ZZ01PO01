import os,sys

import allure
import pytest

sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.page_login import PageLogin
class TestLogin():
    # setup
    def setup_class(self):
        # 实例化 pagelogin
        self.login=PageLogin(get_driver())
    # teardown
    def teardown_class(self):
        # 关闭driver
        self.login.driver.quit()
    # 测试方法 test_login
    @allure.step("开始登陆操作")
    def test_login(self,username="123123",password="123123"):
        # 输入用户名
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_password(password)
        # 点击登录
        self.login.page_click_login_btn()
        # 断言
        try:
            result=self.login.page_get_toast("密码错误")
            print("获取出来的toast消息为：", result)
            assert "密码错误" in result

            # 提示断言成功
            print("断言成功！")
        except:
            # 截图
            self.login.base_get_screen()
            with open("./Image/faild.png","rb") as f:
                # 注意写入图片的方法，还是使用 attach 参数：描述，图片流，图个片格式
                allure.attach("描述",f.read(),allure.attach_type.PNG)
            # 抛异常
            raise