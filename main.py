import turtle
from turtle import Screen
from background import Background
from player import Player
from vehicle import Vehicle
from scorecard import Scorecard
import time

turtle.colormode(255)

screen = Screen()

screen.tracer(0)
background = Background()

player = Player()

screen.listen()
screen.onkeypress(player.player_move, "Up")

vehicles = []

background.welcome()
scorecard = Scorecard()


def vehicle_creation():
    new_vehicle = Vehicle()
    new_vehicle.create_vehicle()
    new_vehicle.color(new_vehicle.vehicle_color())
    vehicles.append(new_vehicle)


def game_body():

    background.clear()
    scorecard.clear()
    scorecard.level = 0

    for vehicle in vehicles:
        vehicle.reset()
        vehicle.hideturtle()
        vehicle.penup()
        vehicle.clear()

    player.reset()
    player.create_player()
    player.player_move()

    counter = 0
    delay = 0.075
    vehicle_spawn_rate = 18  # Fewer means more vehicles will spawn in a given time

    is_game_on = True

    while is_game_on:

        counter += 1
        time.sleep(delay)
        scorecard.display_level()

        if counter % vehicle_spawn_rate == 0:
            vehicle_creation()

        for vehicle in vehicles:

            vehicle.vehicle_move()

            if player.distance(vehicle) < 30:
                is_game_on = False

            if vehicle.xcor() < -300:
                vehicle.hideturtle()
                vehicles.remove(vehicle)

        if player.at_finish_line():
            scorecard.count_level()

            player.goto(player.start_pos)
            delay -= 0.005
            delay = max(0.013, delay)

            vehicle_spawn_rate -= 1
            vehicle_spawn_rate = max(12, vehicle_spawn_rate)

        screen.update()

    scorecard.high_score()
    background.game_over()


screen.onkeypress(game_body, "q")
screen.onkeypress(background.close_app, "e")


screen.exitonclick()
