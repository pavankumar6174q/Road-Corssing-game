import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)




player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.update_score()

screen.listen()

screen.onkey(player.go_up , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1) 
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


    #detecting the car
    for car in car_manager.all_cars:
        if car.distance(player) <25:
            scoreboard.game_over()
            game_is_on = False

    #detect the successful crossing
    if player.at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_lvl()
        






screen.exitonclick()