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

def divisors(n):
    ds = []
    for d in range(1,int(math.ceil(math.sqrt(n)))):
        if n % d == 0:
            ds.append(d)
            ds.append(n / d)
    return ds

if __name__ == "__main__":
    t = 0
    n = 1
    d = []
    while len(d) < 500:
        t += n
        n += 1
        d = divisors(t)
    print t
