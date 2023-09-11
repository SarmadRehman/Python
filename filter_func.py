ages = [5, 12, 17, 18, 24, 32]

# filter() function expects the provided function to return a boolean 
# value (True or False).
def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)
# filter object is returned
print(adults)

for x in adults:
    print(x)
