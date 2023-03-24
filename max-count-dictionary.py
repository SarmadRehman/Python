name = input('Enter the file name to open : ')
file = open(name)
count = dict()
for line in file:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
bigCount = None
bigWord = None
for aaaa, bbbb in count.items():
    if bigCount is None or bbbb > bigCount:
        bigCount = bbbb
        bigWord = aaaa
print(bigWord, ":", bigCount)
