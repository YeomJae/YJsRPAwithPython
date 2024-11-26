import pyautogui
import time

def simulate_click_and_trigger():
    """pyautogui 클릭과 이벤트 실행"""
    # 마우스를 특정 위치로 이동
    pyautogui.moveTo(500, 500, duration=0.5)
    print("마우스를 이동했습니다.")

    # 클릭 시뮬레이션
    pyautogui.click()

    # 클릭에 대한 추가 작업 함수 호출
    on_click_event()

def file_downlond() :
    print("여기에서 파일 다운로드 함수가 실행됩니다.")

def on_click_event():
    print("클릭 이벤트 발생!")
    """클릭 시 실행되는 함수"""
    file_downlond()
    print("클릭 이벤트 처리가 완료되었습니다.")

# 2초 대기 후 시뮬레이션 실행
time.sleep(2)
simulate_click_and_trigger()
