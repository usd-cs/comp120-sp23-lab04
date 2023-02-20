"""
Module: comp120_lab04

Practice using recursion to deal with nested lists.
"""
from typing import Union

def uniques(obj: Union[int, list]) -> list[int]:
    """Returns a non-nested list of unique integers in <obj> (i.e. list with
    no repeats).

    >>> uniques(5)
    [5]
    """
    if isinstance(obj, int):
        # base case
        return [obj]

    else:
        # recursive case
        s = []
        for item in obj:
            s.extend(uniques(item))
        return s


def nested_list_contains(obj: Union[int, list]) -> bool:
    """Return whether the given item appears in <objL.

    Note that if <obj> is an integer, this function checks whether <item> is
    equal to <obj>.
    """

    pass # remove this line and replace it with your implementation
