from Board import *
class move(object):
    def __init__(self,block, direction):
        self.block = block
        self.direction = direction
    @staticmethod
    def applyMove(board, move, blocks):
        for b in blocks:
            if b.id == move.block:
                positions = b.currentPosition
                if (move.direction == 1) or (move.direction == 2):
                    positions = list(reversed(b.currentPosition))
                for pos in positions:
                    if move.direction == 0:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]-1][pos[1]] = b.id
                    elif move.direction == 1:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]][pos[1]+1] = b.id
                    elif move.direction == 2:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]+1][pos[1]] = b.id
                    elif move.direction == 3:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]][pos[1]-1] = b.id
        return board
    @staticmethod
    def applyMoveCloning(board, w, h, matrix, flatList, move, blocks):
        w = w
        h = h
        matrix = matrix
        flatList = flatList
        newBoard = board(w,h,matrix,flatList)
        for b in blocks:
            if b.id == move.block:
                positions = b.currentPosition
                if (move.direction == 1) or (move.direction == 2):
                    positions = list(reversed(b.currentPosition))
                for pos in b.currentPosition:
                    if move.direction == 0:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]-1][pos[1]] = b.id
                    elif move.direction == 1:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]][pos[1]+1] = b.id
                    elif move.direction == 2:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]+1][pos[1]] = b.id
                    elif move.direction == 3:
                        newBoard.matrix[pos[0]][pos[1]] = 0
                        newBoard.matrix[pos[0]][pos[1]-1] = b.id
        return newBoard
