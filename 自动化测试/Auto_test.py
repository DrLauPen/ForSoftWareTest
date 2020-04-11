"""软件测试,选择对百度进行测试."""
import time
from time import sleep

from selenium import webdriver
import warnings

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="/Users/XYJ/Downloads/软件测试下载/自动化测试/chromedriver")

    # 输入对应的搜索内容,并搜索
    driver.get("https://www.bilibili.com/")
    driver.find_element_by_class_name("nav-search-keyword").send_keys("原来是笑傲菌殿下")
    driver.find_element_by_class_name("nav-search-btn").click()

    driver.switch_to.window(driver.window_handles[-1])  # 跳转到搜索界面，否则会找不到.
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[8]/a').click()
    time.sleep(1)  # 延长时间确保能捕捉到.
    sreach_window = driver.current_window_handle
    driver.find_element_by_link_text("刺客信条cg").click()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])  # 跳转到搜索界面，否则会找不到.
    video = WebDriverWait(driver, 30, 0.5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[9]/video')))
    #采用Web的等待机制，每隔0.5s查看一次,如果满足则执行下一步.
    driver.execute_script("return arguments[0].play()", video)  # 开始播放

    # 关闭浏览器
    # driver.close()
