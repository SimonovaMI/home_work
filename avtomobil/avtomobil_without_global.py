from random import random


def go_race():
    time = 5
    car_positions = [1, 1, 1]

    def move_cars():
        for i, _ in enumerate(car_positions):
            if random() > 0.3:
                car_positions[i] += 1

    def run_step_of_race():
        nonlocal time
        time -= 1
        move_cars()

    while time:
        run_step_of_race()
        draw(time, car_positions)


def draw_car(time, car_position):
    print(time, '-' * car_position)


def draw(time, car_positions):
    print(time)
    for car_position in car_positions:
        draw_car(time, car_position)


go_race()
