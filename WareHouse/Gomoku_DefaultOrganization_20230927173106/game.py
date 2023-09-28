'''
This file contains the Game class which manages the game logic and GUI.
'''
import tkinter as tk
from tkinter import messagebox
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku")
        self.board = Board(self.root)
        self.board.pack()
class Board(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=500, height=500, bg="green")  # Change background to green
        self.bind("<Button-1>", self.on_click)
        self.grid = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "black"
    def on_click(self, event):
        x, y = event.x, event.y
        row, col = y // 33, x // 33
        if self.grid[row][col] is None:
            self.draw_piece(row, col)
            self.check_winner(row, col)
            self.switch_player()
    def draw_piece(self, row, col):
        x, y = col * 33, row * 33
        color = "black" if self.current_player == "black" else "white"
        self.create_oval(x, y, x + 33, y + 33, fill=color)
        self.grid[row][col] = self.current_player
    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                new_row, new_col = row + i * dx, col + i * dy
                if 0 <= new_row < 15 and 0 <= new_col < 15 and self.grid[new_row][new_col] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                new_row, new_col = row - i * dx, col - i * dy
                if 0 <= new_row < 15 and 0 <= new_col < 15 and self.grid[new_row][new_col] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 5:
                self.show_winner()
    def show_winner(self):
        winner = "Black" if self.current_player == "black" else "White"
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_board()
    def reset_board(self):
        self.delete("all")
        self.grid = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "black"
    def switch_player(self):
        self.current_player = "white" if self.current_player == "black" else "black"