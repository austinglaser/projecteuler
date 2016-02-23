#!/usr/bin/env python
"""Project Euler problem 1 solution

Usage:
    p1.py <limit>

Finds the sum of multiples of 3 and 5 up to <limit>
"""
import docopt

import numpy as np

def sum_multiples_below(limit, factors=[3, 5]):
    total_sum = 0
    for factor in factors:
        top = limit / factor if limit % factor != 0 else limit / factor - 1
        pair_value = top + 1
        n_pairs = top / 2
        pair_sum = pair_value * n_pairs
        center_value = top / 2 + 1 if top % 2 != 0 else 0
        factor_sum = factor * (pair_sum + center_value)
        total_sum += factor_sum
    return total_sum


if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    try:
        limit = int(args['<limit>'])
    except:
        raise docopt.DocoptExit("<limit> must be an integer")

    print sum_multiples_below(limit)
