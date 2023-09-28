'''
Pong Game
'''
import tkinter as tk
class PongGame:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 800
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='black')
        self.canvas.pack()
        self.ball = self.canvas.create_oval(0, 0, 20, 20, fill='white')
        self.paddle = self.canvas.create_rectangle(0, 0, 10, 60, fill='white')
        self.canvas.bind_all('<KeyPress-Up>', self.move_paddle_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_paddle_down)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
        self.x_speed = 1
        self.y_speed = 1
        self.paddle_speed = 5
        self.game_started = False
    def move_ball(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        ball_pos = self.canvas.coords(self.ball)
        if ball_pos[1] <= 0 or ball_pos[3] >= self.canvas_height:
            self.y_speed *= -1
        if self.check_collision(ball_pos, self.paddle):
            self.x_speed *= -1
        if ball_pos[0] <= 0:
            self.game_over()
        if ball_pos[2] >= self.canvas_width:
            self.game_over()
        if self.game_started:
            self.canvas.after(10, self.move_ball)
    def move_paddle_up(self, event):
        self.canvas.move(self.paddle, 0, -self.paddle_speed)
    def move_paddle_down(self, event):
        self.canvas.move(self.paddle, 0, self.paddle_speed)
    def start_game(self, event):
        self.game_started = True
        self.move_ball()
    def check_collision(self, item1, item2):
        x_collision = item1[2] >= item2[0] and item1[0] <= item2[2]
        y_collision = item1[3] >= item2[1] and item1[1] <= item2[3]
        return x_collision and y_collision
    def game_over(self):
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2, text='Game Over', fill='white', font=('Arial', 20), anchor='center')
        self.game_started = False
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Pong Game')
    game = PongGame(root)
    root.mainloop()