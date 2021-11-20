from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    # Constructor
    def __init__(self):
        # Call Constructor of Turtle class
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color("white")
        self.setheading(90)
        self.start_position()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.back(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def start_position(self):
        self.goto(STARTING_POSITION)
