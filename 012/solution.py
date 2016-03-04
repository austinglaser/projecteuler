#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 12

Triangle number factors
"""


import math
import numpy as np
import collections

def prime_factors(number):
    max_divisor = int(math.sqrt(number))
    for d in range(max_divisor, 1, -1):
        if number % d == 0:
            return prime_factors(d) + prime_factors(number / d)
    return [number]


def n_divisors(n):
    pf = prime_factors(n)
    counts = np.array(collections.Counter(pf).values())
    return np.product(counts + 1)


if __name__ == "__main__":
    t = 0
    n = 1
    while n_divisors(t) < 500:
        t += n
        n += 1
    print t
