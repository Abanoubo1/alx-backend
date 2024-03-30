x#!/usr/bin/env python3
"""
Module to define index_range function for pagination
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start index and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The size of each page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
