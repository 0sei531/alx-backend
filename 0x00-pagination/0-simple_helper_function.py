#!/usr/bin/env python3
"""
Description: Write a function named index_range that takes
two integer arguments page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the range
of indexes to return in a list for those particular
pagination parameters.

Page numbers are 1-indexed, i.e., the first page is page 1.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the pagination start index and end index.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    assert page > 0, "Page number should be greater than 0."
    assert page_size > 0, "Page size should be greater than 0."

    start_index = page_size * (page - 1)
    end_index = page_size * page

    return (start_index, end_index)
