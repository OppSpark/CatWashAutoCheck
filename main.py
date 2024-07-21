from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# ID PW 정보 열기 config.txt
config_file_path = 'config.txt'
with open(config_file_path, 'r') as file:
    lines = file.readlines()

# 오토왁스 ID PW
autoWaxID = None
autoWaxPW = None

for line in lines:
    if 'autoWaxID' in line:
        autoWaxID = line.split('=')[1].strip()
    elif 'autoWaxPW' in line:
        autoWaxPW = line.split('=')[1].strip()

#

# 오토워시 ID, PW
autoWashID = None
autoWashPW = None

for line in lines:
    if 'autoWashID' in line:
        autoWashID = line.split('=')[1].strip()
    elif 'autoWashPW' in line:
        autoWashPW = line.split('=')[1].strip()

# 기본 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1900, 1000)

autoWash_URl = 'https://autowash.co.kr/member/login.html?noMemberOrder&returnUrl=%2Fmyshop%2Findex.html'
autoWax_URL = 'https://m.autowax.co.kr/member/login.php'


# 오토왁스

# 오토왁스 접속
driver.implicitly_wait(time_to_wait=2)
driver.get(url=autoWax_URL)

# 오토왁스 로그인
userId = driver.find_element(By.ID, 'loginId')
userId.send_keys(autoWashID)
userPwd = driver.find_element(By.ID, "loginPwd")
userPwd.send_keys(autoWaxPW)
userPwd.send_keys(Keys.ENTER)

# 오토왁스 출석체크 페이지로 이동
driver.implicitly_wait(time_to_wait=2)
driver.get('https://m.autowax.co.kr/event/attend_stamp.php?sno=3')

# 명시적 대기 (세션 로딩 대기)
time.sleep(3)

## 오토왁스 출석체크 버튼 누르기
driver.implicitly_wait(time_to_wait=2)
driver.find_element(By.ID, 'attendanceCheck').click()
time.sleep(1)

# alert 나오면 엔터 누르기
driver.switch_to.alert.accept()

# 오토워시
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

## 출석체크 버튼 누르기
driver.implicitly_wait(time_to_wait=2)
driver.find_element(By.CSS_SELECTOR, 'a.btnSubmitFix').click()




