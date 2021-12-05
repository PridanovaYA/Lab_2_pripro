import json
from tqdm import tqdm


class Writer:
    """класс для записа в файл"""
    def __init__(self, file_path) -> None:
        self.path = file_path

    def file_writer(self,array) -> None:
        temp = []
        for i in tqdm(range(len(array.val)), desc="Подождите. Идет запись результата в файл", ncols=100):
            if not (False in array.check_valid(i).values()):
                temp.append(array.val[i].dictionary.copy())
        json.dump(temp, open(self.path, 'w', encoding='windows-1251'), ensure_ascii=False, sort_keys=False, indent=4)
