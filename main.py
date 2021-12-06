import argparse
from tqdm import tqdm
from Reader import Reader
from Valid import Valid
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

print("Валидные записи:", v)
print("Невилидные записи:", inv)
print("Ошибка в номере телефона:", res[0])
print("Ошибка в росте", res[1])
print("Ошибка в ИНН", res[2])
print("Ошибка в номере паспорта", res[3])
print("Ошибка в наименовании университета", res[4])
print("Ошибка в возрасте", res[5])
print("Ошибка в степени", res[6])
print("Ошибка в вероисповедании", res[7])
print("Ошибка в адресе", res[8])
