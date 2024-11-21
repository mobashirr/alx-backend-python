#!/usr/bin/env python3

'''
element lenght func
'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return list of lenght of given list'''
    return [(i, len(i)) for i in lst]
