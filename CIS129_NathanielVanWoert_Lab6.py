# Nathaniel Van Woert
# CIS129 Lab 6
# Hotdog Cookout Calculator

import math

# Declare all variables
DOGS = 10
BUNS = 8
people = 0
hotdogs = 0
total = 0
dogsleft = 0
bunsleft = 0
partdogs = 0
partbuns = 0
mindogs = 0
minbuns = 0

# Input number of people attending and number of hotdogs per person
people = int(input("Enter the number of people attending the cookout: "))
hotdogs = int(input("Enter the number of hot dogs for each person: "))
# Calculate total required hotdogs
total = people * hotdogs

# Calculate packages needed
mindogs = math.ceil(total / DOGS) 
minbuns = math.ceil(total / BUNS) 
# Calculate leftovers
partdogs = (total % DOGS)
partbuns = (total % BUNS)
dogsleft = (DOGS - partdogs)
bunsleft = (BUNS - partbuns)

# Print results
print("Minimum packages of hot dogs needed:", mindogs)
print("Minimum packages of hot dog buns needed:", minbuns)
print("Hot dogs left over: ", dogsleft)
print("Hot dog buns left over: ", bunsleft)