#!/usr/bin/env python

print("First time\n")
with open('bros.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

print("\nSecond time\n")
with open('bros.txt', 'r') as f:
    for line in f:
        print(line, end='')
