from board import *

def loadBoard():
    #fname = raw_input('Please provide a file and absolute path.. and then hit RETURN / ENTER \n')
    fname = '/Users/Ross/Documents/Grad_School/CS510/sbp/docs/SBP-level0.txt'
    with open(fname) as f:
        content = f.read()

    inputNums = content.replace("\n", "").split(",")
    w = int(inputNums[0])
    h = int(inputNums[1])
    matrix = [[0 for x in range(w)] for x in range(h)]
    inputNumsIndex = int(2)
    for x in xrange(0, h):
        for y in xrange(0, w):
            matrix[x][y] = int(inputNums[inputNumsIndex])
            inputNumsIndex += 1
    flatList = [item for sublist in matrix for item in sublist]
    boardObj = board(w,h,matrix,flatList)
    return boardObj
