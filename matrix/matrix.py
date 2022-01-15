
from fractions import Fraction
import copy
import fractions
import exception
from exception.exceptions import UnevenRowsError
from matrix import row


class Matrix:
    def __init__(self):
        self.matrix = []
        self.augmented = False

    def parse(self, inputString):
        # create a temp list to hold the rows
        temp = []

        # remove formatting characters
        # remove curly braces
        strippedString = inputString.lstrip("{").rstrip("}")
        # remove whitespace
        strippedString = strippedString.replace(" ", "")
        # result: "x11,x12,x13;x21,x22,x23;...xmn;

        # parse rows
        # creates rowStrings list by splitting inputString on ";"
        rowStrings = strippedString.split(";")
        # remove the empty list entry created. Need to fix this later
        rowStrings.pop(-1)

        # parse values
        for rowString in rowStrings:
            temp.append(row.Row(rowString))

        # if all rows are the same length continue
        for i in range(len(temp) - 1):
            if temp[i].getLength() != temp[i + 1].getLength():
                raise UnevenRowsError
        
        self.matrix = temp

    def setAugmented(self, augmented):
        self.augmented = augmented

    def interchange(self, row1, row2):
        if self.validateRowNumbers(row1, row2):
            return self.validateRowNumbers(row1, row2)

        tempRow = self.matrix[row1 - 1]
        self.matrix[row1 - 1] = self.matrix[row2 - 1]
        self.matrix[row2 - 1] = tempRow

    def additionRowOp(self, targetRow, sourceRow, scalar):
        if self.validateRowOpInputs(targetRow, sourceRow, scalar):
            return self.validateRowOpInputs(targetRow, sourceRow, scalar)

        self.performRowAddOrSubOp(targetRow, sourceRow, scalar, 1)

    def subtractionRowOp(self, targetRow, sourceRow, scalar):
        if self.validateRowOpInputs(targetRow, sourceRow, scalar):
            return self.validateRowOpInputs(targetRow, sourceRow, scalar)

        self.performRowAddOrSubOp(targetRow, sourceRow, scalar, -1)
        
    def performRowAddOrSubOp(self, targetRow, sourceRow, scalar, opType):
        scaledSource = self.matrix[sourceRow - 1].getScaledCopy(scalar)
        
        if opType == 1:
            self.matrix[targetRow - 1].add(scaledSource)
        else:
            self.matrix[targetRow - 1].subtract(scaledSource)
        
    def validateRowOpInputs(self, targetRow, sourceRow, scalar):
        if self.validateRowNumbers(targetRow, sourceRow):
            return self.validateRowNumbers(targetRow, sourceRow)
        
        if self.validateScalar(scalar):
            return self.validateScalar(scalar)

    def validateRowNumbers(self, targetRow, sourceRow):
        if self.validateRowNumber(targetRow):
            return "The first row does not exist in the matrix"
        if self.validateRowNumber(sourceRow):
            return "The second row does not exist in the matrix"

    def validateScalar(self, scalar):
        if not (scalar > 0 or scalar < 0) :
            return "Scalar can not be 0"

    def validateRowNumber(self, rowNumber):
        if rowNumber <= 0:
            return "Row number not valid"

        elif rowNumber > (len(self.matrix)):
            return "Row number not valid"

    def scale(self, row, scalar):
        # validate row number
        if self.validateRowNumber(row):
            return self.validateRowNumber(row)
        
        # validate scalar value
        if self.validateScalar(scalar):
            return self.validateScalar(scalar)

        # self.matrix[row - 1] = self.returnScaled(self.matrix[row - 1], scalar)
        self.matrix[row - 1].scale(scalar)

    def returnScaled(self, row, scalar):
        temp = []

        for value in row:
            if type(scalar) != int:
                tempValue = Fraction(value) * scalar
                if type(tempValue) == Fraction and tempValue.denominator == 1:
                    tempValue = int(tempValue)
                elif type(tempValue) == Fraction and tempValue.numerator == 0:
                    tempValue = 0
            else:
                tempValue = value * scalar

            temp.append(tempValue)
        return temp
        
    def deepCopy(self):
        return copy.deepcopy(self)

    def display(self):
        print(self.getStringRep())

    def getStringRep(self):
        if not self.augmented:
            columns = self.matrix[0].getLength()
        else:
            columns = self.matrix[0].getLength() - 1

        string = ""

        for i in range(columns):
            string += '{: >10}'.format("x" + str(i + 1))
        
        string += "\n"

        for i, row in enumerate(self.matrix):
            rowString = "r" + str(i + 1) + row.getFormattedString() + "\n"

            string += rowString
        return string