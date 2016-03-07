#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Project Euler problem 19.
"""

class Day(object):
    month_lens = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    weekday_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, weekday, day, month, year):
        self.weekday = self.weekday_names.index(weekday)
        self.day     = day - 1
        self.month   = self.month_names.index(month)
        self.year    = year

    def is_sunday(self):
        return self.weekday == 6


    def is_first_of_month(self):
        return self.day == 0


    def is_february(self):
        return self.month == 1


    def is_leap_year(self):
        is_century = self.year % 100 == 0
        is_400 = self.year % 400 == 0
        is_4 = self.year % 4 == 0
        return is_400 or ((not is_century) and is_4)

    def become_tomorrow(self):
        self.weekday = (self.weekday + 1) % 7

        days_in_month = self.month_lens[self.month]
        if self.is_february() and self.is_leap_year():
            days_in_month += 1
        self.day = (self.day + 1) % days_in_month

        if self.day == 0:
            self.month = (self.month + 1) % 12

        if self.month == 0 and self.day == 0:
            self.year += 1

    def __str__(self):
        return '{w}, {d:2d} {m}, {y}'.format(w=self.weekday_names[self.weekday],
                                             d=self.day + 1,
                                             m=self.month_names[self.month],
                                             y=self.year)


    def __repr__(self):
        return 'Day({w}, {d}, {m}, {y})'.format(w=self.weekday_names[self.weekday],
                                                d=self.day + 1,
                                                m=self.month_names[self.month],
                                                y=self.year)


if __name__ == "__main__":
    d = Day('Tue', 1, 'Jan', 1901)
    count = 0
    while d.year < 2001:
        if d.is_first_of_month() and d.is_sunday():
            count += 1
        d.become_tomorrow()
    print count
