#! /usr/bin/env python 
import re
# regular expression for parent key
key_1 = re.compile("\[(\w*)\]")
dict1 = {}
#regular expression for child key and value:
key_val = re.compile('''(\w*)"						# key
					 	\s*
					 	=							# delimiter
					 	\s*							
					 	(\w*)''',re.VERBOSE)		#value
# read the ini file

# read the ini file
try:
	f = open('source/sample.ini','r')
	for line in f.readlines():
		if not line.isspace():
			print(line)
			for parent_key in key_1.findall(line):
				dict1[parent_key] = {}
				'''for key_value_match in key_val.search(line):
						k, v = key_value_match.group[1], key_value_match.group[2]
						print(k,v)
						dict1[parent_key][k]=v'''






finally:
	f.close()

