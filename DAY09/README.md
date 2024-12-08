## chatgpt를 이용한 IMAP 코드 생성하기(무료버전 가능)

4o 버전 ==> https://github.com/marketplace/models/azure-openai/gpt-4o-mini/playground

1. imap을 위한 예제 코드를 만들어줘
2. 최근 2일간의 메일만 검색되게 해줘
3. 검색된 메일에서 제목에 특정 키워드인 "python"이 들어간 메일 제목만 골라서 해당 메일의 첨부문서만 다운로드 되게 해줘

<pre>
<code>
import imaplib
import email
from email.header import decode_header
from datetime import datetime, timedelta

# 기본 설정
IMAP_SERVER = "imap.example.com"
USERNAME = "your_username"
PASSWORD = "your_password"
DOWNLOADF = "path_to_download_directory"
SEARCHDAYS = 2

def search_mail_and_download_attachment(search_string):
    while True:
        try:
            # IMAP 서버 연결
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(USERNAME, PASSWORD)
            mail.select("inbox")
            
            # 최근 2일 이내 이메일 검색
            since_date = (datetime.now() - timedelta(days=SEARCHDAYS)).strftime("%d-%b-%Y")
            result, data = mail.search(None, f'SINCE {since_date}')
            
            if result == "OK":
                email_ids = data[0].split()
                if not email_ids:
                    print("No emails found.")
                
                # 각 이메일 처리
                for email_id in email_ids:
                    result, msg_data = mail.fetch(email_id, "(RFC822)")
                    msg = email.message_from_bytes(msg_data[0][1])

                    # 제목 디코딩
                    subject, encoding = decode_header(msg['Subject'])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else 'utf-8')
                    
                    # 받은 날짜 추출
                    date = msg["Date"]
                    received_date = email.utils.parsedate_to_datetime(date)

                    # 보낸 사람 추출
                    from_ = msg.get("From")

                    # 이메일 정보 출력
                    print(f"Received Date: {received_date}")
                    print(f"From: {from_}")
                    print(f"Subject: {subject}")

                    # 제목에 특정 검색어가 들어가 있는지
                    if search_string in subject:
                        print(f"Found matching email: {subject}")
                        download_attachment(msg, DOWNLOADF)  # 첨부파일 다운로드 함수 호출
            else:
                print("Search failed:", result)

            # 로그아웃
            mail.logout()

        except imaplib.IMAP4.abort as e:
            print(f"Connection error: {e}, retrying...")
            break  # 연결 오류 시 종료
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # 기타 오류 시 종료
        finally:
            try:
                if 'mail' in locals() and mail.state != 'LOGOUT':  # 로그아웃 상태 확인
                    mail.logout()
            except Exception as logout_error:
                print(f"Logout error: {logout_error}")
                break

  search_mail_and_download_attachment("파이썬"):
</code>
</pre>
