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


def palindromes_less_than(max_value):
    max_digits = n_decimal_digits(max_value)
    palindromes_with_digits = [None]*max_digits
    palindromes_with_digits[0] = np.arange(0,10, 1,  dtype='i4')
    palindromes_with_digits[1] = np.arange(0,100,11, dtype='i4')
    for digits in range(3, max_digits + 1):
        seed_row = palindromes_with_digits[(digits - 2) - 1]
        palindromes_with_digits[digits - 1] = np.zeros(len(seed_row)*9, dtype='i4')
        current_row = palindromes_with_digits[digits - 1]
        i = 0
        for seed in seed_row:
            outer_ones = 10 ** (digits - 1) + 1
            for n in range(1, 10):
                value = seed * 10 + n * outer_ones
                current_row[i] = value
                i += 1
    palindromes = np.concatenate(palindromes_with_digits)
    palindromes = np.unique(palindromes[palindromes <= max_value])
    palindromes = palindromes[1:]
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
    largest_product = largest_number ** 2

    candidates = palindromes_less_than(largest_product)[::-1]
    print candidates
