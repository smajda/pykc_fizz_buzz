#!/usr/bin/env python

import argparse


class FizzBuzz(object):

    def __init__(self, start=1, end=10):
        self.start, self.end = start, end

    @staticmethod
    def fizzbuzzify(num):
        if num == 0:
            return '0'
        fizzing = 'Fizz' if num % 3 == 0 else ''
        buzzing = 'Buzz' if num % 5 == 0 else ''
        return "{}{}".format(fizzing, buzzing) or str(num)

    def generate(self):
        for num in xrange(self.start, self.end):
            yield self.fizzbuzzify(num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FizzBuzz program.')
    parser.add_argument('--start', type=int, help='start of range', default=1)
    parser.add_argument('--end', type=int, help='end of range', default=101)
    args = parser.parse_args()
    start = args.start
    end = args.end

    fizz_buzz = FizzBuzz(start, end)
    print("\n".join(i for i in fizz_buzz.generate()))
