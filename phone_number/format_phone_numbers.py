'''
I/P: This program takes the file phone_number_different_formats.txt as input
eg:
408 - 123 - 4576
(408) - 885 - 1523
408.333.1234
408-666-5623
876-540 6578
408 353 9514
408 667 1234
O/P: formats the phone numbers into xxx-xxx-xxxx and prints the result
'''
import re

phone_number_re = re.compile(r''' 
                                        (\d{3}| \(\d{3}\))                        #area code
                                        [^0-9]                           #delimiter1
                                        (\d{3})                             #first 3 digits
                                        [^0-9]                            #delimiter2
                                        (\d{4})                             #last 4 digits
                                       ''', re.VERBOSE)
numbers = []
with open("source/phone_number_different_formats.txt") as file:
    for line in file:
        for group in phone_number_re.findall(line):
            phone_no = "-".join([group[1],group[3],group[5]])
            numbers.append(phone_no)
    print(numbers)