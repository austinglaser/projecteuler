#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 21
"""


import math


def proper_divisors(n):
    divisors = set()
    for i in range(1, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    divisors.remove(n)
    return divisors


if __name__ == "__main__":
    divisor_sums = {}
    pair_sums = 0
    for n in range(1,10001):
        n_sum = sum(proper_divisors(n))
        divisor_sums[n] = n_sum
        if n_sum in divisor_sums:
            if divisor_sums[n_sum] == n and n != n_sum:
                print 'found pair', n, n_sum
                pair_sums += n + n_sum
    print pair_sums
