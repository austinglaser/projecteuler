#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 24
"""

import math

def fib(n):
    if n < 0:
        raise ValueError("Fibonacci numbers only defined for n >= 0")

    if n == 0 or n == 1:
        return n

    prev = 0
    curr  = 1
    i = 1

    while i < n:
        t = prev + curr
        prev = curr
        curr = t
        i += 1

    return curr

if __name__ == "__main__":

    prev_digits = 0
    count = 0
    firstpoint = (1,1)
    n = 0
    while len(str(fib(n))) < 1000:
            n += 1
    print n
