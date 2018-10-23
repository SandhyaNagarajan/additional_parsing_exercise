'''
I/P:This program takes the sample_apache.log as input
O/P: gives the count of i/p which accessed the server max times
'''


with open("source/simple_apache.log") as file:
    ip_hash = {}
    for line in file:
        ip, rest = line.split("- -")
        if ip not in ip_hash:
            ip_hash[ip] = 1
        else:
            ip_hash[ip] += 1
    print(ip_hash.items())
    sorted_ip = sorted(ip_hash.items(), key=lambda x: x[1],reverse=True)
    for ip in sorted_ip:
        if sorted_ip[ip][2] > 5:
