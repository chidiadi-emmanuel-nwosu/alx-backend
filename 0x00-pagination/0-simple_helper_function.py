#!/usr/bin/env python3
""" 0-simple_helper_function """
from typing import Union


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for pagination.

    Args:
    - page (int): The current page number. 1-indexed, i.e.,
                  the first page is page 1.
    - page_size (int): The number of items displayed on each page.

    Returns:
    - tuple: A tuple of size two containing the start index and end index.
             Represents the range of indexes to return in a list for the
             given pagination parameters.
    """

    start_index = (page - 1) * page_size
    end_index = start_index * page_size

    return start_index, end_index
