import math

#! Start of functions 
def userMenu():
    print("____________________________________________________________")
    print("Welcome to the Equation Program")
    print("Below are some choices to select from: ")
    print("0: Exit")
    print("1: Pythagorean Equation Solver")
    print("2: Area Solver")
    print("3: Volume Solver")
    userInput = int(input("Please select choice "))
    print("")
    
    if(userInput == 0):
        exit
    while(userInput != 0):
        if(userInput == 1):
            pythagSolver()
        elif(userInput == 2):
            areaSolver()
        print("____________________________________________________________")
        print("0: Exit")
        print("1: Pythagorean Equation Solver")
        print("2: Area Solver")
        print("3: Volume Solver")
        userInput = int(input("Please select choice "))
        print("")
        
    
    
    
    
    

def pythagSolver():
    print("____________________________________________________________")
    print("What side are you trying to solve for a,b or c")
    userChoice = input("Enter the input here: ")
    userChoice = userChoice.lower()
    if(userChoice == "a"):
        c = input("Enter for side C: ")
        b = input("Enter for side B: ")
        print("{0:.3f}".format(math.sqrt(pow(int(c),2) - pow(int(b),2))))
    elif(userChoice == "b"):
        c = input("Enter for side C: ")
        a = input("Enter for side A: ")
        print("{0:.3f}".format(math.sqrt(pow(int(c),2) - pow(int(a),2))))
    else:
        a = input("Enter for side A: ")
        b = input("Enter for side B: ")
        print("{0:.3f}".format(math.sqrt(pow(int(a),2) - pow(int(b),2))))

def areaSolver():
    print("Please select some of the shapes from below to solve for the area: ")
    print("1: Circle")
    print("2: Trinagle")
    print("3: Square")
    print("4: Rectangle")
    print("5: Trapezoid")
    userInput = int(input("Enter the input here: "))
    if(userInput == 1):
        radius = int(input("Enter the radius of the circle: "))
        print("Area of the circle is " + str((math.pow(radius,2)) * math.pi))
    elif(userInput == 2):
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        print("Area of the triangle is " + str((0.5) * base * height))
    elif(userInput == 3):
        sideX = int(input("Enter a side of the square: "))
        print("Area of the square is " + str(math.pow(sideX,2)))
    elif(userInput == 4):
        base = int(input("Enter the base of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        print("Area of the rectangle is " + str(base * height))
    elif(userInput == 5):
        topBase = int(input("Enter the top base of the trapezoid: "))
        bottomBase = int(input("Enter the bottom base of the trapezoid: "))
        height = int(input("Enter the height of the trapezoid: "))
        print("Area of the trapezoid is " + str(((topBase + bottomBase) / 2) * height))

#* Start of the main program for the equation file
def main():
   userMenu()
    
if __name__=="__main__":
    main()
