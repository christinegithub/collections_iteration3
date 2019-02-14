# Exercise 11
# Let's do our own Bitmaker version of FizzBuzz, which is the name of a classic job interview coding problem.
#
# Write a program that loops over the numbers from 1 to 100. If the number is a multiple of three, output the string
# "Bit". For multiples of five, output "Maker". For numbers which are multiples of both three and five, output
# "BitMaker". Otherwise output the number itself.


one_to_hundred = range(1, 101)

for num in one_to_hundred:
    if num % 3 == 0 and num % 5 == 0:
        print("Bitmaker")
    elif num % 5 == 0:
        print("Maker")
    elif num % 3 == 0:
        print("Bit")
    else:
        print(num)


# Exercise 12

# PizzaMaker wants to handle bulk orders of pizzas, with varying amounts of toppings on each.
# Ask the user for a number of pizzas - call it quantity. We then want to ask the user for quantity more
# numbers - the number of toppings on that pizza - and print them out as in the following example.
#
# How many pizzas do you want to order?
# $ 3
# How many toppings for pizza 1?
# $ 5
# You have ordered a pizza with 5 toppings.
# How many toppings for pizza 2?
# $ 1
# You have ordered a pizza with 1 toppings.
# How many toppings for pizza 3?
# $ 4
# You have ordered a pizza with 4 toppings.
# You will need:
#
# to ask the user for input twice.
# a loop of some kind.
# to make sure your variables are what you think they are! Convert them to integers if needed.
# string interpolation

print("How many pizzas do you want to order?")
quantity = int(input())

num_of_pizzas = range(1, quantity + 1)

for num in num_of_pizzas:
    print("How many toppings for pizza {}?".format(num))
    toppings = int(input())
    print("You have ordered a pizza with {} toppings".format(toppings))
