#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 15

Lattice paths.

The problem, as stated, asks for the number of possible paths between the
top-left to the bottom-right points of a grid. Only paths with movement
downwards and right are allowed. The solution asked for in the problem is that
of a 20x20 grid.

This is effectively the same as asking: For any number (x, y), how many
possible ways are there to reach (0, 0) by subtracting 1 from each member of
the pair individually? For (1, 1) the answer is obviously 2 -- we have the
sequences (1, 1) -> (0, 1) -> (0, 0) and (1, 1) -> (1, 0) -> (0, 0).

I have the suspicion that this problem is soluble analytically, but I'm not
sure how to go about it. However, if we define N(x, y) to be the number of
these sequences, we can say that N(x, y) = 2*N(x-1, y)*2*N(x, y-1) = 4*N(x-1,
y)*N(x,y-1). By combining this with the known fact that N(1, 1) = 2, we have a
definition which lends itself admirably to a recursive solution.

A couple important points for optimization:
    - N(x, y) = N(y, x)
    - We can maintain a dictionary of known values to avoid recomputations of
      common paths.
"""

known_path_lens = {(1,1): 2}

def path_id(x, y):
    return (x, y) if x < y else (y, x)

def path_len(x, y):
    pid = path_id(x, y)
    print pid

    if pid in known_path_lens:
        plen = known_path_lens[pid]
    else:
        plen = 1
        if x > 0:
            plen *= 2*path_len(x-1, y)
        if y > 0:
            plen *= 2*path_len(x, y-1)
        known_path_lens[pid] = plen
    return plen



if __name__ == "__main__":
    print path_len(20, 20)
