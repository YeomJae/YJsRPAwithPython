import olefile

f = olefile.OleFileIO('경로\\temp_1733235551871.-1363003576.hwp')

encoded_text = f.openstream('PrvText').read() #PrvText 스트림 안의 내용 꺼내기 (유니코드 인코딩 되어 있음)

decoded_text = encoded_text.decode('UTF-16') #유니코드이므로 UTF-16으로 디코딩
decoded_text = decoded_text.split("><")

# print(decoded_text)

# 분할된 값을 for 문으로 출력 (인덱스 포함)
index_value_dict = {}
for index, value in enumerate(decoded_text):
    print(f"Index {index}: {value}")
    #if index in [72, 73]:
        #index_value_dict[index] = value.strip("<>")

# 딕셔너리 출력
# print(index_value_dict)
