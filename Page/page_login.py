import Page
from Base.base import Base
class PageLogin(Base):

    """
        注意：在page页面封装方法颗粒度的时候，不用刻意去思考到底封装几个方法，那几步操作封装一个方法，应该：
            1. 每步操作单独封装一个方法
            2. 如果后期调用的时候需要多步操作封装成一个方法，那么就单独在封装一个方法，直接调用以上单步方法
    """
    # 输入用户名 封装
    def page_input_username(self,username):
        self.base_input(Page.login_username,username)
    # 输入密码 封装
    def page_input_password(self,password):
        self.base_input(Page.login_password, password)
    # 点击登录 封装
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)
    # 获取toast封装
    def page_get_toast(self,message):
        return self.base_get_toast(message)