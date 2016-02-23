#!/usr/bin/env python
"""Project Euler problem 1 solution

Usage:
    p1.py <limit>

Finds the sum of multiples of 3 and 5 up to <limit>
"""
import docopt

import numpy as np

def sum_three_five_multiples_below(limit):
    three_multiples = np.arange(3, limit, step=3)
    five_multiples = np.arange(5, limit, step=5)
    threes_sum = three_multiples.sum()
    fives_sum = five_multiples.sum()
    total_sum = threes_sum + fives_sum
    return total_sum

if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    try:
        limit = int(args['<limit>'])
    except:
        raise docopt.DocoptExit("<limit> must be an integer")

    print sum_three_five_multiples_below(limit)
