from random import randint

def randomWalks(Board, board, rand):
    solved = False
    if not solved:
        for n in xrange(0, rand):
            currentBoard = Board.moves(board)
            rand = randint(1,len(currentBoard.moves))
            print(currentBoard.moves[(rand - 1)])
            newBoard = Board.applyMoveCloning(board, currentBoard.moves[(rand - 1)], currentBoard.blocks)
            #normalizedBoard = board.normalize(newBoard)
            #print(newBoard.h)
            solved = Board.isSolved(newBoard)
            board = newBoard
            printDirection = ""
            if currentBoard.moves[(rand - 1)][1] == 0:
                printDirection = 'up'
            elif currentBoard.moves[(rand - 1)][1] == 1:
                printDirection = 'right'
            elif currentBoard.moves[(rand - 1)][1] == 2:
                printDirection = 'down'
            elif currentBoard.moves[(rand - 1)][1] == 3:
                printDirection = 'left'
            print(currentBoard.moves[(rand - 1)][1],printDirection)
            #board.show(board)
            print(solved)
