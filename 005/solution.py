#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import math
import numpy as np


def prime_factors(number):
    max_divisor = int(math.sqrt(number))
    for d in range(max_divisor, 1, -1):
        if number % d == 0:
            return prime_factors(d) + prime_factors(number / d)
    return [number]


if __name__ == "__main__":
    max_factor = 20
    divisors = range(2, max_factor + 1)
    necessary_factors = np.zeros(max_factor + 1, dtype='i4')
    for d in divisors:
        factor_counts = np.bincount(prime_factors(d), minlength = max_factor + 1)
        larger_count = factor_counts > necessary_factors
        necessary_factors[larger_count] = factor_counts[larger_count]

    product = 1
    for factor, count in enumerate(necessary_factors):
        if count > 0:
            product *= factor**count
    print product
