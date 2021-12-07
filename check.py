import re


class Check:
    """ класс для проверки валидности написания"""

    dictionary: dict

    def __init__(self, a) -> None:
        self.dictionary = a.copy()

    def check_telephone(self) -> bool:
        """для проверки номера телефона"""
        pat = "\\+(7)\\-\\(\\d{3}\\)\\-\\d{3}\\-\\d{2}\\-\\d{2}$"
        if re.match(pat, self.dictionary["telephone"]):
            return True
        return False

    def check_height(self) -> bool:
        """для проверки роста"""
        pat = "^[0-2]+.+([0-8]{2})$"
        a = False
        if ((isinstance(self.dictionary["height"], (int, float)) == True)):
            if 0 < self.dictionary["height"] < 2.72:
                return True
        # print(self.dictionary["height"])
        if re.match(pat, str(self.dictionary["height"])):
            a = True
        if a:
            return True
        return False

    def check_inn(self) -> bool:
        """для проверки инн"""
        pat = "^\\d{12}"
        a = False
        if (isinstance(self.dictionary["inn"], int) == True) & (len(self.dictionary["inn"]) == 12):
            return True
        if re.match(pat, self.dictionary["inn"]):
            a = True
        if a:
            return True
        return False

    def check_passport_number(self) -> bool:
        """для проверки номера паспорта"""
        pat = "^\\d{6}"
        a = False
        if (isinstance(self.dictionary["passport_number"], int) == True) & (len(self.dictionary["inn"]) == 6):
            return True
        if re.match(pat, str(self.dictionary["passport_number"])):
            a = True
        if a:
            return True
        return False

    def check_university(self) -> bool:
        """для проверки наименования университета"""
        pat = "^.*([Уу]ниверситет|[Аа]кадеми[яи]|[Пп]олитехнический|[И|и]нститут|им.|[А-Я]{3,}|РФ|СП[Бб]ГУ|[Пп]олитех|[Ии]сследовательск[А-Я]{2}.*$)"
        if re.match(pat, self.dictionary["university"]):
            return True
        return False

    def check_age(self) -> bool:
        """для проверки возраста"""
        if isinstance(self.dictionary["age"], int):
            if 17 <= self.dictionary["age"] < 100:
                return True
        return False

    def check_academic_degree(self) -> bool:
        """для проверки академической степени"""
        pat = "Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук"
        if re.match(pat, self.dictionary["academic_degree"]):
            return True
        return False

    def check_worldview(self) -> bool:
        """для вероисповедания"""
        pat = "^.+(?:изм|нство)$"
        if re.match(pat, self.dictionary["worldview"]):
            return True
        return False

    def check_adress(self) -> bool:
        """для адреса проживания"""
        pat = "(?:ул\\.|Аллея) (?:им[\\.\\s]|)[^\\s]+[^\\s]*(?:\\s|)\\d+"
        if re.match(pat, self.dictionary["address"]):
            return True
        return False
