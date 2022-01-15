
from matrix import matrix
# from decimal import Decimal
from fractions import Fraction

matrix1 = matrix.Matrix()

def greet():
    print("________________________")
    print("\tMATPY")
    print("________________________")
    print()


def quitProgram():
    print("See you next time Space Cowboy")
    exit()


def getInputMatrix():
    temp = input("Give me a matrix (in the form {x11,x12,x13;x21,x22,x23;}\n")
    #temp = "{0,2,3,4;-3,2,-2,0;3,0,2,-2;}"
    parseStatus = matrix1.parse(temp)
    # if there is an error ask again
    # right now only uneven rows are detected
    while parseStatus:
        print(parseStatus)
        temp = input("Let's try that again:\n")
        parseStatus = matrix1.parse(temp)


def displayActionMenu():
    # ask what to do
    print("What do you want to do?")
        
    # elementary ops
    print("1. Interchange rows")
    print("2. Add a row to a row")
    print("3. Subtract a row from a row")
    print("4. Scale a row")
    print("q. Quit")
    print("--------------------------")


def interchangeRowsAction():
    print("Enter the rows you want to interchange, separated by a comma: ")
    inputRows = input()
    if inputRows == "b" or inputRows == "":
        return

    row1 = int(inputRows[0])
    row2 = int(inputRows[-1])
    opStatus = matrix1.interchange(row1, row2)
    if opStatus:
        print(opStatus)
        return

    print("Operation complete!")


def addRowsAction():
    targetRow = int(input("Which row do you want to perform the operation on? "))
    sourceRow = int(input("Which row do you want to use to perform the operation? "))
    scalar = input("Enter the scalar to use: ")

    if scalar == "":
        scalar = 1
    elif "/" in scalar:
        scalar = Fraction(scalar)
    else:
        scalar = int(scalar)

    opStatus = matrix1.additionRowOp(targetRow, sourceRow, scalar)

    if opStatus:
        print(opStatus);
        return
    print("Operation Complete!")


def subtractRowsAction():
    targetRow = int(input("Which row do you want to perform the operation on? "))
    sourceRow = int(input("Which row do you want to use to perform the operation? "))
    scalar = input("Enter the scalar to use: ")

    if scalar == "":
        scalar = 1
    elif "/" in scalar:
        scalar = Fraction(scalar)
    else:
        scalar = int(scalar)

    opStatus = matrix1.subtractionRowOp(targetRow, sourceRow, scalar)

    if opStatus:
        print(opStatus);
        return
    print("Operation Complete!")

def scaleRowAction():
    temp = input("Which row do you want to scale? ")
    if temp == "b" or temp == "":
        return

    targetRow = int(temp)

    temp = input("Enter a scalar to scale by: ")
    if temp == "b":
        return
    
    if "/" in temp:
        scalar = Fraction(temp)
    elif temp == "":
        scalar = 1
    else:
        scalar = float(temp)

    matrix1.scale(targetRow, scalar)


def main():
    greet()
    getInputMatrix()
    
    quit = False
    # main loop
    while(not quit):
        print()
        matrix1.display()
        print()

        displayActionMenu()
        temp = input()

        # if quit
        if temp == "q":
            quitProgram()
        
        elif temp == "1":
            interchangeRowsAction()
        
        elif temp == "2":
            addRowsAction()

        elif temp == "3":
            subtractRowsAction()

        elif temp == "4":
            scaleRowAction()

if __name__ == "__main__":
    main()