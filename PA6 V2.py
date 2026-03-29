def getUserInput():
    seq1 = input("Enter first sequence (No spaces): ").strip()
    seq2 = input("Enter second sequence (No spaces): ").strip()

    match = int(input("Enter match score: "))
    mismatch = int(input("Enter mismatch penalty: "))
    gap = int(input("Enter gap penalty: "))

    return seq1, seq2, match, mismatch, gap

def initializeDP(seq1, seq2, gap, match, mismatch):
    m = len(seq1)
    n = len(seq2)

    print("M =", m) #x coordinate
    print("N =", n) #y coordinate
    print(seq1)
    print(seq2)

    one = list(seq1) #turn strings into lists
    two = list(seq2)
    one.insert(0, '_') #insert gap as beginning of list
    two.insert(0, '_')

    #Create a DP table
    dp = [[0] * (m + 1) for x in range(0, n + 1)]

    #Initialize first row and column
    for i in range(1, n + 1): #Fill first Column, seq2
        dp[i][0] = i * gap

    for j in range(1, m + 1): #Fill first Row, seq1
        dp[0][j] = j * gap

    for i in range(1, n + 1): #pick the row
        for j in range(1, m + 1): #pick the column
            diagonal = 0
            right = dp[i][j - 1] + gap
            down = dp[i - 1][j] + gap
            if(one[j] == two[i]):
                diagonal = dp[i - 1][j - 1] + match
            else:
                diagonal = dp[i - 1][j - 1] + mismatch

            if(diagonal >= right and diagonal >= down):
                dp[i][j] = diagonal
            elif(right > diagonal and right > down):
                dp[i][j] = right
            else: #elif(down > diagonal and down > right):
                dp[i][j] = down


    return dp

def printDPTable(dp):
    print("\nDP Table:")
    for row in dp:
        print(row)

def main():
    seq1, seq2, match, mismatch, gap = getUserInput()
    dp = initializeDP(seq1, seq2, gap, match, mismatch)

    printDPTable(dp)

if __name__ == "__main__":
    main()