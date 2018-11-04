import sys,os
# 获取当前目录
"""
    1. os.getcwd(): 获取当前模块绝对路径
    2. os.sep(): 打印出来就是 /或\ 如果你是windows系统打印出\,如果是mac系统/ 
                 （作用：动态后去/或\）
"""
print(os.getcwd())
print(os.getcwd()+os.sep)
# 给系统path环境添加路径 执行文件当前目录
sys.path.append(os.getcwd())