
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
    dev = True
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


def displayRowOpMenu():
    # ask what to do
    print("What do you want to do?")
        
    # elementary ops
    print("  1. Interchange rows")
    print("  2. Add a row to a row")
    print("  3. Subtract a row from a row")
    print("  4. Scale a row")
    print("  (u)ndo last operation")
    print("  (b)ack")
    print("  (q)uit")
    print("--------------------------")

def displayMainMenu():
    # ask what to do
    print("What do you want to do?")
        
    print("  (r)ow Operations")
    print("  (h)istory")
    print("  (e)xport history")
    print("  (n)ew matrix")
    print("  (q)uit")
    print("--------------------------")


def interchangeRowsAction():
    print("Enter the rows you want to interchange, separated by a comma: ")
    inputRows = input()
    if inputRows == "b" or inputRows == "":
        print("Gotcha. Returning to the main menu")
        return

    if len(inputRows) < 3:
        print("You didn't give me two rows. Returning to the main menu")
        return

    inputRows = inputRows.split(",")

    for row in inputRows:
        try: 
            int(row) - 1

        except ValueError:
            print(f"\nHA! \'{row}\' isn't valid input. I cast ye back to the main menu")
            return 

    row1 = int(inputRows[0]) - 1
    row2 = int(inputRows[-1]) - 1
   
    try:
        matrix1.interchange(row1, row2)
    except Exception as e:
        print(e)
        return

    history.add(operationresult.OperationResult(["interchange", row1 + 1, row2 + 1], matrix1))

    print("Operation complete!")


def getOperationInputs():
    targetRow = int(input("Which row do you want to perform the operation on? "))
    sourceRow = int(input("Which row do you want to use to perform the operation? "))
    scalar = input("Enter the scalar to use: ")

    return [targetRow -1, sourceRow - 1, scalar]


def parseScalar(scalar):
    if scalar == "":
        return 1
    elif "/" in scalar:
        return Fraction(scalar)
    elif "." in scalar:
        return float(scalar)
    else:
        return int(scalar)


def addRowsAction():
    inputs = getOperationInputs()
    scalar = parseScalar(inputs[2])

    try:
        matrix1.additionRowOp(inputs[0], inputs[1], scalar)
    except Exception as e:
        print(e)
        return

    history.add(operationresult.OperationResult(["add", inputs[0] + 1, inputs[1] + 1, scalar], matrix1))

    print("Operation Complete!")


def subtractRowsAction():
    inputs = getOperationInputs()
    scalar = parseScalar(inputs[2])

    try:
        matrix1.subtractionRowOp(inputs[0], inputs[1], scalar)
    except Exception as e:
        print(e)
        return

    history.add(operationresult.OperationResult(["subtract", inputs[0] + 1, inputs[1] + 1, scalar], matrix1))

    print("Operation Complete!")


def scaleRowAction():
    temp = input("Which row do you want to scale? ")
    if temp == "b" or temp == "":
        print("Going back")
        return

    try:
        targetRow = int(temp) - 1
    except ValueError:
        print("That wasn't an integer. Returning you to main menu.")
        return

    # get scalar and parse
    temp = input("Enter a scalar to scale by: ")
    if temp == "b":
        return
    scalar = parseScalar(temp)

    try:
        matrix1.scale(targetRow, scalar)

    except Exception as e:
        print(e + "Returning you to the main menu")
        return
   
    history.add(operationresult.OperationResult(["scale", targetRow + 1, scalar], matrix1))


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


def rowOpsMenu():
    temp = ""
    while True:
        print()
        print("Current: ")
        print("------------------------------------------")
        matrix1.display()
        print("------------------------------------------")
        print()

        displayRowOpMenu()
        temp = input()

        if temp == "q":
            quitProgram()

        elif temp == "b":
            return

        elif temp == "1":
            interchangeRowsAction()
        
        elif temp == "2":
            addRowsAction()

        elif temp == "3":
            subtractRowsAction()

        elif temp == "4":
            scaleRowAction()

        elif temp == "u":
            undo()

        elif temp == "n":
            new()


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
        print("Current: ")
        print("------------------------------------------")
        matrix1.display()
        print("------------------------------------------")
        print()

        displayMainMenu()
        temp = input()

        # if quit
        if temp == "q":
            quitProgram()
        
        elif temp == "r":
            rowOpsMenu()
        
        elif temp == "h":
            history.display()

        elif temp == "e":
            history.writeFile()

        elif temp == "n":
            new()
        

if __name__ == "__main__":
    main()