stepArr = []

def main():
    exitLoop = "n"
    while exitLoop == "n" or exitLoop == "N":

        userInput = input("How many steps? (Enter a positive integer)\n")
        isNum = userInput.isnumeric() #Checks if input is a positive int. Includes 0
        while isNum == False: #If User does NOT enter a positive int
            userInput = input("Enter a POSITIVE INTEGER.\n")
            isNum = userInput.isnumeric()

        #Make sure there are at least 2 entries
        leapArr = input("What steps are allowed in a leap? Separate numbers by spaces: ").split()
        while (len(leapArr) < 2):
            leapArr = input("Please enter at least 2 numbers. Separate them by spaces: ").split()

        allNum = bool
        while allNum != True: #Make sure all entries are ints
            if allNum == False:
                leapArr = input("Please only enter ints. Separate them by spaces: ").split()
                while (len(leapArr) < 2):
                    leapArr = input("Please enter at least 2 numbers. Separate them by spaces: ").split()
            for i in leapArr:
                #print("Checking ", i) #Commented out for debugging
                allNum = i.isdigit()
                if(allNum == False):
                    #print(i, "is not int") #Commented out for debugging
                    break
                else:
                    #print(i, "is an int") #Commented out for debugging
                    allNum = True

        intArr = list(map(int, leapArr)) #User input is now a list of ints

        print("Steps: ", leapArr)

        exitLoop = input("Exit Program? (y/n): ")  # user input to exit while loop. Shouldn't be case-sensitive.
        while exitLoop != "y" and exitLoop != "n" and exitLoop != "Y" and exitLoop != "N":  # User needs to input either n or y
            exitLoop = input("Please input y or n: ")

    print("Closing Program.")

if __name__ == "__main__":  # ends the definition of main
    main()  # calls the main function