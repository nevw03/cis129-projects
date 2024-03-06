# Author: Nathaniel Van Woert
# Second Python lab for CIS129
# Runs a simple coffee shop simulator

# This first batch of code is run first. A menu is displayed for the user.
print("Welcome to the Rising Star Coffee Shop!")
print("Menu:")
print("Coffee - $5.00")
print("Muffins - $4.00")
print("Cinnamon rolls - $3.50")
print("Donuts - $1.25")

# This batch of code is run next. This is the input function that asks the user how much of each menu item they want.
coffees = int(input("Number of coffees?: "))
muffins = int(input("Number of muffins?: "))
cinnarolls = int(input("Number of cinnamon rolls?: "))
donuts = int(input("Number of donuts?: "))

# Running calculations:
# cfetotal = total cost of coffees
# muftotal = total cost of muffins
# cinnatotal = total cost of cinnamon rolls
# donuttotal = total cost of donuts
# notax = total cost put together, before tax
# totaltax = 6% of notax, total amount of tax
# total = total cost with tax applied
cfetotal = (coffees*5.00)
muftotal = (muffins*4.00)
cinnatotal = (cinnarolls*3.50)
donuttotal = (donuts*1.25)
notax = (cfetotal+muftotal+cinnatotal+donuttotal)
totaltax = (notax*0.06)
total = (notax+totaltax)

#Final receipt:
print("***************************************")
print("Rising Star Coffee Shop")
print("Number of coffees bought?")
print(coffees,)
print("Number of muffins bought?")
print(muffins,)
print("Number of cinnamon rolls bought?")
print(cinnarolls,)
print("Number of donuts bought?")
print(donuts,)
print("***************************************")
print(" ")
print("***************************************")
print("My Coffee and Muffin Shop receipt",)
if(coffees==1):
    print(coffees, "Coffee at $5 each: $", f'{cfetotal:.2f}')
if(coffees!=1):
    print(coffees, "Coffees at $5 each: $", f'{cfetotal:.2f}')
if(muffins==1):
    print(muffins, "Muffin at $4 each: $", f'{muftotal:.2f}')
if(muffins!=1):
    print(muffins, "Muffins at $4 each: $", f'{muftotal:.2f}')
if(cinnarolls==1):
    print(cinnarolls, "Cinnamon roll at $3.50 each: $", f'{cinnatotal:.2f}')
if(cinnarolls!=1):
    print(cinnarolls, "Cinnamon rolls at $3.50 each: $", f'{cinnatotal:.2f}')
if(donuts==1):
    print(donuts, "Donut at $1.25 each: $", f'{donuttotal:.2f}')
if(donuts!=1):
    print(donuts, "Donuts at $1.25 each: $", f'{donuttotal:.2f}')
print("Total without tax: $", f'{notax:.2f}')
print("6% tax: $", f'{totaltax:.2f}')
print("---------")
print("Total: $", f'{total:.2f}')
print("***************************************")
print("Thank you for visiting the Rising Star Coffee Shop! We hope to see you again soon!")
