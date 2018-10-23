#! usr/bin/var python
file = open("apache.log", 'r')
log_data = file.readlines()
file.close()
result = {}

for entry in log_data:
    ip_data = entry.split(" ")
    if ip_data[0] not in result:
        result[ip_data[0]] = 1
    else:
        result[ip_data[0]] +=1
sorted_result = sorted(result.items(),key = lambda x: x[1],reverse=True)
for i in range(10):
    print(str(sorted_result[i][1]) + "   " + str(sorted_result[i][0]))