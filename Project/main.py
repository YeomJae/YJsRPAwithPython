import util as ut
import os
import xlsxProcess as xlp

directory = ut.exedir('py')
directory_workF = ut.exedir('py')+"\\workF"
directory_resultF = directory_workF.replace("workF","resultF")

"""
filename = "20241016_89900100056880_154004"
xlp.toExcelErp(directory_workF, filename)

search_item = filename.split('_')[1]
worker = xlp.get_worker(directory, search_item)
print(worker) #  {"Name" : "홍길동", "Email" : "hong@abcd.co.kr"}
"""

file_list = os.listdir(directory_workF)
file_list = [file for file in file_list if "거래처원장" not in file]
for file_name in file_list:
    if file_name.endswith(('.xls', '.xlsx')):
        search_item = file_name.split('_')[1]
        worker = xlp.get_worker(directory, search_item)
        print(worker) #  {"Name" : "홍길동", "Email" : "hong@abcd.co.kr"}
        xlp.toExcelErp(directory_workF, file_name)
        wep.sendMail(directory_resultF,worker) #DAY07 구현단계
