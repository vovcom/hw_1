#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
        if wall_is_above() and wall_is_on_the_left():
            #Bерхний левый угол
            while not wall_is_on_the_right() and not wall_is_beneath():
                move_right()
                move_down()
            pass
        elif wall_is_above() and wall_is_on_the_right():
            #Верхний правый угол
            while not wall_is_on_the_left() and not wall_is_beneath():
                move_left()
                move_down()
            pass
        elif wall_is_beneath() and wall_is_on_the_left():
            while not wall_is_on_the_right() and not wall_is_above():
                move_right()
                move_up()
            pass
        else:
            #Нижний правый угол
            while not wall_is_on_the_left() and not wall_is_above():
                move_left()
                move_up()
            pass


if __name__ == '__main__':
    run_tasks()