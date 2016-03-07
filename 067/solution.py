#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem 67 (problem 18 on steroids).
"""


if __name__ == "__main__":
    with open('triangle.txt') as triangle_file:
        triangle = []
        for line in triangle_file.readlines():
            numbers = [int(n) for n in line.split(' ')]
            triangle.append(numbers)
    while len(triangle) > 1:
        last_row = triangle[-1]
        second_to_last_row = triangle[-2]
        for i in range(len(second_to_last_row)):
            elem_pair = last_row[i:i+2]
            second_to_last_row[i] += max(elem_pair)
        del triangle[-1]
    print triangle[0][0]
