from tqdm import tqdm
import re
from check import Check

class Valid:
    """класс для проверки данных на валидность записи"""
    val: list

    def __init__(self, array) -> None:
        self.val = array

    def check_valid(self, index) -> dict:
        """функция проверяет и записывает данные в словарь"""
        result = {"telephone": self.val[index].check_telephone(),
                "height":self.val[index].check_height(),
                "inn":self.val[index].check_inn(),
                "passport_number":self.val[index].check_passport_number(),
                "university":self.val[index].check_university(),
                "age":self.val[index].check_age(),
                "academic_degree": self.val[index].check_academic_degree(),
                "worldview":self.val[index].check_worldview(),
                "address":self.val[index].check_adress()}

        return result.copy()

    def count_correct_records(self) -> int:
        """функция проверяет массив на количество корректных записей(возвращает количество)"""

        count_correct = 0
        for i in tqdm(range(len(self.val)), desc="Подождите. Идет подсчет корректных записей", ncols=100):
            if not (False in self.check_valid(i).values()):
                count_correct += 1
        return count_correct

    def count_incorrect_records(self) -> int:
        """функция проверяет массив на общее количество некорректных записей(возвращает количество)"""

        count_incorrect = 0
        for i in tqdm(range(len(self.val)), desc="Подождите. Идет подсчет некорректных записей", ncols=100):
            if (False in self.check_valid(i).values()):
                count_incorrect += 1
        return count_incorrect

    def count_errors_in_dict(self):
        """функция находит число невалидных записей по типам ошибок и возвращает их количество"""
        res = []

        count_err_telephone = 0
        count_err_height = 0
        count_err_inn = 0
        count_err_passport_number = 0
        count_err_university = 0
        count_err_age = 0
        count_err_academic_degree = 0
        count_err_worldview = 0
        count_err_address = 0

        for i in tqdm(range(len(self.val)), desc="Подождите. Идет подсчет некорректных по типам ошибок записей", ncols=100):
            if not self.val[i].check_telephone():
                count_err_telephone += 1

            if not self.val[i].check_height():
                count_err_height += 1

            if not self.val[i].check_inn():
                count_err_inn += 1

            if not self.val[i].check_passport_number():
                count_err_passport_number += 1

            if not self.val[i].check_university():
                count_err_university += 1

            if not self.val[i].check_age():
                count_err_age += 1

            if not self.val[i].check_academic_degree():
                count_err_academic_degree += 1

            if not self.val[i].check_worldview():
                count_err_worldview += 1

            if not self.val[i].check_adress():
                count_err_address += 1

        res.append(count_err_telephone)
        res.append(count_err_height)
        res.append(count_err_inn)
        res.append(count_err_passport_number)
        res.append(count_err_university)
        res.append(count_err_age)
        res.append(count_err_academic_degree)
        res.append(count_err_worldview)
        res.append(count_err_address)
        return res





