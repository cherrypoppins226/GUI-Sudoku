from tkinter import Tk, Frame, Button, Canvas, BOTH, TOP, BOTTOM, font
from sudoku import Sudoku 

#Board and cell dimensions
Margin = 20
Side = 50
Width = Height = Margin * 2 + Side * 9

#SudokuUI
class SudokuUI(Frame) :

    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        self.Width = Width
        self.Height = Height
        Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        self.__initUI__()

    def __initUI__(self):
        
        self.parent.title("Sudoku")
        self.pack(fill = BOTH)

        self.canvas = Canvas(self, width = self.Width, height = self.Height)
        self.canvas.pack(fill = BOTH, side = TOP)

        self.frame = Frame(self)
        #self.frame.grid(row = 2, column = 0)

        button1 = Button(self.frame, text = "Solve",bg = "green", font = ('Ariel', 16))
        button2 = Button(self.frame, text = "Reset",bg = "green", font = ('Ariel', 16), command = self.reset)
        button1.grid(row = 0, column = 2, padx = (0,2.5), pady = (0, 5))
        button2.grid(row = 0, column = 3, padx = (2.5,0), pady = (0, 5))

        self.frame.pack()

        self.draw_grid()
        self.insert_values()

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)

    #Grid drawing
    def draw_grid(self) :

        for i in range(10):
            color = "blue" if i%3 == 0 else "gray"

            x0 = Margin + i * Side
            y0 = Margin
            x1 = Margin + i * Side
            y1 = Height - Margin

            self.canvas.create_line(x0, y0, x1, y1, fill = color)

            x0 = Margin
            y0 = Margin + i * Side
            x1 = Width - Margin
            y1 = Margin + i * Side

            self.canvas.create_line(x0, y0, x1, y1, fill = color)

    def reset(self):
        self.game.__init__()
        self.insert_values()


    def insert_values(self) :
        self.canvas.delete("numbers")

        for i in range(9):
            for j in range(9):

                x = Margin + Side * i + Side / 2
                y = Margin + Side * j + Side / 2

                val = self.game.board[i][j]
                if val != 0 :
                    color = "black"
                    self.canvas.create_text(y, x, text = val,font = ('Ariel', 12, 'bold'), fill = color, tags = "numbers")

    
    def cell_clicked(self, event) :

        x, y = event.x, event.y

        if Margin < x < Width - Margin and Margin < y < Height - Margin :
            self.canvas.focus_set()
        
        row, col = (y - Margin) // Side, (x - Margin) // Side

        if (row, col) == (self.row, self.col):
            self.row, self.col = -1, -1
        elif self.game.board[row][col] == 0 :
            self.row, self.col = row, col
        
        self.highlight_cell()

    def highlight_cell(self) :
        self.canvas.delete("Highlight")

        if self.row >= 0 and self.col >= 0 :
            y0 = Margin + self.row * Side
            x0 = Margin + self.col * Side
            y1 = Margin + (self.row + 1) * Side
            x1 = Margin + (self.col + 1) * Side

            self.canvas.create_rectangle(x0, y0, x1, y1, tags = "Highlight", outline = "red")

    def key_pressed(self, event) :
        if self.row >= 0 and self.col >= 0 and event.char in "123456789" :
            val = int(event.char)
            self.game.board[self.row][self.col] = val
            self.row = -1
            self.col = -1
            if self.game.isValidMove(self.game.board, self.row, self.col, val):
                #print("Success")
                self.insert_cell(event, val)
            else:
                print("Fail")
            
    def insert_cell(self, event, value) :
        x, y = event.x, event.y
        row, col = (y - Margin) // Side , (x - Margin) // Side
        row = Margin + Side * col + Side // 2
        col = Margin + Side * row + Side // 2
        self.canvas.create_text(col, row, text = value,font = ('Ariel', 12, 'bold'), fill = "black", tags = "numbers")


root = Tk()
game = Sudoku()
sudoku = SudokuUI(root,game)
root.mainloop()







    



