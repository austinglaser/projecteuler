#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Problem 6 solution.
"""

import numpy as np


if __name__ == "__main__":
    numbers = np.arange(1,101)
    sum_of_squares = sum(numbers**2)
    square_of_sums = sum(numbers)**2
    print square_of_sums - sum_of_squares
