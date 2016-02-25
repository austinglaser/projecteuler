#!/usr/bin/env python
"""

Usage:
    solution.py <value>

Find the largest prime factor of <value>.
"""
import docopt

import numpy as np
import math

def prime_numbers_upto(limit):
    is_prime = np.array([True]*(limit - 1))
    for c in np.arange(2, int(math.sqrt(limit)) + 1):
        if is_prime[c - 2]:
            is_prime[np.arange(c**2 - 2, limit - 1, c)] = False
    candidates = np.arange(2, limit + 1)
    return candidates[is_prime]

if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    try:
        value = int(args['<value>'])
    except:
        raise docopt.DocoptExit('<value> must be an integer')

    primes = prime_numbers_upto(int(math.sqrt(value)))
    for candidate in primes[::-1]:
        if value % candidate == 0:
            print candidate
            exit()
