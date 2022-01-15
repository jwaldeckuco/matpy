
import enum
from fractions import Fraction
import copy

class Row:
    def __init__(self, inputString=""):
        self.row = []
        if not inputString == "":
            self.parse(inputString)

    def parse(self, inputString):
        tempRow = []

        # split inputString on ","
        tempRowStrings = inputString.split(",")
        # result: a list of string values

        for value in tempRowStrings:
            tempRow.append(int(value))
        
        self.row = tempRow

    # element access
    def getColValue(self, index):
        return self.row[index]
    
    # row operations
    def scale(self, scalar):
        self.row = self.getScaledList(scalar)

    def getScaledList(self, scalar):
        temp = []

        for value in self.row:
            if type(scalar) != int:
                tempValue = Fraction(value) * scalar

                if type(tempValue) == Fraction and tempValue.denominator == 1:
                    tempValue = int(tempValue)
                elif type(tempValue) == Fraction and tempValue.numerator == 0:
                    tempValue = 0
            else:
                tempValue = value * scalar
            temp.append(tempValue)

        return copy.deepcopy(temp)

    def getScaledCopy(self, scalar=1):
        temp = Row()
        temp.row = self.getScaledList(scalar)
        return temp

    def add(self, sourceRow):
         for i in range(len(self.row)):
            self.row[i] += sourceRow.getColValue(i)

    def subtract(self, sourceRow):
        for i in range(len(self.row)):
            self.row[i] -= sourceRow.getColValue(i)
    
    def getFormattedString(self):
        rowString = ""

        for i in range(len(self.row)):
            if type(self.row[i]) == float:
                rowString += '{: >10f}'.format((self.row[i]))
                
            elif type(self.row[i]) == Fraction:
                num = self.row[i].numerator
                den = self.row[i].denominator

                rowString += '{: >10}'.format(str(num) + "/" + str(den))

            else:
                rowString += '{: >10}'.format(int(self.row[i]))

            if i < len(self.row) - 1:
                rowString = rowString + ","  
        return rowString

    # properties type stuff
    def getLength(self):
        return len(self.row)