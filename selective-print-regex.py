#!/usr/bin/env python

import re

print("So .match() matches against the beginning of the string, so we can leave out the '^' to anchor it")
print("Note:  I'm not 100% sure this is *same* as '^', but it appears to work that way.")
pat1 = re.compile('bro')

with open('bros.txt', 'r') as f:
    for line in f:
        if pat1.match(line):
            print(line, end='')

