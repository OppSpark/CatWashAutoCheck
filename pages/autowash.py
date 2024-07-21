from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def autowash_login_and_check_in(autoWashID, autoWashPW):
    # 기본 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1900, 1000)

    autoWash_URl = 'https://autowash.co.kr/member/login.html?noMemberOrder&returnUrl=%2Fmyshop%2Findex.html'

    # 오토워시 접속
    driver.implicitly_wait(time_to_wait=2)
    driver.get(url=autoWash_URl)

    # 오토워시 로그인
    userId = driver.find_element(By.ID, 'member_id')
    userId.send_keys(autoWashID)
    userPwd = driver.find_element(By.ID, "member_passwd")
    userPwd.send_keys(autoWashPW)
    userPwd.send_keys(Keys.ENTER)

    # 출석체크 페이지로 이동
    driver.implicitly_wait(time_to_wait=2)
    driver.find_element(By.CSS_SELECTOR, 'div.fold-icon').click()
    driver.implicitly_wait(time_to_wait=1)
    driver.find_element(By.CSS_SELECTOR, 'a.attendBanner').click()

    # 출석체크 버튼 누르기
    driver.implicitly_wait(time_to_wait=2)
    driver.find_element(By.CSS_SELECTOR, 'a.btnSubmitFix').click()

    return driver
