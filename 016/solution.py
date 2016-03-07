#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem 16.
"""

if __name__ == "__main__":
    s = 0
    for c in str(2**1000):
        s += int(c)
    print s
