import re

phone_number_re = re.compile(r''' 
                                        (\d{3}| \(\d{3}\))                        #area code
                                        [^0-9]                           #delimiter1
                                        (\d{3})                             #first 3 digits
                                        [^0-9]                            #delimiter2
                                        (\d{4})                             #last 4 digits
                                       ''', re.VERBOSE)

infile = open('/home/ubuntu/user.csv', 'r')

for line in infile:
    match = phone_number_re.search(line)
    if match:
        phone_number_re.sub(r'XXX-XXX-XXXX',line)
        print(line)