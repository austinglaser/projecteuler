#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 12

Triangle number factors
"""


import math

def n_divisors(n):
    ds = 0
    for d in range(1,int(math.ceil(math.sqrt(n)))):
        if n % d == 0:
            ds += 2
    return ds

if __name__ == "__main__":
    t = 0
    n = 1
    d = 0
    while d < 500:
        t += n
        n += 1
        d = n_divisors(t)
    print t
