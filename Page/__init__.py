"""

    __init__.py 机制：可以通过包名.的方式获取 __init__.py模块内的方法或属性
"""
from selenium.webdriver.common.by import By

"""
    以下为：登录页面数据
"""
# 用户名
login_username = By.ID,"com.vcooline.aike:id/etxt_username"
# 密码
login_password = By.ID,"com.vcooline.aike:id/etxt_pwd"
# 登录按钮
login_btn=By.ID,"com.vcooline.aike:id/btn_login"
"""
    以下为：订单管理页面数据
"""