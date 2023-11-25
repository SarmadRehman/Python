def d():
    animal = "elephant"

    def e():
        nonlocal animal
        animal = "giraffe"
        print("inside nested function:", animal)

    print("Before calling function: ", animal)
    e()
    print("After calling function: ", animal)


animal = "camel"
d()
print("Global animal: ", animal)
