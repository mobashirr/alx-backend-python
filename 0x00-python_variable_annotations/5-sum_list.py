#!/usr/bin/env python3

'''
func sum_list
'''


from typing import List

def sum_list(input_list: List[float]) -> float:
    sum = 0.0
    for ele in input_list:
        sum += ele
    return sum
