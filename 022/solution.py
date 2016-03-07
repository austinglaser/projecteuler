#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem 22
"""


def value(name):
    value= 0
    for c in name:
        value += (ord(c) + 1) - ord('A')
    return value


if __name__ == "__main__":
    with open('names.txt', 'r') as namefile:
        namestr = namefile.readlines()[0]
        names = sorted([name.strip('"') for name in namestr.split(',')])

    totalscore = 0
    for i, name in enumerate(names):
        score = value(name)*(i+1)
        totalscore += score
    print totalscore
