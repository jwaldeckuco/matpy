
from fractions import Fraction
import copy
from matrix import cell

class Row:
    def __init__(self, inputString=""):
        self.row = []
        # TODO: update to exception handling
        if not inputString == "":
            self.parse(inputString)

    def parse(self, inputString):
        tempRow = []

        # split inputString on ","
        tempRowStrings = inputString.split(",")
        # result: a list of string values

        for value in tempRowStrings:
            tempRow.append(cell.Cell(value))
        
        self.row = tempRow

    # element access
    def getColValue(self, index):
        return self.row[index].value
    
    # row operations
    def scale(self, scalar):
        self.row = self.getScaledList(scalar)

    def getScaledList(self, scalar):
        temp = []

        for value in self.row:
            temp.append(value.getScaledCopy(scalar))
        
        return copy.deepcopy(temp)

    def getScaledCopy(self, scalar=1):
        temp = Row()
        temp.row = self.getScaledList(scalar)
        return temp

    def add(self, sourceRow):
         for i in range(len(self.row)):
            self.row[i].add(sourceRow.getColValue(i))

    def subtract(self, sourceRow):
        for i in range(len(self.row)):
            self.row[i].subtract(sourceRow.getColValue(i))
    
    def getFormattedString(self):
        rowString = ""

        for i in range(len(self.row)):
            rowString += self.row[i].getFormattedString()

            if i < len(self.row) - 1:
                rowString = rowString + ","  
        return rowString

    # properties type stuff
    def getLength(self):
        return len(self.row)