#!/usr/bin/env python3

'''
sum_mized_list this annotaed function should accept list of floats or intergers
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''take a list of int or floats and return the sum'''
    acc = 0.0

    for ele in mxd_lst:
        acc += ele
    return acc
