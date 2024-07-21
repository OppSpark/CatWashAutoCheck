from pages.autowax import autowax_login_and_check_in
from pages.autowash import autowash_login_and_check_in

# ID PW 정보 열기 config.txt
config_file_path = 'config.txt'
with open(config_file_path, 'r') as file:
    lines = file.readlines()

# 오토왁스 ID PW
autoWaxID = None
autoWaxPW = None

# 오토워시 ID, PW
autoWashID = None
autoWashPW = None

for line in lines:
    if 'autoWaxID' in line:
        autoWaxID = line.split('=')[1].strip()
    elif 'autoWaxPW' in line:
        autoWaxPW = line.split('=')[1].strip()
    elif 'autoWashID' in line:
        autoWashID = line.split('=')[1].strip()
    elif 'autoWashPW' in line:
        autoWashPW = line.split('=')[1].strip()

# 오토왁스 로그인 및 출석체크
autowax_driver = autowax_login_and_check_in(autoWaxID, autoWaxPW)

# 오토워시 로그인 및 출석체크
autowash_driver = autowash_login_and_check_in(autoWashID, autoWashPW)
