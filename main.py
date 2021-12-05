import argparse
from tqdm import tqdm
from Reader import Reader

from Valid import Valid
#filename = "16.txt"
#file_path = "D://Lab_2_pripro/16.txt"
from Writer import Writer

parser = argparse.ArgumentParser("Input/Output parser")
parser.add_argument("-input", type=str, default="16.txt", help="Input path")
parser.add_argument("-output", type=str, default="res.txt", help="Output path")
par = parser.parse_args()

f = Reader(par.input)
array = Valid(f.read_file())
v = array.count_correct_records()
inv = array.count_incorrect_records()
res = array.count_errors_in_dict()
writer = Writer(par.output)
writer.file_writer(array)

print("Валидные записи:",v)
print("Невилидные записи:",inv)
print("Ошибка в номере телефона:", res[0])
print("Рост", res[1])
print("ИНН", res[2])
print("Номер паспорта", res[3])
print("Университет", res[4])
print("Возраст", res[5])
print("Степень", res[6])
print("Вероисповедание", res[7])
print("Адрес", res[8])
