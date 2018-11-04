from selenium.webdriver.common.by import By

login_btn=By.XPATH,"//*[contains(@text,'登录')]"

print(type(login_btn))

"""
    说明：
        1. 元祖小括号包含 如：(By.XPATH,"//*[contains(@text,'登录')]")
        2. 元祖也可以没小括号(前提：两个值以上，以逗号分隔) 如：login_btn=By.XPATH,"//*[contains(@text,'登录')]"
"""
# 未解包
print("未解包格式：",login_btn)
# 解包 加上单个*号为元祖解包，两个**为字典解包
print("解包格式：",*login_btn)
