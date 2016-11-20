#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 27
"""

import math
import numpy as np

def is_prime(n):
    if n < 0:
        return False

    limit = int(math.sqrt(n)) + 1

    for i in np.arange(2, limit):
        if n % i == 0:
            return False
    return True

def prime_numbers_upto(limit):
    can_be_prime = np.array([True]*(limit - 1))
    for c in np.arange(2, int(math.sqrt(limit)) + 1):
        if can_be_prime[c - 2]:
            can_be_prime[np.arange(c**2 - 2, limit - 1, c)] = False
    candidates = np.arange(2, limit + 1)
    return candidates[can_be_prime]

if __name__ == "__main__":
    primes = prime_numbers_upto(1000)

    pairs = []
    for p in primes:
        for i in range(-999, 1000):
            pairs.append((i,p))

    best = None
    best_count = 0
    for p in pairs:
        n = 1
        while True:
            v = n ** 2 + n * p[0] + p[1]
            if not is_prime(v):
                if n > best_count:
                    best_count = n
                    best = p
                break
            n += 1
    #print best, best_count
    print best[0]*best[1]
