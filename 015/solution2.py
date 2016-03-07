#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Combinatorial solution
"""

def factorial(num):
    if num < 0:
        raise ValueError("factorial only defined for positive integers")
    f = 1
    for n in range(1, num + 1):
        f *= n
    return f

def npickk(n, k):
    return factorial(n) / factorial(n - k)

def nchoosek(n, k):
    return npickk(n, k) / factorial(k)

if __name__ == "__main__":
    print nchoosek(40, 20)
