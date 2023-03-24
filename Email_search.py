
fname = input("Enter file:")
if len(fname) < 1:
    name = "mbox-short.txt"
hand = open(fname)

lst = list()

for line in hand:
    if line.startswith("From:"):
        line = line.split()
        lst.append(line[1])
    else:
        continue

counts = dict()
for word in lst:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
