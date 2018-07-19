#!/usr/bin/env python3

"""
Print a random quote from Call of Duty.
(Read by default from `quotes.txt`.)
"""

import random
import os
import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Prints a random quote '
                                             'from Call of Duty')
parser.add_argument('-u', '--utf8',
                    help='print pretty punctuation',
                    action='store_true')

parser.add_argument('-f', '--file',
                    help='read from selected file '
                         '(default: ./quotes.txt)')
args = parser.parse_args()

# Opening file:
if not args.file:
    this_script_dir = os.path.dirname(__file__)
    quotes_file = os.path.join(this_script_dir, 'quotes.txt')
else:
    quotes_file = args.file


# Since quotes.txt is only ~20Kb and we are parsing it every
# once in a while, we are cool with storing the whole file
# in memory.
with open(quotes_file, 'r') as f:
    quotes = f.read().splitlines()

# Selecting an index at random:
index = random.randint(0, len(quotes) - 1)

quote = quotes[index]

if args.utf8:
    # Replacing ASCII quotation marks with real UTF-8
    # double quotes and dashes with em-dashes.
    quote = quote.replace('\'', u'\u201C', 1)
    quote = quote.replace('\'', u'\u201D', 1)
    quote = quote.replace('-', u'\u2014', 1)

print(quote)
