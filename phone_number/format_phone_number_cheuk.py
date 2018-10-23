#!/usr/bin/python

import re

phone_number_re = re.compile(r'(\d{3})[^0-9]*(\d{3})[^0-9]*(\d{4})')

numbers = []

infile = open('source/phone_number_different_formats.txt', 'r')

for line in infile:
    match = phone_number_re.search(line)
    if match:
        phone_no = "-".join([match.groups()[0],match.groups()[1],match.groups()[2]])
        numbers.append(phone_no)

infile.close()

print(numbers)