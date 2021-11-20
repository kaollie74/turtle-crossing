import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Turtle Crossing")

# Player/Turtle
playa = Player()

# Cars
car_manager = CarManager()

# ScoreBoard
scoreboard = Scoreboard()

# event listeners
screen.listen()
screen.onkey(playa.move_up, "Up")
screen.onkey(playa.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create car
    car_manager.create_car()
    car_manager.car_move()

    # detect collision with car(s)
    for car in car_manager.all_cars:
        if car.distance(playa) < 25:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if playa.is_at_finish_line():
        playa.start_position()
        car_manager.level_up()
        scoreboard.increment_score()

screen.exitonclick()
