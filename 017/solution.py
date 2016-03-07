#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem 17.
"""

if __name__ == "__main__":
    digit_strs = ['Zero', 'One',    'Two',    'Three',    'Four',     'Five',    'Six',     'Seven',     'Eight',    'Nine']
    tens_strs  = ['',     'Ten',    'Twenty', 'Thirty',   'Forty',    'Fifty',   'Sixty',   'Seventy',   'Eighty',   'Ninety',
                  '',     'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    count = 0
    for n in range(1, 1001):
        ones = digit_strs[n % 10]

        if n % 10 == 0:
            tens = tens_strs[(n % 100) / 10]
        elif n % 100 < 20:
            tens = tens_strs[n % 100]
        else:
            tens = tens_strs[(n % 100) / 10] + ones

        hundreds = digit_strs[(n % 1000) / 100] + 'Hundred'

        if n < 10:
            numstr = ones
        elif n < 100:
            numstr = tens
        elif n < 1000:
            if n % 100 == 0:
                numstr = hundreds
            else:
                numstr = hundreds + 'And' + tens
        else:
            numstr = 'OneThousand'

        count += len(numstr)
        print numstr
    print count
