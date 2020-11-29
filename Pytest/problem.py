#!/usr/bin/env python3

from mysum import mysum

def sumIntegers():
    assert mysum([0, 1, 2, 3, 4]) == 10

def sumFloats():
    assert mysum([0.0, 1.0, 2.0, 3.0, 4.0]) == 10.0

def sumNothing():
    assert mysum([]) == 0
