#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Austin Glaser <austin@boulderes.com>
#
# Distributed under terms of the MIT license.

class DecimalPalindromes(object):

    def __init__(self):
        self.cache = {}

    def ofLen(self, n):
        assert(n >= 0)

        if n == 0:
            yield ""
        elif n in self.cache:
            for pal in self.cache[n]:
                yield pal
        else:
            self.cache[n] = []
            for digit in range(10):
                if (n == 1):
                    pal = str(digit)
                    self.cache[n].append(pal)
                    yield pal
                else:
                    for subPal in self.ofLen(n - 2):
                        pal = str(digit) + subPal + str(digit)
                        self.cache[n].append(pal)
                        yield pal

    def ofLenUpto(self, n):
        for length in range(1, n + 1):
            for decPal in self.ofLen(length):
                yield decPal

def isBinaryPalindrome(number):
    binRep = bin(number)[2:]
    checkLen = len(binRep) / 2
    suffixReversed = binRep[-1:-(checkLen + 1):-1]
    return binRep.startswith(suffixReversed)

if __name__ == "__main__":
    pals = DecimalPalindromes()
    count = 0
    for decPalStr in pals.ofLenUpto(7):
        decPal = int(decPalStr)
        if isBinaryPalindrome(decPal):
            print decPal, bin(decPal)
            count += decPal
    print count

