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
#0.start with an inital board.
#1.for each current board (only one at this point)
#2.search all moves for that given board state
#3.create a copy of the board, and perform each moves independently.
#4.save those boards in list.
#5.repeat until solution is found.
def breathFirstPlay(Board, board):
    solved = False
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
                prettyPrint(board.movesToCurrent)
                Board.show(board)
    else:
        print('the provided initial board state is already solved, exiting.')

#tries all possible moves on a board, starting with a single move and finding new
#subsequent moves. traditionally in depth-first search, the search would work its
#way back up a tree when it has run into a dead end. With sliding block puzzles,
#there are no dead ends. Now if we were finding the most 'optimum' depth first
#search, then we would set a limit or make sure we never got back to the original
#board state
def depthFirstPlay(Board, board):
    solved = False
    pendingMoves = []
    boardsTried = [board]
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
                while moves:
                    pendingMove = moves.pop(0)
                    newBoard = Board.applyMoveCloning(board, pendingMove, board.blocks)
                    newBoard.movesToCurrent.append(pendingMove)
                    if (Board.isSolved(newBoard)):
                        solved = True
                        newBoard.winner = True
                        boards.append(newBoard)
                        break
                    else:
                        for b in boardsTried:
                            if Board.simpleComparison(b,newBoard):
                                break
                        else:
                            boardsTried.append(newBoard)
                            newMovesSearch = Board.moves(newBoard)
                            newBoard.pendingMoves = []
                            for newMove in newMovesSearch.moves:
                                 newBoard.pendingMoves.append(newMove)
                                 boards.insert(0, newBoard)

                            break
        for board in boards:
            if board.winner:
                prettyPrint(board.movesToCurrent)
                Board.show(board)
    else:
        print('the provided initial board state is already solved, exiting.')

#combination of breadth first search and depth first search. searches depth wise
#for a number of additional levels (default 1) and then goes back up to search
#breadth wise for any pending nodes. my implementation alternates the every level
#to try the next level deep move, or if its already tried a next level deep move,
#adds the new move to the end of the queue to try later (after all at above level
#have been attempted.)
def iterativeDeepeningSearch(Board, board):
    solved = False
    pendingMoves = []
    boardsTried = [board]
    boards = []
    #check if solved first
    if not solved:
        gamePlay = Board.moves(board)
        initialBoard = deepcopy(board)
        initialBoard.pendingMoves = []
        initialBoard.pendingMoves = gamePlay.moves
        boards.append(initialBoard)
        searchLevel = 0
        while boards:
            board = boards.pop(0)
            if solved:
                break
            else:
                moves = board.pendingMoves
                while moves:
                    pendingMove = moves.pop(0)
                    newBoard = Board.applyMoveCloning(board, pendingMove, board.blocks)
                    newBoard.movesToCurrent.append(pendingMove)
                    if (Board.isSolved(newBoard)):
                        solved = True
                        newBoard.winner = True
                        boards.append(newBoard)
                        break
                    else:
                        for b in boardsTried:
                            if Board.simpleComparison(b,newBoard):
                                break
                        else:
                            boardsTried.append(newBoard)
                            newMovesSearch = Board.moves(newBoard)
                            newBoard.pendingMoves = []
                            for newMove in newMovesSearch.moves:
                                 newBoard.pendingMoves.append(newMove)
                                 if searchLevel % 2 == 0:
                                     boards.insert(0, newBoard)
                                 else:
                                     boards.append(newBoard)
                                 searchLevel += 1
                            break
        for board in boards:
            if board.winner:
                prettyPrint(board.movesToCurrent)
                Board.show(board)
    else:
        print('the provided initial board state is already solved, exiting.')
