import smtplib

def test_smtp_connection(smtp_server, smtp_port, username, password):
    try:
        # SMTP 서버 연결
        print(f"Connecting to SMTP server: {smtp_server}:{smtp_port}")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # 서버 초기화
        server.starttls()  # TLS 시작
        print("Starting TLS...")

        # 로그인 시도
        print("Attempting login...")
        server.login(username, password)
        print("SMTP connection successful!")

        # 연결 종료
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your username and password.")
    except smtplib.SMTPConnectError:
        print("SMTP Connection Error: Unable to connect to the server.")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
test_smtp_connection(
    smtp_server="smtp메일주소",  # SMTP 서버 주소
    smtp_port=포트,
    username="메일아이디",
    password="메일비번"
)
