#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 20
"""


def factorial(num, stop=1):
    if num < 0:
        raise ValueError("factorial only defined for positive integers")
    f = 1
    for n in range(stop, num + 1):
        f *= n
    return f


if __name__ == "__main__":
    f = factorial(100)
    digits = [int(c) for c in str(f)]
    print sum(digits)
