#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

"""
Solution to project euler problem 9.

Find pythagorean triplet of natural numbers a, b, and c.

Constraints:

    a^2 + b^2 == c^2
    a < b < c
    a + b + c == 1000
"""

import numpy as np


def triangle_sides_with_perimeter(perimeter):
    """
    Return a list of triplets, where each triplet could be values for the side
    of a triangle with the given perimeter
    """
    sides = []
    for side1 in range(1, perimeter + 2):
        perimeter_left = perimeter - side1
        for side2 in range(1, perimeter_left + 1):
            side3 = perimeter_left - side2
            if ((side1 + side2 > side3) and
                (side1 + side3 > side2) and
                (side2 + side3 > side1) and
                (side1 < side2) and (side2 < side3)):
                sides.append((side1, side2, side3))
    return sides


if __name__ == "__main__":
    sides = np.array(triangle_sides_with_perimeter(1000))
    side_squares = sides ** 2
    first_two_sum = np.sum(side_squares[:,0:2], axis=1)
    pythagorean_index = np.where(first_two_sum == side_squares[:,2])
    triplet = sides[pythagorean_index][0]
    print triplet
    print np.product(triplet)
