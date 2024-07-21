from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def autowax_login_and_check_in(autoWaxID, autoWaxPW):
    # 기본 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1900, 1000)

    autoWax_URL = 'https://m.autowax.co.kr/member/login.php'

    # 오토왁스 접속
    driver.implicitly_wait(time_to_wait=2)
    driver.get(url=autoWax_URL)

    # 오토왁스 로그인
    userId = driver.find_element(By.ID, 'loginId')
    userId.send_keys(autoWaxID)
    userPwd = driver.find_element(By.ID, "loginPwd")
    userPwd.send_keys(autoWaxPW)
    userPwd.send_keys(Keys.ENTER)

    # 오토왁스 출석체크 페이지로 이동
    driver.implicitly_wait(time_to_wait=2)
    driver.get('https://m.autowax.co.kr/event/attend_stamp.php?sno=3')

    # 명시적 대기 (세션 로딩 대기)
    time.sleep(2)

    # 오토왁스 출석체크 버튼 누르기
    driver.implicitly_wait(time_to_wait=2)
    driver.find_element(By.ID, 'attendanceCheck').click()
    time.sleep(1)

    # alert 나오면 엔터 누르기
    driver.switch_to.alert.accept()

    return driver
