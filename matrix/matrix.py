
# from decimal import Decimal
from email import header
from fractions import Fraction
from wsgiref import headers


class Matrix:
    def __init__(self) -> None:
        self.matrix = []

    def parse(self, inputString):
        temp = []
        # remove brackets
        strippedString = inputString.lstrip("{").rstrip("}")
        strippedString = strippedString.replace(" ", "")
        
        # parse rows
        rowStrings = strippedString.split(";")
        # remove the empty element created. Need to fix this later
        rowStrings.pop(-1)

        # parse values
        for row in rowStrings:
            tempRow = []
            tempRowString = row.split(",")

            for value in tempRowString:
                tempRow.append(float(value))
            temp.append(tempRow)

        # if all rows are the same length continue
        for i in range(len(temp) - 1):
            if len(temp[i]) != len(temp[i + 1]):
                return "uneven rows error"
        
        self.matrix = temp

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
        scaledSource = []
    
        # scale the source row
        # for value in sourceRow:
        #     temp = value * scalar
        #     scaledSource.append(temp)
        scaledSource = self.returnScaled(self.matrix[sourceRow - 1], scalar)
        print(scaledSource)

        for i in range(len(self.matrix[targetRow -1])):
            if opType == 1:
                self.matrix[targetRow - 1][i] += scaledSource[i]
            else:
                self.matrix[targetRow - 1][i] -= scaledSource[i]
        
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
        if self.validateRowNumber(row):
            return self.validateRowNumber(row)
        
        if self.validateScalar(scalar):
            return self.validateScalar(scalar)

        self.matrix[row - 1] = self.returnScaled(self.matrix[row - 1], scalar)

    def returnScaled(self, row, scalar):
        temp = []

        for value in row:
            if int(scalar) != 0:
                tempValue = Fraction(value) * scalar
                if tempValue.denominator == 1:
                    tempValue = int(tempValue)
            else:
                tempValue = value * scalar

            temp.append(tempValue)
        return temp
        
    def display(self):
        columns = len(self.matrix[0])
        headerString = ""

        for i in range(columns):
            headerString += '{: >10}'.format("x" + str(i + 1))
        
        print(headerString)
        # create row strings
        for i, row in enumerate(self.matrix):
            rowString = "r" + str(i + 1)

            for i in range(len(row)):
                rowString = rowString + '{: >10f}'.format((row[i]))

                if i < len(row) - 1:
                    rowString = rowString + ","

            print(rowString)