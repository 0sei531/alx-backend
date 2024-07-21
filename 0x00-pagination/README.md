# Pagination Project

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Simple Helper Function](#simple-helper-function)
  - [Simple Pagination](#simple-pagination)
  - [Hypermedia Pagination](#hypermedia-pagination)
  - [Deletion-Resilient Hypermedia Pagination](#deletion-resilient-hypermedia-pagination)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates various pagination techniques for handling large datasets. It includes implementations for simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- `Popular_Baby_Names.csv` dataset file

## Project Structu
- `README.md`: This file, containing information about the project.
- `index_range.py`: Contains the `index_range` function.
- `simple_pagination.py`: Contains the `Server` class with simple pagination.
- `hypermedia_pagination.py`: Extends `Server` class with hypermedia pagination.
- `deletion_resilient_pagination.py`: Extends `Server` class with deletion-resilient hypermedia pagination.
- `Popular_Baby_Names.csv`: Dataset used for pagination.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/alx-backend.git
    cd alx-backend/0x00-pagination
    ```

2. Ensure you have Python 3.7 installed. You can check your Python version with:

    ```bash
    python3 --version
    ```

3. Place the `Popular_Baby_Names.csv` file in the project directory.

## Usage

### Simple Helper Function

The `index_range` function calculates the start and end indices for pagination.

```python
from index_range import index_range

page = 1
page_size = 10
start, end = index_range(page, page_size)
print(f"Start index: {start}, End index: {end}")
re
