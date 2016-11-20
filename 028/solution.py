#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 28

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20 7  8  9  10 27
40 19 6  1  2  11 28
39 18 5  4  3  12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
"""

import math
import numpy as np

def corners(ring):
    return 16*(ring**2) + 4*ring + 4

def spiral(size):
    s = 1
    for i in range(1,size + 1):
        s += corners(i)
    return s

if __name__ == "__main__":
    print spiral(500)
