# 모든 iframe을 찾고, 올바른 iframe으로 전환
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
for i, iframe in enumerate(iframes):
    print(f"iframe {i}: {iframe.get_attribute('id')}, {iframe.get_attribute('name')}")

# 원하는 iframe으로 전환
driver.switch_to.frame(iframe)

# 다시 원래 프레임으로 돌아오기
driver.switch_to.default_content()
