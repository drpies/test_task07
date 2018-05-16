# я немного изменил пример класса, т.к. не совсем понял от чего отталкиваться
import random

class Calendar:
    #  такие диапазоны я задал, что бы повысить процент выдачи невалидных дат
    # return day e.g. 31
    def get_day():
        return random.randrange(0, 40)
    # return month e.g. 3
    def get_month():
        return random.randrange(0, 15)
    # return year e.g. 1989
    def get_year():
        return 1960 + random.randrange(0, 50)
