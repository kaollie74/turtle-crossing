import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CAR_POSITION = (300, random.randint(-250, 250))


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.care_pace = STARTING_MOVE_DISTANCE

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.care_pace)

    def create_car(self):
        random_time_to_create_car = random.randint(1, 6)

        if random_time_to_create_car == 1:
            # CONFIGURE CAR
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            start_car_position = (300, random.randint(-250, 250))
            car.setposition(start_car_position)
            # ADD CAR TO LIST
            self.all_cars.append(car)

    def level_up(self):
        self.care_pace += MOVE_INCREMENT
