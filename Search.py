from random import randint
from copy import deepcopy

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
        pendingMoves = gamePlay.moves
        initialBoard = deepcopy(board)
        #
        #
        #
        #add one board to boards[]
        #while boards 
        #1.get moves for current board
        #2.create deepcopy for each move, make move, check goal state, add board to boards
        #3. remove level -1 boards
        #
        #
        #
        #initialState = state([],initialBoard)
        #print(initialState)
        #print(newState)
        Board.show(initialBoard)
        while pendingMoves:
            #copyBoard = Board(initialBoard.h, initialBoard.w,initialBoard.matrix,initialBoard.flatList)
            #newBoard = deepcopy(initialBoard)
            pendingMove = pendingMoves.pop(0)
            print(pendingMove)
            newBoard = Board.applyMoveCloning(initialBoard, pendingMove, initialBoard.blocks)
            newBoard.movesToCurrent = []
            newBoard.movesToCurrent.append(pendingMove)
            #newState = state([],newBoard)
            boards.append(newBoard)

        #print(initialState)
        #print(newState)
        #Board.show(initialState.currentBoard)
        #board.show(newState.currentBoard)

        #while pendingMoves:
            #for pm in pendingMoves:
                ##print(pm.block,',',pm.direction)

            #print('currentGameBoard')
            #self.show(boardx)
            #pendingMove = pendingMoves.pop(0)
            #print('current move',pendingMove.block,',',pendingMove.direction)
            #newBoard = move.applyMoveCloning(move(), initialBoard, pendingMove, gamePlay.blocks)
            #self.show(newBoard)
            #newBoard.movesToCurrent.append(pendingMove)
            #boards.append(newBoard)

            # if pendingMove not in movesTried:
            #     movesTried.append(pendingMove)
            #     newBoard = move.applyMoveCloning(move(), board, pendingMove, gamePlay.blocks)
            #     self.show(newBoard)
            #     if(self.isSolved(newBoard)):
            #         solved = True
            #         break
            #     newBoard.movesToCurrent.append(pendingMove)
            #     boards.append(newBoard)
                #nextGamePlay = self.moves(newBoard, self.getBlocks(newBoard))
            #for newMove in nextGamePlay.moves:
                #print('new move:',newMove.block,',',newMove.direction)
                #pendingMoves.append(newMove)
            #gameBoard = newBoard
            #blocks = nextGamePlay.blocks
        i = 0
        for board in boards:
            i+=1
            print('board',i)
            Board.show(board)
        for correctMoves in movesTried:
            print('blockid:',correctMoves.block,',direction:',correctMoves.direction)
    else:
        print('solved!!!!!')
