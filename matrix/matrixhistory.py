
class MatrixHistory:
    def __init__(self):
        self.history = []

    def getLast(self):
        if len(self.history) > 0:
            return self.history[-1]
    
    def undo(self):
        if len(self.history) > 1:
            self.history.pop()
            
        return self.history[-1]

    def add(self, operationResult):
        self.history.append(operationResult)

    def display(self):
        print(self.getStringRep())

    def getStringRep(self):
        string = ""

        for operation in self.history:
            rowOperation = operation.getOperation()
            opType = operation.getOpType()
            opString = "operation: " + opType + " "

            if opType == "interchange":
                opString += "r" + str(rowOperation[1]) + " and r" + str(rowOperation[2])
            elif opType == "add":
                opString += str(rowOperation[3]) + "r" + str(rowOperation[2]) + " to r" + str(rowOperation[1])
            elif opType == "subtract":
                opString += str(rowOperation[3]) + "r" + str(rowOperation[2]) + " from r" + str(rowOperation[1])
            elif opType == "scale":
                opString += "r" + str(rowOperation[1]) + " by " + str(rowOperation[2])

            opString += "\n result:\n"
            opString += operation.getMatrix().getStringRep()
            
            string += opString + "\n"
        return string

    def writeFile(self):
        file = open("save.txt", "w")
        file.write(self.getStringRep())
        file.close()
            
        