import tkinter as tk
from random import randint, shuffle

class Minesweeper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.width = 10
        self.height = 10
        self.mines = [(i, j) for i in range(self.height) for j in range(self.width)]
        shuffle(self.mines)
        self.revealed = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.buttons = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                button = tk.Button(self.root, text="", width=2, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, i, j):
        if (i, j) in self.mines:
            self.game_over()
        else:
            count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    ni, nj = i + x, j + y
                    if 0 <= ni < self.height and 0 <= nj < self.width:
                        if not self.revealed[ni][nj]:
                            count += 1
            if count > 0:
                self.buttons[i][j].config(text=str(count))
                self.revealed[i][j] = True
            else:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        ni, nj = i + x, j + y
                        if 0 <= ni < self.height and 0 <= nj < self.width:
                            if not self.revealed[ni][nj]:
                                self.click(ni, nj)

    def game_over(self):
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.mines:
                    self.buttons[i][j].config(text="X")
                else:
                    count = 0 
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            ni, nj = i + x, j + y
                            if 0 <= ni < self.height and 0 <= nj < self.width:
                                if not self.revealed[ni][nj]:
                                    count += 1
                    self.buttons[i][j].config(text=str(count))

    def run(self):
        for row in self.buttons:
            for button in row:
                button.config(relief="sunken")
        self.root.mainloop()

if __name__ == "__main__":
    game = Minesweeper()
    game.run()