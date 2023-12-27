#!/usr/bin/env python3
""" 1-simple_pagination """
import csv
import math
from typing import List


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
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data based on page number and page size
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end]
