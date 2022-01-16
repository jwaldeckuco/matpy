
from operator import truediv
from matrix import matrix
from fractions import Fraction
from matrix import matrixhistory
from matrix import operationresult
from exception import exceptions
# from ui import wxui
# import wx

# globals
matrix1 = matrix.Matrix()
history = matrixhistory.MatrixHistory()

def greet():
    # user greeting
    print("________________________")
    print("\tMATPY")
    print("Matrix Algebra Row Operation Calculator")
    print("________________________")
    print()


def quitProgram():
    print("See you next time Space Cowboy")
    exit()


def getInputMatrix():
    global matrix1
    dev = False
    goodParse = True
    firstTry = True

    while firstTry or not goodParse:
        firstTry = False
        
        if dev:
            # testing matrix
            # uncomment below for testing
            #temp = "{0,2,3,4;-3,2,-2,0;3,0,2,-2;}"
            temp = "{1,0,1,-6;3,2,-1,4;2,1,0,-1;}"
            augmented = "y"
        else:
            temp = input("Give me a matrix (in the form {x11,x12,x13;x21,x22,x23;} but without the xs\n")
            augmented = input("Is this an augmented matrix (y/n)? ")

        if augmented == "y":
            augmented = True
        else: 
            augmented = False
        try:
            matrix1.parse(temp)
        except:
            print("Parsing error... please try again")
            goodParse = False
        finally:
            goodParse = True
  
    matrix1.setAugmented(augmented)
    history.add(operationresult.OperationResult(["init"], matrix1))


def displayActionMenu():
    # ask what to do
    print("What do you want to do?")
        
    # elementary ops
    print("1. Interchange rows")
    print("2. Add a row to a row")
    print("3. Subtract a row from a row")
    print("4. Scale a row")
    print("5. Show history")
    print("6. Export history")
    print("u. Undo last operation")
    print("n. Start over with a new matrix")
    print("q. Quit")
    print("--------------------------")


def interchangeRowsAction():
    print("Enter the rows you want to interchange, separated by a comma: ")
    inputRows = input()
    if inputRows == "b" or inputRows == "":
        print("Going back")
        return
    if len(inputRows) < 3:
        print("Invalid row. Going back")
        return

    try:
        row1 = int(inputRows[0])
        row2 = int(inputRows[-1])
    except:
        print("Invalid row... or something. Going back.")

    opStatus = matrix1.interchange(row1, row2)
    if opStatus:
        print(opStatus)
        return
    history.add(operationresult.OperationResult(["interchange", row1, row2], matrix1))

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

    history.add(operationresult.OperationResult(["add", targetRow, sourceRow, scalar], matrix1))

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
        print(opStatus)
        return

    history.add(operationresult.OperationResult(["subtract", targetRow, sourceRow, scalar], matrix1))

    print("Operation Complete!")


def scaleRowAction():
    temp = input("Which row do you want to scale? ")
    if temp == "b" or temp == "":
        print("Going back")
        return

    try:
        targetRow = int(temp)
    except ValueError:
        print("Invalid row selection. Returning you to main menu.")
        return

    temp = input("Enter a scalar to scale by: ")
    if temp == "b":
        return
    
    if "/" in temp:
        scalar = Fraction(temp)
    elif temp == "":
        scalar = 1
    else:
        scalar = float(temp)

    opStatus = matrix1.scale(targetRow, scalar)
    if opStatus:
        print(opStatus)
        return
    
    history.add(operationresult.OperationResult(["scale", targetRow, scalar], matrix1))


def undo():
    global matrix1
    matrix1 = history.undo().getMatrix()
    print("I am undone")


def new():
    global history
    temp = input("Are you sure (y/n)? ")
    if temp == "n" or temp == "":
        print("Ok, going back.")
        return
    
    history.reset()
    print()
    getInputMatrix()


def main():
    # app = wx.App()
    # frame = wxui.WxUI()
    # app.MainLoop()
    
    greet()
    getInputMatrix()
    
    quit = False
    # main loop
    while(not quit):
        print()
        print("current: ")
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

        elif temp == "5":
            history.display()

        elif temp == "6":
            history.writeFile()
        
        elif temp == "u":
            undo()

        elif temp == "n":
            new()
        

if __name__ == "__main__":
    main()