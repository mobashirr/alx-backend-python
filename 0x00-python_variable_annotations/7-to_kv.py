#!/usr/bin/env python3

'''
to_key module
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return tuple of string k and v square'''
    com = (k, v ** 2)
    return com
