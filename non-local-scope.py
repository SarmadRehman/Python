def outer_function():
    x = 10  # Variable in the outer function scope

    def inner_function():
        nonlocal x  # Declare 'x' as nonlocal to modify the variable in the outer scope
        x = 20  # Modify the value of 'x' in the outer function's scope
        print("Inner function - modified x:", x)

    print("Outer function - before inner call:", x)
    inner_function()
    print("Outer function - after inner call:", x)


outer_function()
