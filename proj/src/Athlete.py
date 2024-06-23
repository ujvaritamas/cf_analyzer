
#to count ranking
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class RankCounter():
    def __init__(self):
        self.rank = 1

    def increment(self):
        self.rank+=1

    def get_rank(self):
        rank = self.rank
        self.increment()
        return rank

class Athlete(object):
    INCH_TO_CM_CENVERSION_VALUE = 2.54

    def __init__(self, name: str, age: int, height: float, weight: float, year:int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.rank = self.get_rank()
        self.year = year

    @staticmethod
    def get_header():
        return ['name', 'age', 'height (cm)', 'wight (kg), rank, year']

    def get_rank(self) ->int:
        return RankCounter().get_rank()

    def __str__(self):
        return f"{self.name}, {self.age}, {self.height}, {self.weight}, {self.rank}, {self.year}"

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.height}, {self.weight}, {self.rank}, {self.year}"

    def list_csv(self):
        return [self.name, self.age, self.height, self.weight, self.rank, self.year]

    def convert_inch_to_cm(height_in_inch):
        return height_in_inch * Athlete.INCH_TO_CM_CENVERSION_VALUE

