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

import numpy as np


if __name__ == "__main__":
    elems = sorted(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    for i in range(1000000):
        k = None
        for i in range(len(elems) - 2, -1, -1):
            if elems[i] < elems[i + 1]:
                k = i
                break
        if k is None:
            break

        l = None
        for i in range(len(elems) - 1, k, -1):
            if elems[k] < elems[i]:
                l = i
                break

        tmp = elems[k]
        elems[k] = elems[l]
        elems[l] = tmp

        elems[k+1:] = reversed(elems[k+1:])

    print ''.join(elems)
