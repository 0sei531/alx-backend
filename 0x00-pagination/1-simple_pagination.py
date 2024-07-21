#!/usr/bin/env python3
"""
Description: Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size with
default value 10.

- You have to use this CSV file (same as the one presented at the top
  of the project)
- Use assert to verify that both arguments are integers greater than 0.
- Use index_range to find the correct indexes to paginate the dataset
  correctly and return the appropriate page of the dataset (i.e. the
  correct list of rows).
- If the input arguments are out of range for the dataset, an empty list
  should be returned.
"""

import csv
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE, newline='') as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]  # Skip header row
            except FileNotFoundError:
                print(f"Error: The file {self.DATA_FILE} was not found.")
                self.__dataset = []
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
                self.__dataset = []

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A list of rows from the dataset corresponding to the
                        requested page and page size.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)

        return self.dataset()[start:end]
