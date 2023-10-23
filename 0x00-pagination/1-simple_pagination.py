#!/usr/bin/env python3
"""a simple pagination exercise"""


import csv
import math
from typing import List, Tuple


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
        """
        Retrieving a specific page of the dataset
        based on the provided page and page size.

        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: The list of baby name records for the specified page.

        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculating the start and end indexes for the given page and page size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
