from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        ran_choice = random.randint(1,6)
        if ran_choice == 1:
            new_car = Turtle(shape= 'square')
            new_car.shapesize(stretch_wid=1 , stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ran_ycor = random.randint(-250, 250)
            new_car.goto(300, ran_ycor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
