#!/usr/bin/env python3
""" Basic annotations - element_length """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotate the below functions parameters and
        return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
