#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem 22
"""


if __name__ == "__main__":
    with open('names.txt', 'r') as namefile:
        namestr = namefile.readlines()[0]
        names = [name.strip('"') for name in namestr.split(',')]
    print names
