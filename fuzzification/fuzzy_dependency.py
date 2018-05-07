import math

DISTANCE_NEAR = "Near"
DISTANCE_MEDIUM = "Medium"
DISTANCE_FAR = "Far"

RED = "Red"
LESS_RED = "Less_red"
GREEN = "Green"
LESS_GREEN = "Less_green"

FAST = "Fast"
MEDIUM = "Medium"
SLOW = "Slow"
STOP = "Stop"


# distance dependency
def distance_near_dependency(distance):
    if 0 <= distance <= 70:
        return 1.0
    if 70 < distance < 140:
        return (140 - distance) / 70.0
    return 0.0


def distance_medium_dependency(distance):
    if 70 <= distance < 130:
        return (distance - 70) / 60.0
    if 130 <= distance <= 150:
        return 1.0
    if 150 < distance <= 210:
        return (210 - distance) / 60.0
    return 0.0


def distance_far_dependency(distance):
    if 140 <= distance <= 210:
        return (distance - 140) / 70.0
    if distance >= 210:
        return 1.0
    return 0.0


# light dependency
def light_red_dependency(time):
    if time >= 6:
        return 1.0
    if 3 <= time <= 6:
        return (time - 3) / 3.0
    return 0.0


def light_less_red_dependency(time):
    if time <= 3:
        return 1.0
    if 3 <= time <= 6:
        return (6 - time) / 3.0
    return 0.0


def light_less_green_dependency(time):
    if 0 <= time <= 3:
        return 1.0
    if 3 <= time <= 6:
        return (6 - time) / 3.0
    return 0.0


def light_green_dependency(time):
    if time >= 6:
        return 1.0
    if 3 <= time <= 6:
        return (time - 3) / 3.0
    return 0.0


# speed dependency
def speed_stop_dependency(speed):
    if speed == 0:
        return 1.0
    if 0 < speed < 0.1:
        return (0.1 - speed) / 0.1
    return 0.0


def speed_slow_dependency(speed):
    if 0 <= speed <= 0.5:
        return speed / 0.5
    if 0.5 <= speed <= 1:
        return (1 - speed) / 0.5
    return 0.0


def speed_medium_dependency(speed):
    if 0.5 <= speed <= 1:
        return (speed - 0.5) / 0.5
    if 1 <= speed <= 1.5:
        return (1.5 - speed) / 0.5
    return 0


def speed_fast_dependency(speed):
    if speed >= 1.5:
        return 1.0
    if 1 <= speed <= 1.5:
        return (speed - 1) / 0.5
    return 0.0


# calculate distance dependency
def cal_distance_dependencies(distance):
    distance_dependencies = []
    if distance_near_dependency(distance) > 0:
        distance_dependencies.append((DISTANCE_NEAR, distance_near_dependency(distance)))
    if distance_medium_dependency(distance) > 0:
        distance_dependencies.append((DISTANCE_MEDIUM, distance_medium_dependency(distance)))
    if distance_far_dependency(distance) > 0:
        distance_dependencies.append((DISTANCE_FAR, distance_far_dependency(distance)))
    return distance_dependencies

# calculate light dependencies
def cal_light_dependencies(light_status):
    light_dependencies = []
    time = light_status[0]
    status = light_status[1]
    if status == 1:
        if light_green_dependency(time) > 0:
            light_dependencies.append((GREEN, light_green_dependency(time)))
        if light_less_green_dependency(time) > 0:
            light_dependencies.append((LESS_GREEN, light_less_green_dependency(time)))
    if status == 2:
        if light_red_dependency(time) > 0:
            light_dependencies.append((RED, light_red_dependency(time)))
        if light_less_red_dependency(time) > 0:
            light_dependencies.append((LESS_RED, light_less_red_dependency(time)))
    return light_dependencies
