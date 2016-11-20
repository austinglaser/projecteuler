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

if __name__ == "__main__":
    elems = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    perm = []
    perm_n = 999999

    while len(elems) > 0:
        subseq_n = math.factorial(len(elems) - 1)

        subseq = perm_n / subseq_n
        perm_n = perm_n % subseq_n

        perm.append(elems[subseq])
        del elems[subseq]

    print ''.join(perm)
