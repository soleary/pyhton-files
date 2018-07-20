#!/usr/bin/env python

import re

pat = re.compile('^br')

with open('bros.txt', 'r') as f:
    for line in f:
        if pat.match(line):
            print(line, end='')

