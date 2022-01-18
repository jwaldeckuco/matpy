from fractions import Fraction

class Cell:
    def __init__(self, value):
        if type(value) == str:
            self.parse(value)
        else:
            self.value = value

    def parse(self, valueString):
        # if a fraction is supplied
        if "/" in valueString:
            self.value = Fraction(valueString)
        else:
            try:
                self.value = int(valueString)
            except(ValueError):
                self.value = float(valueString)

    def getScaledCopy(self, scalar):
        temp = self.value * scalar

        if type(temp) == float and temp.is_integer():
            temp = int(temp)
        elif type(temp) == Fraction:
            if temp.numerator == 0:
                temp = 0
            elif temp.denominator == 1:
                temp = int(temp)

        return Cell(temp)

    def add(self, addend):
        self.value += addend

    def subtract(self, minuend):
        self.value -= minuend

    def getFormattedString(self):
        if type(self.value) == float:
            return '{: >8.3f}'.format(self.value)

        elif type(self.value) == Fraction:
            num = self.value.numerator
            den = self.value.denominator
            return '{: >8}'.format(str(num) + "/" + str(den))
        
        else:
            return '{: >8}'.format(self.value)