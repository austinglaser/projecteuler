#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 99
"""

import math
import numpy as np

if __name__ == "__main__":
    base_exp = np.loadtxt('p099_base_exp.txt', delimiter=',')

    numbers = base_exp[:,1] * np.log(base_exp[:,0])

    print np.argmax(numbers) + 1
