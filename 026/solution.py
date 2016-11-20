#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 26
"""

import math

if __name__ == "__main__":
    max_cycle       = 0
    max_cycle_digit = None
    for d in range (2,1000):
        sequence = []
        remainder = 1
        cycle = None

        while True:
            oldr = remainder
            remainder *= 10
            digit = remainder / d
            state = (digit, oldr)

            if remainder == 0 and digit == 0:
                break

            if state in sequence:
                cycle = state
                break

            remainder -= d * digit
            sequence.append(state)


        if cycle:
            cycle_len = len(sequence) - sequence.index(cycle)
            if cycle_len > max_cycle:
                max_cycle = cycle_len
                max_cycle_digit = d
    print max_cycle_digit

