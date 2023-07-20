def reverseString(any_string):
    if any_string == "":
        return any_string
    else:
        return reverseString(any_string[1:]) + any_string[:1]


x = input("input a String : ")
print("String reversed as : ", reverseString(x))
