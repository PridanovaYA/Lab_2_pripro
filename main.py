import argparse

from Reader import Reader
from Valid import Valid


filename = "16.txt"
file_path = "D://Lab_2_pripro/16.txt"

parser = argparse.ArgumentParser("Input/Output parser")
parser.add_argument("-input", type=str, default="16.txt", help="Input path")
parser.add_argument("-output", type=str, default="res.txt", help="Output path")
par = parser.parse_args()

f = Reader(par.input)
print(f)

