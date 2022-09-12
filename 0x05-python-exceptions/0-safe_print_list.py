ements of a list."""


def safe_print_list(my_list#!/usr/bin/python3

"""a function that prints x el=[], x=0):
    count = 0
    try:
        for index in range(0, x):
            print(my_list[index], end='')
            count += 1
    except Exception:
        error = Exception
    finally:
        print('')
    return count
