class Athlete(object):
    INCH_TO_CM_CENVERSION_VALUE = 2.54

    def __init__(self, name: str, age: int, height: float, weight: float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.age}, {self.height}, {self.weight}"

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.height}, {self.weight}"

    def convert_inch_to_cm(height_in_inch):
        return height_in_inch * Athlete.INCH_TO_CM_CENVERSION_VALUE

