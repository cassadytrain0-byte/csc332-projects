from itertools import combinations
import time

testlist = []
setList = []

class Task:  # groups all of the information about a task into a singular object
    def __init__(self, id, start, end, val):
        self.id = id
        self.start = start
        self.end = end
        self.val = val


def getTasks():
    n = int(input("Enter number of tasks: "))  # asks the user for the number of tasks the program needs to complete
    tasks = []

    for i in range(n):  # repeats the loop until the value of n is reached
        print(f"Task {i + 1}:")  # prints which task the loop is on
        start = int(input("Start Time: "))  # takes user input for the start time
        end = int(input("End Time: "))  # takes user input for the end time
        val = int(input("Value: "))  # takes user input for the value
        tasks.append(Task(i, start, end, val))  # adds all of the numbers into a shared task

    tasks.sort(key=lambda x: x.end)  # sorts by the end time

    return tasks


def printTasks(tasks):  # this function prints all of the infdrmation about a task
    print("\nTasks sorted by end time:")
    print("ID | Start | End | Value")
    for t in tasks:
        print(f"{t.id + 1} | {t.start} | {t.end} | {t.val}")


def compPrevious(tasks):
    p = []
    for i in range(len(tasks)):
        print(i)
        j = i - 1
        print(j)
        while j >= 0 and tasks[j].end > tasks[i].start:
            j -= 1
        p.append(j)
        testlist.append(j)
    return p

def maxVal(tasks, tasknum): #finds max(i). tasknum should be i - 1. Assuming for loops begin @ 1 and not 0
    #print("Maxval Start: Tasknum", tasknum)

    if tasknum < 1: return 0

    maxm = 0
    lastMax = 0
    prevMax = 0
    #print("Generate prevList:")
    #prevList = compPrevious(tasks)
    i = tasknum - 1
    #print("I =", i)
    j = tasknum - 2
    #print("J =", j)

    if (i == 0): #i is in position 0
        #print("Task", tasknum, "has a value of", tasks[i].val) #tasks is NOT a list
        if tasknum not in setList:
            setList.append(tasknum)

        return tasks[i].val

    elif(i > 0):
        lastMax += maxVal(tasks, i) #find max of tasknum-1
        if (testlist[i] < 0): prevMax = 0
        else: prevMax += maxVal(tasks, testlist[i] + 1) #find max of prev()


    if (j >= 0) and (lastMax > tasks[i].val + prevMax): #i is in position 1+, max(i-1) is greater
        #print("Task", tasknum, "- LASTMAX - Task", tasks[j].id, "has a value of", tasks[j].val)
        maxm += tasks[j].val
        if tasknum not in setList:
            setList.append(tasknum)

    elif (j >= 0) and (tasks[i].val + prevMax >= lastMax): #i is in postion 1+, value + max(prev(i)) is greater
        maxm += tasks[i].val
        maxm += prevMax
        if tasknum not in setList:
            setList.append(tasknum)
        #print("Task", tasknum, "- PREVMAX - task", tasknum, "has a value of", maxm)

    #print("Max of", tasknum, "is", maxm, "-- val =", tasks[i].val, "prevmax =", prevMax)
    return maxm

def bruteForce(tasks):  # runs the tasks through the brute force algorithm
    startTime = time.time()
    n = len(tasks)
    bestVal = 0
    bestSets = []

    for r in range(1, n + 1):
        for subset in combinations(tasks, r):
            subset = sorted(subset, key=lambda x: x.end)

            valid = True
            for i in range(len(subset) - 1):
                if subset[i].end > subset[i + 1].start:
                    valid = False
                    break

            if valid:
                total = sum(t.val for t in subset)
                if total > bestVal:
                    bestVal = total
                    bestSets = [subset]
                elif total == bestVal:
                    bestSets.append(subset)

    elapsed = time.time() - startTime
    return bestVal, bestSets, elapsed

def recursive(tasks): #start at end of list and move to front
    startTime = time.time()
    n = len(tasks)
    bestVal = 0
    bestSets = setList

    bestVal = maxVal(tasks, n)





    elapsed = time.time() - startTime
    return bestVal, bestSets, elapsed

def dynamic(tasks): #start at front of list and move to end, adding elements to an array
    startTime = time.time()
    n = len(tasks)
    bestVal = 0
    bestSets = []
    completed = []




    elapsed = time.time() - startTime
    return bestVal, bestSets, elapsed

def printResults(name, val, sets, elapsedTime):
    print(f"\n{name}")
    print(f"Time Elapsed: {elapsedTime:.6f}s")
    print(f"Maximum Earning = {val}")

    for s in sets:
        order = " -> ".join(f"Task_{t.id + 1}" for t in s)
        print(f"{order}, total earning = {val}")


def main():
    tasks = getTasks()
    printTasks(tasks)

    p = compPrevious(tasks) #when does this get used?

    bf_val, bf_sets, bf_time = bruteForce(tasks)
    printResults("Brute Force", bf_val, bf_sets, bf_time)
    rec_val, rec_sets, rec_time = recursive(tasks)
    print("Recursive\n Time Elapsed:", rec_time * .6, "\n Maximum Earning:", rec_val, "\nTask Sets:", rec_sets)
    #dyn_val, dyn_sets, dyn_time = dynamic(tasks)
    #printResults("Dynamic", dyn_val, dyn_sets, dyn_time)

main()