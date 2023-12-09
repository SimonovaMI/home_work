from random import random

time = 0
car_positions = []


def input_time_position():
    global time
    global car_positions
    time = 5
    car_positions = [1, 1, 1]


def output_result(car_position):
    print('-' * car_position)


def start_race():
    global time
    global car_positions
    while time:
        # decrease time
        time -= 1

        print('')

        for i in range(len(car_positions)):
            # move car
            if random() > 0.3:
                car_positions[i] += 1

            # draw car
            output_result(car_positions[i])


input_time_position()
start_race()
