def my_function(x):
    return x[::-1]


mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)


# Create a slice that starts at the end of the string, and moves backwards.
# In this particular example, the slice statement [::-1] means
# start at the end of the string and end at position 0, move with
# the step -1, negative one, which means one step backwards.
