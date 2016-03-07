#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 23
"""


import math
import numpy as np


def proper_divisors(n):
    divisors = set()
    for i in range(1, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    divisors.remove(n)
    return divisors


if __name__ == "__main__":
    abundant_numbers = []
    for n in range(1, 28124):
        if sum(proper_divisors(n)) > n:
            abundant_numbers.append(n)
    abundant_numbers = np.array(abundant_numbers)

    abundant_number_sums = np.array([False]*(28123*2 -1), dtype=bool)
    for i, a in enumerate(abundant_numbers):
        abundant_number_sums[abundant_numbers[i:] + a] = True
    results = np.arange(1, 28124)
    result_idx = np.logical_not(abundant_number_sums)[:len(results)]
    print np.sum(results[result_idx])

