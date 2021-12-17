def function():
    try:
        number  = int(input("Please Enter an integer number: "))
    except ValueError:
        print("This is invalid input, please provide an integer, debugging")
    else:
        if number == 0:
            print("O is universe number")
        elif number % 2 == 0:
             print("It is an even number")
        else:
             print("It is an odd number")
function()
