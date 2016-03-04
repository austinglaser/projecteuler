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

Try1:

This doesn't work at all. So let's limit to square grid sizes, and try to come
up with a recursive (or at least iterative) formula for them.

Specifically, we try to define N(x, x) in terms of N(x-1, x-1). This is pretty straightforward
"""

known_path_lens = {
                    (1,1): 2,
                    (0,1): 1
                  }

def path_id(x, y):
    return (x, y) if x < y else (y, x)

def path_len(x, y):
    pid = path_id(x, y)
    print pid
    print known_path_lens
    print

    if pid in known_path_lens:
        plen = known_path_lens[pid]
    else:
        if x == 0:
            plen = y
        elif y == 0:
            plen = x
        else:
            plen = path_len(x-1, y) * path_len(y, x-1)
        known_path_lens[pid] = plen
    return plen



if __name__ == "__main__":
    print path_len(2, 2)
