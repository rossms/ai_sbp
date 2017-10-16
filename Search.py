from __future__ import print_function
from random import randint
from copy import deepcopy

def prettyPrint(moves):
    for move in moves:
        printDirection = ""
        if move[1] == 0:
            printDirection = 'up'
        elif move[1] == 1:
            printDirection = 'right'
        elif move[1] == 2:
            printDirection = 'down'
        elif move[1] == 3:
            printDirection = 'left'
        print('(',move[0],',',printDirection,')',sep='')

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

#finds a solution given a board, by searching/moving all of the known moves first,
#then applying those moves and searching/moving all moves from those states, and so on
def breathFirstPlay(Board, board):
    solved = False
    movesTried = []
    pendingMoves = []
    boards = []
    #check if solved first
    if not solved:
        gamePlay = Board.moves(board)
        initialBoard = deepcopy(board)
        initialBoard.pendingMoves = []
        initialBoard.pendingMoves = gamePlay.moves
        boards.append(initialBoard)
        while boards:
            board = boards.pop(0)
            if solved:
                break
            else:
                moves = board.pendingMoves
                for pendingMove in board.pendingMoves:
                    newBoard = Board.applyMoveCloning(board, pendingMove, board.blocks)
                    newBoard.movesToCurrent.append(pendingMove)
                    if (Board.isSolved(newBoard)):
                        solved = True
                        newBoard.winner = True
                        boards.append(newBoard)
                        break
                    else:
                        newMovesSearch = Board.moves(newBoard)
                        newBoard.pendingMoves = newMovesSearch.moves
                        boards.append(newBoard)
        for board in boards:
            if board.winner:
                Board.show(board)
                prettyPrint(board.movesToCurrent)
                #for move in board.movesToCurrent:
                    #print 'move:',move
    else:
        print('the provided initial board state is already solved, exiting.')
