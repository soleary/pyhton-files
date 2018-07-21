#!/usr/bin/env python

import re

print("So .match() matches against the beginning of the string, so we can leave out the '^' to anchor it")
print("Note:  I'm not 100% sure this is *same* as '^', but it appears to work that way.")
pat1 = re.compile('bro')

with open('bros.txt', 'r') as f:
    for line in f:
        if pat1.match(line):
            print(line, end='')

print("\n.fullmatch() matches against the whole string, as if the supplied regex were anchored at each end.")
print("It's not quite like '^regex$', as '$' will match a newline chracter at the end of string, but .fullmatch()")
print("requires us to include the '\\n' in the regex.")
pat2 = re.compile('bro\n')

with open('bros.txt', 'r') as f:
    for line in f:
        if pat2.fullmatch(line):
            print(line, end='')

print("\n.search() will match anywhere in the supplied string, so if you only want to match at the beginning, you've got")
print("to anchor the patten in your regex.")
pat3 = re.compile('^bro')

with open('bros.txt', 'r') as f:
    for line in f:
        if pat3.search(line):
            print(line, end='')

print("\nThis will have to match a whole string, since it's anchored at both ends.  But '$' will match the end of a string or a newline")
print("followed by the end of the string, so we don't have to actually include the '\\n' in our regex.")
pat4 = re.compile('^bro$')

with open('bros.txt', 'r') as f:
    for line in f:
        if pat4.search(line):
            print(line, end='')

