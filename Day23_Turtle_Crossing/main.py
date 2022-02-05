import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")

# Generate cars
cars = []

for i in range(5):
    car = CarManager(player.level)
    cars.append(car)

game_is_on = True
cont_car_add = 0
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cont_car_add += 1
    # Move the cars
    for car in cars:
        car.move_car()
    # Level up
    if player.finish_line():
        player.up_level()
        scoreboard.level_up_scoreboard()
        for car in cars:
            car.level_up()

    #Increment number of cars after 6 loops
    if cont_car_add == 6:
        cont_car_add = 0
        for _ in range(player.level//2+1):
            car_temp = CarManager(player.level)
            cars.append(car_temp)


    # Detect collision of payer with any car:
    for car in cars:
        if car.distance(player) < 20:
            player.color("red")
            screen.update()
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
