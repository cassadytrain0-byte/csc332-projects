
class Node:

    def __init__(self, nodeName, connected): #connected should be an array of every node that it is connected to
        self.name = nodeName
        self.connections = connected.split()
        self.vertex = ["White"] * len(self.connections) #list of colors. same len as connections.


def getNode():
    nodeList = []
    userInput = input("How many nodes? ")
    isNum = userInput.isdigit()
    while isNum == False:
        userInput = input("Enter a POSITIVE INTEGER.\n")
        isNum = userInput.isnumeric()

    cycle = int(userInput)
    for i in range(cycle):
        name = input("Enter node name: ")
        connections = input("What is node " + name + " connected to? Enter as list with spaces: ")
        x = Node(name, connections)
        nodeList.append(x)

    return nodeList


def printNodes(nodeList):
    print("\nPrinting Nodes:")
    for i in nodeList:
        print("\t" + i.name + " -> ", end = "")
        for j in i.connections:
            print(j, end = " ")
        print("")

def printMatrix(nodeList):
    print("\nPrinting Matrix: ")



def main():
    nodes = getNode()
    printNodes(nodes)
    printMatrix(nodes)

main()