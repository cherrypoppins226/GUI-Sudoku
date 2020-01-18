
import math as m

from bo import Board

class Sudoku():

    #self.board = Board()
    def __init__(self) :
        self.board = Board() #original
        self.solved = []
        
    def fill_values(self):
        for i in range(9):
            l = []
            for j in range(9):
                l.append(self.board[i][j])
            self.solved.append(l)

    def isValidMove(self,board, row, col, num) :
        for i in range(9):
            if board[row][i] == num or board[i][col] == num :
                return False

        subgridSize = int(m.sqrt(len(board)))

        blockRow = row // subgridSize
        blockCol = col // subgridSize

        blockRowIndex = blockRow * subgridSize
        blockColIndex = blockCol * subgridSize

        for i in range(3) :
            for j in range(3):
                if board[blockRowIndex + i][blockColIndex + j] == num :
                    return False
            
        return True

    def solve(self, board, row, col):
        if col == len(board[0]) :
            col = 0
            row += 1
        if row == len(board) :
            return True

        if board[row][col] != 0 :
            return self.solve(board, row, col + 1)
        
        for num in range(1, 10) :
            if self.isValidMove(board,row,col,num):
                board[row][col] = num
                self.solved[row][col] = num
                if self.solve(board, row, col + 1) :
                    return True
            
            board[row][col] = 0
        
        return False
    
    




