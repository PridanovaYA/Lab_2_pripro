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
    dictionary: dict

    def __init__(self, array,a) -> None:

        self.dictionary = a.copy()
        self.val = array

    def check_telephone(self)-> bool:
        """для проверки номера телефона"""
        pat = "\\+(7)\\-\\(\\d{3}\\)\\-\\d{3}\\-\\d{2}\\-\\d{2}$"
        if re.math(pat, self.dictionary["telephone"]):
            return True
        return False

    def check_height(self) -> bool:
        """для проверки роста"""
        if 1.00 < self.dictionary["height"] < 2.50:
            return True
        return False

    def check_inn(self) -> bool:
        """для проверки инн"""
        pat = "^//d{12}"
        if re.math(pat, self.dictionary["inn"]):
            return True
        return False

    def check_passport_number(self) -> bool:
        """для проверки номера паспорта"""
        pat = "^//d{6}"
        if re.math(pat, self.dictionary["passport_number"]):
            return True
        return False

    def check_university(self) -> bool:
        """для проверки наименования университета"""
        pat = "^.*([Уу]ниверситет|[Аа]кадеми[яи]|[Пп]олитехнический|[И|и]нститут|им.|[А-Я]{3,}|РФ|СП[Бб]ГУ|[Пп]олитех|[Ии]сследовательск[А-Я]{2}.*$)"
        if re.math(pat, self.dictionary["university"]):
            return True
        return False

    def check_age(self) -> bool:
        """для проверки возраста"""
        if 0 <= self.dictionary["age"] < 120:
            return True
        return False

    def check_academic_degree(self) -> bool:
        pat = "Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук"
        if re.math(pat, self.dictionary["academic_degree"]):
            return True
        return False

    def check_worldview(self)-> bool:
        """для вероисповедания"""
        pat = ""
        if re.math(pat, self.dictionary["worldview"]):
            return True
        return False

    def check_address(self)-> bool:
        """для адреса проживания"""
        pat = ""
        if re.math(pat, self.dictionary["address"]):
            return True
        return False

    def check_valid(self):
        result = {}


        return result

    def count_correct_records(self):
        count_correct = 0


        return count_correct

    def count_incorrect_records(self):
        count_incorrect = 0

        return count_incorrect




