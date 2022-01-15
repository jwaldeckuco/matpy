
class OperationResult:
    def __init__(self, operation, matrix):
        self.operation = operation
        self.matrix = matrix.deepCopy()

    def getOperation(self):
        return self.operation

    def getOpType(self):
        return self.operation[0]
    
    def getMatrix(self):
        return self.matrix