from random import randint
from .Calc import Calc
from .Input import Input
from .Timing import Timing


def get_exercise(index):
    x = randint(0, 100)
    y = randint(0, 100)
    print(f"{index}:    {x} + {y} = ")
    return [x, y]


def get_calculation(calc, x, y):
    return calc.addition_int(x, y)


def get_input(input):
    return int(input.get_result_input())


def validate(calc, calculation, user_input):
    return calc.validate_result(calculation, user_input)


def run_controller():
    calc = Calc()
    input = Input()
    timing = Timing()

    timing.start()
    
    for x in range(0, 10):
        exercise = get_exercise(x+1)
        calculation = get_calculation(calc, exercise[0], exercise[1])
        user_input = get_input(input)
        result = validate(calc, calculation, user_input)
        print(result)
    
    timing.stop()
    measured_time = round(timing.get_measured_time(), 2)
    print(f"Made it in: {measured_time} seconds")
