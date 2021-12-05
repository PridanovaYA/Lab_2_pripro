import tqdm
import re


"""класс для проверки данных на валидность записи"""
#        "telephone": "+7-(918)-043-20-33",
#        "height": "1.76",
#       "inn": "920207713870",
#        "passport_number": 123166,
#        "university": "Санкт-Петербургский государственный архитектурно-строительный университет",
#        "age": 63,
#        "academic_degree": "Магистр",
#        "worldview": "Пантеизм",
#        "address": "Аллея Прудовой 766"
class Valid:

    val: list

    def __init__(self, array) -> None:
        self.val = array

    """функция проверяет и записывает данные в словарь"""
    def check_valid(self, index)-> dict:
        result = {"telephone": self.val[index].check_telephone(),"height":self.check_height(),
        "inn":self.val[index].check_inn(),"passport_number":self.val[index].check_passport_number(),
        "university":self.val[index].check_university(),"age":self.val[index].check_age(),
        "academic_degree":self.val[index].check_academic_degree(),"worldview":self.val[index].check_worldview(),
        "address":self.val[index].check_adress()}

        return result.copy()

    def count_correct_records(self):
        count_correct = 0


        return count_correct

    def count_incorrect_records(self):
        count_incorrect = 0

        return count_incorrect




