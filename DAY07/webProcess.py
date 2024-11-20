from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import util as ut

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
# chrome_options.add_argument("headless")  # 헤드리스 모드 설정
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

output_file_path = logininfo["workF"]

chrome_options.add_experimental_option("prefs", {
"download.default_directory": output_file_path,  # 다운로드 폴더 지정
"download.prompt_for_download": False,  # 다운로드 시 사용자에게 묻지 않음
"download.directory_upgrade": True,
"safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://---")
driver.maximize_window()

mailid = driver.find_element(By.CSS_SELECTOR, "#mailid").send_keys(logininfo["ID"])
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(logininfo["PW"])

driver.close()
