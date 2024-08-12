#!/usr/bin/env python3
""" Basic annotations - make_multiplier """
from typing import List, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes a float multiplier
        as argument and returns a function that multiplies a float by
        multiplier.
    """
    def multn(n: float):
        return n * multiplier
    return multn
