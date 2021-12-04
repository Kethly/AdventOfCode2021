with open('input.txt') as f:
    fullInput = [x.strip() for x in f.readlines()]
lines = str(fullInput[0])
test = fullInput[2:]
boards = []
tempArray = []
#print(test)
for x in range(len(test)):
    if str(test[x]) == '':
        boards.append(tempArray.copy())
        tempArray.clear()
    else:
        tempArray.append(test[x].split())
    if x == (len(test) - 1):
        boards.append(tempArray.copy())

def testWinCondition(arr):
    for x in arr:
        if x.count("X") == 5:
            return True
    for x in [list(x) for x in list(zip(*arr))]:
        if x.count("X") == 5:
            return True
    testArr = ""
    for x in range(len(arr)):
        testArr += arr[x][x]
    if testArr == "XXXXX":
        return True
    testArr = ""
    inverseBoard = [list(x) for x in list(zip(*boards[0]))]
    for x in range(len(inverseBoard)):
        testArr += inverseBoard[x][x]
    if testArr == "XXXXX":
        return True
    return False
def getSum(board):
    total = 0
    #print(board)
    for x in board:
        #print([0 if y=="X" else int(y) for y in x])
        total += sum(list([0 if y=="X" else int(y) for y in x]))
    return total
    
order = lines.split(",")
#print(order)
#now to get the squares

def runTest(order, boards):
    result = []
    for x in order:
        for z in range(len(boards)):
            for y in range(len(boards[z])):
                for g in range(len(boards[z][y])):
                    if boards[z][y][g] == str(x):
                        boards[z][y][g] = "X"
                        #print("replaced")
            if(testWinCondition(boards[z])):
                return [z, x]
finalResult = 0
finalBoard = []
while len(boards) > 0:
    values = runTest(order, boards)
    finalBoard = boards.pop(values[0])
    finalResult = int(values[1])

print(getSum(finalBoard) * finalResult)
