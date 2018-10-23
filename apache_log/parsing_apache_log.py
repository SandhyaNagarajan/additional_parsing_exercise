'''
This program parses the logfile simple_apache.log and
prints the count of ip which refers to itself(127.0.0.1) and
to that of others
'''


with open("source/simple_apache.log") as log:
    count_self = 0
    count_others = 0
    for line in log:
        ip,rest = line.split("- -")
        if ip.strip() == "127.0.0.1":
            count_self += 1
        else:
            count_others += 1
    print(count_self,count_others)