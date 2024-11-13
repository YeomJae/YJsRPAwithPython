import util as ut
import xlsxProcess as xlp

directory = ut.exedir('py')
filename = "20241016_89900100056880_154004"
xlp.toExcelErp(directory, filename)

search_item = filename.split('_')[1]
worker = xlp.get_worker(directory, search_item)
print(worker) #  {"Name" : "홍길동", "Email" : "hong@abcd.co.kr"}
