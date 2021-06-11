from turtle import Turtle


class Dashboard:
    score = 0
    score_board = Turtle()
    game_over_board = Turtle()

    def __init__(self):
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score_board.goto(x=-170, y=250)

        self.game_over_board.penup()
        self.game_over_board.hideturtle()

        self.refresh_score()

    def update_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.score_board.clear()
        self.score_board.write(arg=f"Score : {self.score}", font=("Arial", 24, "normal"), align="center")

    def game_over(self):
        self.game_over_board.write(arg="Game Over !", font=("Arial", 24, "normal"), align="center")
