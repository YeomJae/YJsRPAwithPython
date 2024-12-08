import smtplib  # SMTP 통신을 위한 모듈

def test_smtp_connection(smtp_server, smtp_port, username, password):
    """
    SMTP 서버 연결 테스트 함수
    :param smtp_server: SMTP 서버 주소 (예: smtp.gmail.com)
    :param smtp_port: SMTP 포트 번호 (예: 587)
    :param username: 이메일 계정 사용자 이름
    :param password: 이메일 계정 비밀번호
    """
    try:
        # SMTP 서버 연결 시도
        print(f"Connecting to SMTP server: {smtp_server}:{smtp_port}")
        server = smtplib.SMTP(smtp_server, smtp_port)  # 서버 및 포트 설정
        server.ehlo()  # 서버 초기화 및 확인
        server.starttls()  # TLS 암호화 시작
        print("Starting TLS...")

        # 로그인 시도
        print("Attempting login...")
        server.login(username, password)  # 사용자 계정으로 로그인
        print("SMTP connection successful!")  # 성공 메시지 출력

        # 연결 종료
        server.quit()  # 서버와의 연결 종료
    except smtplib.SMTPAuthenticationError:
        # 인증 실패 (아이디/비밀번호 오류)
        print("SMTP Authentication Error: Check your username and password.")
    except smtplib.SMTPConnectError:
        # 서버 연결 오류
        print("SMTP Connection Error: Unable to connect to the server.")
    except smtplib.SMTPException as e:
        # SMTP 관련 기타 예외 처리
        print(f"SMTP Error: {e}")
    except Exception as e:
        # 일반적인 예외 처리
        print(f"An error occurred: {e}")

# Example usage
test_smtp_connection(
    smtp_server="smtp메일주소",  # SMTP 서버 주소 입력 (예: smtp.gmail.com)
    smtp_port=포트,  # 포트 번호 입력 (예: 587)
    username="메일아이디",  # 이메일 계정 사용자 이름
    password="메일비번"  # 이메일 계정 비밀번호
)
