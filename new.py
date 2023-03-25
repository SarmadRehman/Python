name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From"):
        words = line.split()
    else:
        continue
print(words)
