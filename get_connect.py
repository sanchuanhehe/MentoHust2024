from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.expected_conditions import url_changes
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver import ActionChains
import json


def get_credentials(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["users"]


def get_connect(user_index=None):
    # 连接网络

    # 获取用户信息
    if user_index is not None:
        users = get_credentials("config.json")
        user = users[user_index]
    else:
        users = get_credentials("config.json")
        user = users[0]
    # else:
    #     # 获取用户信息
    #     users = get_credentials("config.json")
    #     # 判断时间范围,在0点到6点之间使用users0,其它时间使用users1
    #     # 获取当前时间
    #     current_time = time.localtime(time.time())
    #     # 获取当前时间的小时,24小时制
    #     current_hour = current_time.tm_hour
    #     # 判定
    #     if current_hour >= 0 and current_hour <= 6:
    #         user = users[1]
    #     else:
    #         user = users[0]

    # 创建 EdgeOptions 对象
    options = Options()
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--ignore-certificate-errors-spki-list")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--enable-chrome-browser-cloud-management")
    # 设置浏览器后台运行
    options.add_argument("--headless")

    # 创建 WebDriver 对象
    service = webdriver.EdgeService('.\edgedriver_win64\msedgedriver.exe')
    driver = webdriver.Edge(options=options)
    # 如果是firefox浏览器,则使用下面的代码
    # driver = webdriver.Firefox(options=options)

    driver.get("http://172.18.18.61:8080")

    WebDriverWait(driver, 100).until(url_changes("http://172.18.18.61:8080"))

    # 检测是否跳转到了登录页面,如跳转的url以http://172.18.18.61:8080/eportal/index.jsp开头,继续执行,如http://172.18.18.61:8080/eportal/success.jsp开头,则说明已经登录,不需要再次登录
    if driver.current_url.startswith("http://172.18.18.61:8080/eportal/index.jsp"):
        print("跳转到了登录页面")
    else:
        if driver.current_url.startswith(
            "http://172.18.18.61:8080/eportal/success.jsp"
        ):
            driver.quit()
            return "已经登录"
        else:
            print("跳转到了其他页面")
            driver.quit()
            exit()

    wait = WebDriverWait(driver, 10)  # 等待10秒

    try:
        username = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[2]/table/tbody/tr[2]/td[2]/div/div/div[1]/div[1]/div[1]/input",
                )
            )
        )
        username.send_keys(user["username"])

        # 添加延迟
        time.sleep(2)

        # 找到需要点击的密码框
        pwd_tip = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[2]/table/tbody/tr[2]/td[2]/div/div/div[3]/div[1]/input[2]",
                )
            )
        )

        # 创建一个ActionChains对象
        actions = ActionChains(driver)

        # 移动到元素上然后点击
        actions.move_to_element(pwd_tip).click().perform()
        # 输入密码
        password = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[2]/table/tbody/tr[2]/td[2]/div/div/div[3]/div[1]/div[1]/input",
                )
            )
        )
        password.send_keys(user["password"])

        try:
            login_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/div[2]/table/tbody/tr[2]/td[2]/div/div/div[16]/div/div/ol/li/a",
                    )
                )
            )
            login_button.click()  # 点击登录按钮
        except:
            print("login_button error")

    except TimeoutException:
        print("Timeout waiting for page to load")

    # 检测是否登录成功,如果登录成功,则会跳转到http://172.18.18.61:8080/eportal/success.jsp....后面省略,不同情况下后面的内容不同

    # 等待
    time.sleep(5)
    if driver.current_url.startswith("http://172.18.18.61:8080/eportal/success.jsp"):
        driver.quit()
        return "登录成功"
    else:
        driver.quit()
        return "登录失败"
