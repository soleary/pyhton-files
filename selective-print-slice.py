#!/usr/bin/env python

with open('bros.txt', 'r') as f:
    for line in f:
        if line[:2] == 'br':
            print(line, end='')

