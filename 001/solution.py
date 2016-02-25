#!/usr/bin/env python
"""Project Euler problem 1 solution

Usage:
    solution.py <limit>

Finds the sum of multiples of 3 and 5 up to <limit>
"""
import docopt

import numpy as np

def sum_multiples_below(limit, factors=[3, 5]):
    total_sum = 0
    for n in range(limit):
        for factor in factors:
            if n % factor == 0:
                total_sum += n
                break
    return total_sum


if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    try:
        limit = int(args['<limit>'])
    except:
        raise docopt.DocoptExit("<limit> must be an integer")

    print sum_multiples_below(limit)
