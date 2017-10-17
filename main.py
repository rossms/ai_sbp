from Board import *
from copy import deepcopy
from Search import *
#load a board from disk

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
    boardObj = Board(w,h,matrix,flatList)
    return boardObj




currentBoard = loadBoard()
#print out the current board
#currentBoard.show(currentBoard)
#clone a state/board
#newBoard = currentBoard.clone(currentBoard)
#newBoard.show(newBoard)
#print(currentBoard.isSolved(currentBoard))
#get all the moves for a current board state
#currentBoard = Board.moves(currentBoard)
#Board.show(currentBoard)
#currentBoard = Board.moves(currentBoard)
#for move in currentBoard.moves:
#    print(move[0],move[1])
#move

#currentBoard = newMove.applyMove(currentBoard,newMove, currentBoard.blocks)
#Board.show(currentBoard)
#currentBoard = board.applyMove(currentBoard, (2,3), currentBoard.blocks)
#newBoard = deepcopy(currentBoard)
#newBoard.blocks = deepcopy(currentBoard.blocks)
#Board.applyMove(newBoard, (3,3), newBoard.blocks)
#currentBoard.blocks = Board.getCurrentBlocks(currentBoard)
#newBoard = Board.applyMoveCloning(currentBoard, (2,3), currentBoard.blocks)
#Board.show(newBoard)
#newBoard = Board.moves(newBoard)
#newBoard2 = Board.applyMoveCloning(newBoard, (2,1), newBoard.blocks)
#Board.show(newBoard2)
#print(currentBoard.matrix)
#print(newBoard.matrix)
#print(Board.simpleComparison(newBoard,currentBoard))
#normalize board and then compare
#normalizedBoard = Board.normalize(newBoard)
#print(Board.simpleComparison(Board.normalize(newBoard),Board.normalize(currentBoard)))

#randomWalks(Board, currentBoard, 5)
#breathFirstPlay(Board, currentBoard)
depthFirstPlay(Board, currentBoard)
