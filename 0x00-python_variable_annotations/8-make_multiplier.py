#!/usr/bin/env python3

'''

'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return func that mul any given number by multiplier'''
    def func(arg: float) -> float:
        return multiplier * arg
    return func
