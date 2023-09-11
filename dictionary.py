count = dict()
line = input('some text give in:\n')
# this .split() splits the given string w.r.t spaces and make a list to store them
# all
splitList = line.split()
for word in splitList:
    # .get() usually use a single parameter to search for in the dict but the
    # other one is given for the case to give it a value when the string isn't present

    count[word] = count.get(word, 0) + 1
print('count', count, '\n', 'values: ', count.values(), '\n', 'keys: ', count.keys(), '\n',
      'tuples: ', count.items())
# a succinct way to iterate through two variables over tuples
for aaaa, bbbb in count.items():
    print(aaaa, ':', bbbb)
 