import random
import time
import math
import csv

NUM_INTS = 1000  # the multiplictor of how many ints will be in each list
RAND_MIN = 1  # smallest number
RAND_MAX = 9000  # largest number


def print_unsorted(num, list):
    print("Array {}: Unsorted".format(num))  # prints which unsorted list is being looked at
    print("--------------------------------------------------------------------------------------------------")
    for i in list:  # goes through all items in the list
        print(i, end=' ')  # prints every item in the list


def print_merge_sort(num, list):
    print(" ")
    print("Array {}: Sorted".format(num))  # prints which list is being looked at
    print("--------------------------------------------------------------------------------------------------")
    print(merge_sort(list))  # prints the sorted list by calling the merge_sort function


def merge_sort(list):
    if len(list) <= 1:  # checks if the list is <= 1 in length
        return list  # returns the original list if it it <= 1 in length

    mid = len(list) // 2  # finds the middle number in the list
    left_half = merge_sort(list[:mid])  # splits the list in half, assigning the top to left_half
    right_half = merge_sort(list[mid:])  # splits the list in half, assigning the bottom to right_half

    return merge(left_half, right_half)  # returns the newly sorted list using the merge function


def rand_array(num):
    arr = [(random.randint(RAND_MIN, RAND_MAX)) for _ in
           range(NUM_INTS * num)]  # creates an array with random numbers and length changes based off of array num
    return arr  # returns the array


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):  # sorts the two lists by ascending numerical order
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result  # returns the sorted list


# ----------MAIN PROGRAM----------

def main():
    random_list_1 = rand_array(1)  # creates a list using the rand_array() function

    random_list_2 = rand_array(2)

    random_list_3 = rand_array(3)

    random_list_4 = rand_array(4)

    random_list_5 = rand_array(5)

    random_list_6 = rand_array(6)

    random_list_7 = rand_array(7)

    random_list_8 = rand_array(8)

    random_list_9 = rand_array(9)

    arrays = {
        1: random_list_1,
        2: random_list_2,
        3: random_list_3,
        4: random_list_4,
        5: random_list_5,
        6: random_list_6,
        7: random_list_7,
        8: random_list_8,
        9: random_list_9,
    }

    sorted_arrays = {}
    results = []

    for i in range(1, 10):
        arr_copy = arrays[i].copy()
        n = len(arr_copy)
        n_log_n = n * math.log2(n)

        start = time.perf_counter()
        sorted_arr = merge_sort(arr_copy)
        end = time.perf_counter()

        elapsed = end - start
        ratio = n_log_n / elapsed if elapsed > 0 else 0

        sorted_arrays[i] = sorted_arr

        results.append([

            n,
            f"{n_log_n:.2f}",
            f"{elapsed:.6f}",
            f"{ratio:.3E}"
        ])

    with open("Mergesort_Time.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Input size n",
            "n* log2(n)",
            "Time spent (seconds)",
            "(n * log n) / time"
        ])
        writer.writerows(results)

    exitLoop = "n"

    while exitLoop == "n" or exitLoop == "N":
        userInput = input(
            "Which array would you like to see? (#1-9) ")  # takes the user's input for which array they would like to see

        while (userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4" and
               userInput != "5" and userInput != "6" and userInput != "7" and userInput != "8" and
               userInput != "9"):  #If the user enters something other than a number from 1-9, force reentry.
            userInput = input("Enter a number from 1 to 9: ")

        arr = int(userInput)

        if arr > 9 or arr < 0:  # checks that the number inputted isn't greater than 9 or less than 0
            arr = int(input(
            "That is not a valid number, enter a number 1-9: "))  # if num > 9 or num < 0, tells the user to input a num 1-9
            if arr == 1:  # if user then enters 1
                print_unsorted(arr, random_list_1)  # prints the unsorted array using the print_unsorted function for 1
                print_merge_sort(arr, random_list_1)  # prints the sorted array using the print_sorted function for 1
            elif arr == 2:  # if user enters 2
                print_unsorted(arr, random_list_2)  # prints the unsorted array using the print_unsorted function for 2
                print_merge_sort(arr, random_list_2)  # prints the sorted array using the print_sorted function for 2
            elif arr == 3:
                print_unsorted(arr, random_list_3)
                print_merge_sort(arr, random_list_3)
            elif arr == 4:
                print_unsorted(arr, random_list_4)
                print_merge_sort(arr, random_list_4)
            elif arr == 5:
                print_unsorted(arr, random_list_5)
                print_merge_sort(arr, random_list_5)
            elif arr == 6:
                print_unsorted(arr, random_list_6)
                print_merge_sort(arr, random_list_6)
            elif arr == 7:
                print_unsorted(arr, random_list_7)
                print_merge_sort(arr, random_list_7)
            elif arr == 8:
                print_unsorted(arr, random_list_8)
                print_merge_sort(arr, random_list_8)
            else:
                print_unsorted(arr, random_list_9)
                print_merge_sort(arr, random_list_9)
        else:  # if the user enters a number 1-9, goes through the same if-else statements as above
            if arr == 1:
                print_unsorted(arr, random_list_1)
                print_merge_sort(arr, random_list_1)
            elif arr == 2:
                print_unsorted(arr, random_list_2)
                print_merge_sort(arr, random_list_2)
            elif arr == 3:
                print_unsorted(arr, random_list_3)
                print_merge_sort(arr, random_list_3)
            elif arr == 4:
                print_unsorted(arr, random_list_4)
                print_merge_sort(arr, random_list_4)
            elif arr == 5:
                print_unsorted(arr, random_list_5)
                print_merge_sort(arr, random_list_5)
            elif arr == 6:
                print_unsorted(arr, random_list_6)
                print_merge_sort(arr, random_list_6)
            elif arr == 7:
                print_unsorted(arr, random_list_7)
                print_merge_sort(arr, random_list_7)
            elif arr == 8:
                print_unsorted(arr, random_list_8)
                print_merge_sort(arr, random_list_8)
            else:
                print_unsorted(arr, random_list_9)
                print_merge_sort(arr, random_list_9)
        exitLoop = input("Exit Program? (y/n): ") #user input to exit while loop. Shouldn't be case-sensitive.
        while exitLoop != "y" and exitLoop != "n" and exitLoop != "Y" and exitLoop != "N": #User needs to input either n or y
            exitLoop = input("Please input y or n: ")

    print("Closing Program.")
if __name__ == "__main__":  # ends the definition of main
    main()  # calls the main function
