import re

# 대상 텍스트 리스트
texts = [
    "(2세부) aaaaaaaaaaaaaaaaaaa (1차년도)",
    "(2세부) aaaaaaaaaaaaaaaaaaa (2차년도)",
    "(2세부) aaaaaaaaaaaaaaaaaaa (3차년도)",
    "[aaaa] aaaaaaaaaaaaaaaaaaa (2단계-5차년도)"
]

# 정규식 패턴
pattern = r"\d+차년도\)"

# 텍스트에서 패턴 제거
cleaned_texts = [re.sub(pattern, "", text) for text in texts]

# 결과 출력
print(cleaned_texts[0])
print(cleaned_texts[1])
print(cleaned_texts[2])
print(cleaned_texts[3])
"""
(2세부) aaaaaaaaaaaaaaaaaaa (
(2세부) aaaaaaaaaaaaaaaaaaa (
(2세부) aaaaaaaaaaaaaaaaaaa (
[aaaa] aaaaaaaaaaaaaaaaaaa (2단계-
"""
print("==================================================")
processed_texts = []
for text in cleaned_texts:
    if text.endswith("("):  # 마지막 글자가 "("인 경우
        processed_texts.append(text[:-1])  # "(" 삭제
    elif text.endswith("-"):  # 마지막 글자가 "-"인 경우
        processed_texts.append(text[:-1] + ")")  # "-"를 ")"로 대체
    else:
        processed_texts.append(text)  # 변경하지 않음

# 결과 출력
print(processed_texts[0])
print(processed_texts[1])
print(processed_texts[2])
print(processed_texts[3])

"""
(2세부) aaaaaaaaaaaaaaaaaaa
(2세부) aaaaaaaaaaaaaaaaaaa
(2세부) aaaaaaaaaaaaaaaaaaa
[aaaa] aaaaaaaaaaaaaaaaaaa (2단계)
"""
