from __future__ import print_function
from copy import deepcopy
from block import *
class Board(object):
    def __init__(self,w,h,matrix,flatList):
        self.w = w
        self.h = h
        self.matrix = matrix
        self.flatList = flatList

    def show(currentBoard):
        print(currentBoard.w,',',currentBoard.h,',',sep='')
        for x in xrange(0, currentBoard.h):
            row = ''
            for y in xrange(0, currentBoard.w):
                row += str(currentBoard.matrix[x][y])
                row +=','
            print(row,sep='')
    @staticmethod
    def clone(currentBoard):
        newObj = board(currentBoard.w,currentBoard.h,currentBoard.matrix,currentBoard.flatList)
        return newObj
    @staticmethod
    def isSolved(currentBoard):
        solved = True
        for x in xrange(0, currentBoard.h):
            for y in xrange(0, currentBoard.w):
                if currentBoard.matrix[x][y] == -1:
                    solved = False
        return solved
    @staticmethod
    def getCurrentBlocks(currentBoard):
        return list(set(currentBoard.flatList) - set([-1, 0, 1]))
    @staticmethod
    def moves(currentBoard):
        blocks = list(set(currentBoard.flatList) - set([-1, 0, 1]))
        moves = []
        currblocks = []
        for b in blocks:
            for x in xrange(0, currentBoard.h):
                for y in xrange(0, currentBoard.w):
                    if currentBoard.matrix[x][y] == b:
                        #print('position of',b,'is: ',x,',',y)
                        for obj in currblocks:
                            if obj.id == b:
                                for pos in obj.currentPosition:
                                    if pos[0] != x:
                                        obj.height += 1
                                    if pos[1] != y:
                                        obj.width += 1
                                obj.currentPosition.append((x,y))
                                break
                        else:

                            bid = b
                            height = 1
                            width = 1
                            position = []
                            position.append((x,y))
                            newBlock = block(bid, height, width, position)
                            currblocks.append(newBlock)
        for obj in currblocks:
            #print('searching for new moves : ',obj.id,',',obj.height,',',obj.width,',',obj.position)
            moveUp = True
            moveRight = True
            moveDown = True
            moveLeft = True
            for pos in obj.currentPosition:

                if currentBoard.matrix[pos[0]-1][pos[1]] != 0 and currentBoard.matrix[pos[0]-1][pos[1]] != obj.id:
                    moveUp = False
                if currentBoard.matrix[pos[0]][pos[1]+1] != 0 and currentBoard.matrix[pos[0]][pos[1]+1] != obj.id:
                    moveRight = False
                if currentBoard.matrix[pos[0]+1][pos[1]] != 0 and currentBoard.matrix[pos[0]+1][pos[1]] != obj.id:
                    moveDown = False
                if currentBoard.matrix[pos[0]][pos[1]-1] != 0 and currentBoard.matrix[pos[0]][pos[1]-1] != obj.id:
                    moveLeft = False
            if moveUp:
                newMove = (obj.id,0)
                moves.append(newMove)
            if moveRight:
                newMove = (obj.id,1)
                moves.append(newMove)
            if moveDown:
                newMove = (obj.id,2)
                moves.append(newMove)
            if moveLeft:
                newMove = (obj.id,3)
                moves.append(newMove)

        #for obj in moves:
            #print('blockid:',obj.block,',direction:',obj.direction)
        currentBoard.blocks = currblocks
        currentBoard.moves = moves
        return currentBoard
    @staticmethod
    def applyMove(Board, move, blocks):
        newMatrix = Board.matrix
        for b in blocks:
            if b.id == move[0]:
                positions = b.currentPosition
                if (move[1] == 1) or (move[1] == 2):
                    positions = list(reversed(b.currentPosition))
                for pos in positions:
                    if move[1] == 0:
                        newMatrix[pos[0]][pos[1]] = 0
                        newMatrix[pos[0]-1][pos[1]] = b.id
                    elif move[1] == 1:
                        newMatrix[pos[0]][pos[1]] = 0
                        newMatrix[pos[0]][pos[1]+1] = b.id
                    elif move[1] == 2:
                        newMatrix[pos[0]][pos[1]] = 0
                        newMatrix[pos[0]+1][pos[1]] = b.id
                    elif move[1] == 3:
                        newMatrix[pos[0]][pos[1]] = 0
                        newMatrix[pos[0]][pos[1]-1] = b.id
        Board.matrix = newMatrix
    @staticmethod
    def applyMoveCloning(board, move, blocks):
        newBoard = deepcopy(board)
        newBoard.blocks = deepcopy(blocks)
        for b in blocks:
            if b.id == move[0]:
                positions = b.currentPosition
                if (move[1] == 1) or (move[1] == 2):
                    positions = list(reversed(b.currentPosition))
                for pos in positions:
                    if move[1] == 0:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]-1][pos[1]] = b.id
                    elif move[1] == 1:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]][pos[1]+1] = b.id
                    elif move[1] == 2:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]+1][pos[1]] = b.id
                    elif move[1] == 3:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]][pos[1]-1] = b.id
        return newBoard
    @staticmethod
    def simpleComparison(board1, board2):
        identical = True
        if (board1.h != board2.h) or (board1.w != board2.w):
            identical = False
        for x in xrange(0, board1.h):
            for y in xrange(0, board1.w):
                #print ('board1:',board1.matrix[x][y])
                #print ('board2:',board2.matrix[x][y])
                if board1.matrix[x][y] != board2.matrix[x][y]:
                    identical = False
                    break
        return identical
    @staticmethod
    def normalize(board):
        nextIndex = 3
        for x in xrange(0, board.h):
            for y in xrange(0, board.w):
                if board.matrix[x][y] == nextIndex:
                    nextIndex += 1
                elif board.matrix[x][y] > nextIndex:
                    swapIdx(nextIndex, board.matrix[x][y],board)
                    nextIndex += 1
        return board
    @classmethod
    def swapIdx(self, idx1, idx2, board):
        for x in xrange(0, board.h):
            for y in xrange(0, board.w):
                if board.matrix[x][y] == idx1:
                    board.matrix[x][y] = idx2
                elif board.matrix[x][y] == idx2:
                    board.matrix[x][y] = idx1
        return board
