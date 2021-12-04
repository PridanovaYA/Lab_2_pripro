import json

class Reader:
    def __init__(self, file_path) -> None:
        self.path = file_path
    def read_file(self)-> list:
        array: list = []
        data = json.load(open(self.path, encoding='windows-1251'))
        for i in data:
            array.append(i.copy())
        return array
