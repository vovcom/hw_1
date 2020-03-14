#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while True:
        if wall_is_on_the_left() or not wall_is_above():
            break
        move_left()
    while True:
        if wall_is_on_the_right() or not wall_is_above():
            break
        move_right()

    while not wall_is_above():
        move_up()

    while not wall_is_on_the_left():
        move_left()
    pass
if __name__ == '__main__':
    run_tasks()
