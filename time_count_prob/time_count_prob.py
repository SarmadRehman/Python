name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        words = words[5][:2]
        d[words] = d.get(words, 0) + 1

List = list()
for k, v in d.items():
    List.append((k, v))
List.sort()
for k, v in List:
    print(k, v)


# desired output :
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
