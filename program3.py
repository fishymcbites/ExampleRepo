#Input function

def ask_for_input():
    number_picked = input("Pick a number: ")
    return number_picked

#Echo result function

def echo_user_input(x):
    print(x)

#Addition function with the ability to echo_user_input

def add_two_numbers(x,y):
    z = int(x) + int(y)
    print(z)

#Multiplication function

def multiply_three_numbers(x,y,z):
    a = int(x) * int(y) * int(z)
    return(a)

#Comparison function

def determine_largest(x,y):
    if "x" == "y":
        print(str(x) + " and " + str(y) + "are equal numbers.")
    elif "x" > "y":
        print(str(x) + " is the largest.")
    else:
        print(str(y) + " is the largest.")

#Ask initial number

a = ask_for_input()

echo_user_input(a)

#To add numbers together

a = ask_for_input()
b = ask_for_input()

add_two_numbers(a,b)

#To multiply two values

product = multiply_three_numbers(ask_for_input(),ask_for_input(),ask_for_input())

echo_user_input(product)

#To compare two values

a = ask_for_input()
b = ask_for_input()

determine_largest(a,b)

