## chatgpt를 이용한 IMAP 코드 생성하기(무료버전 가능)

4o 버전 ==> https://github.com/marketplace/models/azure-openai/gpt-4o-mini/playground

1. 파일첨부를 해줘. 파일첨부는 엑셀 파일만 해줘.
2. 받는 사람 형식을 formataddr()로 이름과 메일주소로 만들어줘.

<pre>
<code>
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
from email.header import Header
import os

# SMTP 서버 정보
SMTP_SERVER = "smtp.example.com"  # SMTP 서버 주소 (예: Gmail은 "smtp.gmail.com")
SMTP_PORT = 587                   # SMTP 포트 번호 (일반적으로 587)
SMTP_USER = "your_email@example.com"  # 발신자 이메일 주소
SMTP_PASSWORD = "your_password"      # 발신자 이메일 비밀번호

# 함수: 이메일 전송
def send_email_with_attachment(subject, body, to_name, to_email, file_path):
    """
    이메일을 보내는 함수 (엑셀 파일 첨부 포함)
    :param subject: 이메일 제목
    :param body: 이메일 본문
    :param to_name: 받는 사람 이름
    :param to_email: 받는 사람 이메일 주소
    :param file_path: 첨부 파일 경로 (엑셀 파일만 가능)
    """
    try:
        # 받는 사람 형식을 "이름 <이메일>"로 설정
        to_addr = formataddr((Header(to_name, 'utf-8').encode(), to_email))
        
        # 이메일 메시지 객체 생성 (멀티파트 사용)
        message = MIMEMultipart()
        message["From"] = formataddr((Header("Your Name", "utf-8").encode(), SMTP_USER))  # 발신자 정보
        message["To"] = to_addr  # 수신자 정보
        message["Subject"] = subject  # 이메일 제목

        # 이메일 본문 추가
        message.attach(MIMEText(body, "plain", "utf-8"))  # 본문은 일반 텍스트로 추가

        # 첨부 파일 추가 (엑셀 파일만 첨부)
        if file_path.endswith((".xls", ".xlsx")) and os.path.isfile(file_path):  # 파일이 엑셀 형식이고 존재하는 경우
            with open(file_path, "rb") as file:  # 파일 읽기
                part = MIMEBase("application", "octet-stream")  # 첨부 파일 MIME 타입 설정
                part.set_payload(file.read())  # 파일 내용을 MIME에 추가
                encoders.encode_base64(part)  # 파일 내용을 Base64로 인코딩
                part.add_header(
                    "Content-Disposition",
                    f'attachment; filename="{os.path.basename(file_path)}"'  # 첨부 파일 헤더 설정
                )
                message.attach(part)  # 이메일 메시지에 첨부 파일 추가

        # SMTP 서버 연결 및 이메일 전송
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # TLS 보안 연결 시작
            server.login(SMTP_USER, SMTP_PASSWORD)  # SMTP 서버 로그인
            server.sendmail(SMTP_USER, to_email, message.as_string())  # 이메일 전송
        
        print("이메일 전송 성공!")  # 성공 메시지 출력

    except Exception as e:
        print(f"이메일 전송 실패: {e}")  # 오류 발생 시 실패 메시지 출력

# 예제 사용
subject = "엑셀 파일 첨부 테스트"  # 이메일 제목
body = "첨부된 엑셀 파일을 확인해주세요."  # 이메일 본문
to_name = "Recipient Name"  # 수신자 이름
to_email = "recipient@example.com"  # 수신자 이메일 주소
file_path = "example.xlsx"  # 첨부할 엑셀 파일 경로

send_email_with_attachment(subject, body, to_name, to_email, file_path)  # 함수 호출
</code>
</pre>
