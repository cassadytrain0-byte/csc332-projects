import time
import math
import csv
fibArr = [0, 1]


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]  # returns the number kept in memory

    # Base cases
    if n == 0:  # if the number entered is 0
        return 0  # the program returns the number 0
    elif n == 1:  # else, if the number entered is 1
        return 1  # the program returns the number 1

    # Recursive case
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)  # if the number entered isn't 0, the program goes through the fibonacci sequence
    return memo[n]  # returns the number found using the recursive function

def DPfib(x): #Left in print statements for debugging. Delete them if you want
    #print("\nDPFib START: " + str(x))
    #print("Array Size =", len(fibArr))
    if x < 0:
        #print("Please input a positive integer.")
        return -1

    if int(x) < len(fibArr): #check if value already exists in array

        #print("x is less than len: " + str(x))
        #print("F(" + str(x) + ") = " + str(fibArr[x]))

        return fibArr[int(x)]

    elif int(x) == len(fibArr):
        l = len(fibArr)
        #print("x is same as len: " + str(x))

        p = DPfib(l - 1)
        q = DPfib(l - 2)
        pq = p + q

        #print("pq =", pq)
        fibArr.append(pq)
        return pq

    else: #Value doesn't exist in array
        #print("x is greater than len: " + str(x))

        temp1 = DPfib(x-1)
        #print("Temp1 - ", temp1)
        temp2 = DPfib(x-2)
        #print("Temp2 - ", temp2)
        tempAdd = temp1 + temp2

        #print("Appending " + str(tempAdd))
        fibArr.append(tempAdd)

        #print("Array is now:", fibArr )

        #print("\nSuccessfully made it to end of else: " + str(x) + "\n")
        #print("F(" + str(x) + ") = " + str(fibArr[x]))
        return tempAdd



def main():
    exitLoop = "n"
    while exitLoop == "n" or exitLoop == "N":
        userInput = input("Which sequence would you like? Recursive of Dynamic?\n")
        rc = userInput
        while (userInput != "Recursive" and userInput != "Dynamic" and userInput != "r" and
            userInput != "R" and userInput != "d" and userInput != "D"):
            print("Please input Recursive or Dynamic. You may also use R and D.")
            userInput = input()

        userInput = input("What level of Fibonacci Sequence do you want to see? (Enter a positive integer)\n")
        isNum = userInput.isnumeric() #Checks if input is a positive int. Includes 0
        while isNum == False: #If User does NOT enter a positive int
            userInput = input("Enter a POSITIVE INTEGER.\n")
            isNum = userInput.isnumeric()

        if rc == "Dynamic" or rc == "d" or rc == "D": #Start Dynamic
            result = DPfib(int(userInput))
            print("F("+ userInput + ") =",result)

        if rc == "Recursive" or rc == "r" or rc == "R": #Start Recursive
            result = fibonacci(int(userInput))
            print("F("+ userInput + ") =",result)

        exitLoop = input("Exit Program? (y/n): ")  # user input to exit while loop. Shouldn't be case-sensitive.
        while exitLoop != "y" and exitLoop != "n" and exitLoop != "Y" and exitLoop != "N":  # User needs to input either n or y
            exitLoop = input("Please input y or n: ")

    print("Closing Program.")

if __name__ == "__main__":  # ends the definition of main
    main()  # calls the main function
