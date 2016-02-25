#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project euler prob 7.
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
    primes = np.array([])
    prime_max = 1
    while len(primes) < 10001:
        print primes
        prime_max *= 10
        primes = prime_numbers_upto(prime_max)
    print primes[10000]
