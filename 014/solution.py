#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 14

Long Sequence
"""

known_seqs = dict()

def sequence_length(n):
    n_orig = n
    s_l = 1
    while n > 1:
        if n in known_seqs:
            s_l += known_seqs[n] - 1
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        s_l += 1
    known_seqs[n_orig] = s_l
    return s_l


if __name__ == "__main__":
    max_length = 0
    max_n = 0
    for n in range(1,1000000):
        l = sequence_length(n)
        if l > max_length:
            max_length = l
            max_n = n
    print max_n, max_length
