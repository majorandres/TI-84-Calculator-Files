import math

#! Start of functions 
def userMenu():
    print("____________________________________________________________")
    print("Welcome to the Equation Program")
    print("Below are some choices to select from: ")
    print("0: Exit")
    print("1: Pythagorean Equation Solver")
    userInput = int(input("Please select choice "))
   
    
    if(userInput == 0):
        exit
    while(userInput != 0):
        print("0: Exit")
        print("1: Pythagorean Equation Solver")
        print("")
        
        if(userInput == 1):
            pythagSolver()
        print("____________________________________________________________")
        userInput = int(input("Please select choice "))
        
    
    
    
    
    

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
    
    

#* Start of the main program for the equation file
def main():
   userMenu()
    
if __name__=="__main__":
    main()
