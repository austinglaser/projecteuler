#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem four.

Largest palindrome product of n digits

Usage:
    solution.py <digits>
"""
import docopt

import math
import numpy as np

def n_decimal_digits(value):
    return int(math.log(value, 10)) + 1


def is_n_decimal_digits(value, n):
    return n_decimal_digits(value) == n


def palindromes_between(min_value, max_value):
    max_digits = n_decimal_digits(max_value)
    palindromes_with_digits = [None]*max_digits
    palindromes_with_digits[0] = np.arange(0,10, 1,  dtype='i8')
    palindromes_with_digits[1] = np.arange(0,100,11, dtype='i8')
    for digits in range(3, max_digits + 1):
        seed_row = palindromes_with_digits[(digits - 2) - 1]
        palindromes_with_digits[digits - 1] = np.zeros(len(seed_row)*10, dtype='i8')
        current_row = palindromes_with_digits[digits - 1]
        i = 0
        for seed in seed_row:
            outer_ones = 10 ** (digits - 1) + 1
            for n in range(0, 10):
                value = seed * 10 + n * outer_ones
                current_row[i] = value
                i += 1

    palindromes = np.concatenate(palindromes_with_digits)
    palindromes = np.unique(palindromes)
    palindromes = palindromes[palindromes <= max_value]
    palindromes = palindromes[palindromes >= min_value]
    return palindromes


if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    try:
        digits = int(args['<digits>'])
    except:
        raise docopt.DocoptExit("'digits' must be a positive integer")
    if digits < 1:
        raise docopt.DocoptExit("'digits' must be a positive integer")

    largest_number = 10**(digits) - 1
    smallest_number = 10**(digits - 1)
    largest_product = largest_number ** 2
    smallest_product = smallest_number ** 2

    candidates = palindromes_between(smallest_product, largest_product)[::-1]
    for candidate in candidates:
        factor = largest_number
        while is_n_decimal_digits(factor, digits) and n_decimal_digits(candidate / factor) <= digits:
            if candidate % factor == 0:
                cofactor = candidate/factor
                print "{p} is {f} * {c}".format(p=candidate, f=factor, c=cofactor)
                exit(0)
            factor -= 1

    print "wut"
