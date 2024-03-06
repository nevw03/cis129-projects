# Author: Nathaniel Van Woert
# Second Python lab for CIS129
# Runs a simple coffee shop simulator

# This first batch of code is run first. The input functions ask how much of each iten the user wants.
coffees = int(input("Number of coffees bought?: "))
muffins = int(input("Number of muffins bought?: "))

# Running calculations:
cfetotal = (coffees*5.00)
muftotal = (muffins*4.00)
notax = (cfetotal+muftotal)
totaltax = (notax*0.06)
total = (notax+totaltax)

#Final receipt:
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffees)
print("Number of muffins bought?")
print(muffins,)
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
print("6% tax: $", f'{totaltax:.2f}')
print("---------")
print("Total: $", f'{total:.2f}')
