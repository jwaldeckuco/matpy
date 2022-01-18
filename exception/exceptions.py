
class IncorrectInputFormatError(Exception):
    pass

class UnevenRowsError(Exception):
    pass

class InvalidRowError(Exception):
    def __init__(self, row):
        self.row = row
        self.message = f"{self.row} is not a valid row. "
        super().__init__(self.message)

class InvalidScalarError(Exception):
    def __init__(self):
        self.message = "Scalar can not be 0"
        super().__init__(self.message)

class RowParseError(Exception):
    def __init__(self, row):
        self.row = row
        self.message = f"{self.row} parsing failed."
        super().__init__(self.message)