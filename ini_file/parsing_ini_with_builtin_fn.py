#! /usr/bin/var python
with open('source/sample.ini') as file:
    cur_parent_key = "-"
    dict1 = {}
    for line in file:
        line = line.strip()
        if len(line) == 0 or line[0] == "#":
            continue
        if line.startswith("[") and line.endswith("]"):
            current_parent_key=line[1:-1]
            dict1[current_parent_key]={}
        elif line.count("=") == 1:
            key , value = line.split("=")
            dict1[current_parent_key][key.strip()] = value.strip()

    print(dict1)