from get_connect import get_connect
import io
import sys
import time
import os

# 检查依赖项
try:
    import selenium
except ImportError:
    print("请安装selenium库,可以使用pip install selenium安装")
    time.sleep(50)
    exit()

# 检查edge浏览器"msedge.exe"是否安装
if not os.path.exists(
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
):
    print(
        "请安装edge浏览器,并将其安装目录添加到系统环境变量中,或者修改get_connect.py中的webdriver.Edge()为webdriver.Chrome()或者webdriver.Firefox()"
    )
    time.sleep(50)
    exit()

# 检查edgedriver是否安装在.\edgedriver_win64\msedgedriver.exe
if not os.path.exists(".\\edgedriver_win64\\msedgedriver.exe"):
    print(
        "请下载edgedriver,并将其放在当前目录下的edgedriver_win64文件夹中,下载地址:https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
    )
    time.sleep(50)
    exit()

# 检查配置文件是否存在
if not os.path.exists("config.json"):
    print("请创建.\config.json文件,并按照如下的格式填写")
    print('''
        {
            "users": [
                {
                    "username": "UXXXXXXXXX",
                    "password": "xxxxxxxxx"
                },
                {
                    "username": "MXXXXXXXXX",
                    "password": "xxxxxxxxx"
                }
            ]
        }
    ''')
    time.sleep(50)
    exit()


def is_connected():
    # 使用ping命令ping www.baidu.com，如果成功，返回0
    return os.system("ping -n 1 www.baidu.com") == 0

print("欢迎使用MentoHUST2024   版本号:0.1.0 alpha1")
print("人到华中大,有甜亦有辣.明德厚学地,求是创新家.")

while True:
    # 检查网络连接
    if not is_connected():
        # 如果没有网络连接，执行get_connect函数
        old_stdout = sys.stdout  # 创建一个StringIO对象并将其设置为系统的标准输出
        sys.stdout = message = io.StringIO()
        # 请在这里修改get_connect()的参数,或自己写不同情况下给get_connect()传入不同参数
        msg = get_connect()  # =get_connect(0)#默认使用第一个用户
        # 恢复系统的标准输出
        sys.stdout = old_stdout
        print(msg)
        # 检查网络是否连接上
        if msg == "登录成功":
            print("网络重连成功")
        else:
            if msg == "登录失败":
                print("网络重连失败")
            else:
                if msg == "已经登录":
                    print(
                        "已经登录,请检查代理和网络环境,可能是网络环境不稳定或者代理失效"
                    )
                else:
                    print("未知错误")
        message_str = message.getvalue()
        # 将消息存入文件message.log
        with open("message.log", "a") as f:
            f.write(message_str)
    else:
        print("网络连接正常")
    # 等待5分钟
    time.sleep(20)
