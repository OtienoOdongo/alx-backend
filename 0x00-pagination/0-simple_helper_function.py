#!/usr/bin/env python3
"""
a helper function for Calculating
pagination parameter of a page_size
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculating the start and end indexes for the given page and page size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
