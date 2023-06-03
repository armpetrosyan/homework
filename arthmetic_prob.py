def foo(one, two):
    if one - two > 0:
        operation = one - two
    else:
        operation = -1 * (one - two)

    addition = one + two

    result = operation / addition
    print(result)


x_input = int(input())
y_input = int(input())

if x_input + y_input == 0:
    print("Not Defined Operation")
else:
    foo(x_input, y_input)
