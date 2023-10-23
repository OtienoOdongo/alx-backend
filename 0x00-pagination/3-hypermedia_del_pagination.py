#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self,
        start_index: int = None,
        page_size: int = 10
    ) -> Dict:
        """
        Getting a hypermedia page from the indexed dataset.

        Args:
            start_index (int): 
            The starting index. Defaults to None.
            page_size (int):
            The number of items per page. Defaults to 10.

        Returns:
            Dict: 
            A dictionary containing index, next_index, page_size, and data.
        """
        assert 0 <= start_index < len(self.dataset())

        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        i = start_index

        while len(indexed_page) < page_size and i < len(self.dataset()):
            if i in indexed_dataset:
                indexed_page[i] = indexed_dataset[i]
                i += 1

        page = list(indexed_page.values())
        page_indices = indexed_page.keys()

        return {
            'index': start_index,
            'next_index': i,
            'page_size': len(page),
            'data': page
        }
