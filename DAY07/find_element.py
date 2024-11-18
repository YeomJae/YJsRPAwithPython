from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriver 초기화
driver = webdriver.Chrome()

# HTML 파일 로드
driver.get("C:\IACFPYTHON\example.html") 

# 각 방법으로 요소 찾기
try:
    # ID
    element_by_id = driver.find_element(By.ID, "unique-id")
    print("ID:", element_by_id.text)

    # NAME
    element_by_name = driver.find_element(By.NAME, "username")
    print("NAME:", element_by_name.get_attribute("value"))

    # XPATH
    element_by_xpath = driver.find_element(By.XPATH, "//p[text()='XPath Example']")
    print("XPATH:", element_by_xpath.text)

    # LINK_TEXT
    element_by_link_text = driver.find_element(By.LINK_TEXT, "Click Me")
    print("LINK_TEXT:", element_by_link_text.text)

    # PARTIAL_LINK_TEXT
    element_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "About")
    print("PARTIAL_LINK_TEXT:", element_by_partial_link_text.text)

    # TAG_NAME
    element_by_tag_name = driver.find_element(By.TAG_NAME, "h1")
    print("TAG_NAME:", element_by_tag_name.text)

    # CLASS_NAME
    element_by_class_name = driver.find_element(By.CLASS_NAME, "sample-class")
    print("CLASS_NAME:", element_by_class_name.text)

    # CSS_SELECTOR
    element_by_css_selector = driver.find_element(By.CSS_SELECTOR, ".css-selector-example")
    print("CSS_SELECTOR:", element_by_css_selector.text)

finally:
    # WebDriver 종료
    driver.quit()
