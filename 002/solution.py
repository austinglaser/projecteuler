#!/usr/bin/env python
"""

Usage:
    solution.py <limit>

Sum even fibonacci numbers less than <limit>
"""
import docopt

import numpy as np

def fibonacci_below(limit):
    fib_seq = []
    if limit > 1:
        fib_seq.append(1)
    if limit > 2:
        fib_seq.append(2)
    if limit > 3:
        next_elem = fib_seq[-1] + fib_seq[-2]
        while next_elem < limit:
            fib_seq.append(next_elem)
            next_elem = fib_seq[-1] + fib_seq[-2]
    return np.array(fib_seq)

if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    try:
        limit = int(args['<limit>'])
    except:
        raise docopt.DocoptExit('<limit> must be an integer')

    fibs = fibonacci_below(limit)
    even_fib_indices = np.arange(1,fibs.shape[0], 3)
    even_fibs = fibs[even_fib_indices]
    print even_fibs.sum()
