#Set
#The set comprehension deals with the set data type and it's very similar to list 
#comprehension. The only key difference is the use of curly brackets for sets
# instead of square brackets as in lists
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

# Generator comprehensions  
# Generator comprehensions are also very similar to lists with the variation of 
# using curved brackets instead of square brackets. They are also more memory 
# efficient as compared to list comprehensions.


data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")