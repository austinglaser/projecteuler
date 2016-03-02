#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 10.

Sum of primes < 2,000,000
"""

import math
import numpy as np


def prime_numbers_upto(limit):
    is_prime = np.array([True]*(limit - 1))
    for c in np.arange(2, int(math.sqrt(limit)) + 1):
        if is_prime[c - 2]:
            is_prime[np.arange(c**2 - 2, limit - 1, c)] = False
    candidates = np.arange(2, limit + 1)
    return candidates[is_prime]


if __name__ == "__main__":
    print np.sum(prime_numbers_upto(2000000))
