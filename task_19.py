#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    isBallWithoutExit = True
    move_right(4)
    if not wall_is_on_the_right():
        isBallWithoutExit = False
        move_right()
    else:
        move_left(8)
        if not wall_is_on_the_left():
            isBallWithoutExit = False
            move_left()

    if isBallWithoutExit:
        move_right(8)
    else:
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()


    pass


if __name__ == '__main__':
    run_tasks()
