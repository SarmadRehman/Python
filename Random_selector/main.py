import random

f_name = input("Type the file name: ")
b = "Random_selector/" + f_name + ".txt"
f = open(b)  # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))
