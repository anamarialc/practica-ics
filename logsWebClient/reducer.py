#!/usr/bin/env python

import sys

current_key = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    key, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        print('Could not convert data to an integer.')

    if current_key == key:
        current_count += count
    else:
        if current_key:
            print('%s\t%d', current_key, current_count)
        current_count = count
        current_key = key

# Outputs the last key if needed!
if current_key == key:
    print('%s\t%d', (current_key, current_count))