# Module 4 Lab-4
# Nathaniel Van Woert
# 3/13/2024
# This program calculates bonus amounts for a retail company.

# declare local variables
monthlySales = 0   # monthly sales amount
storeAmount = 0   # store bonus amount
empAmount = 0   # employee bonus amount
salesIncrease = 0   # percent of sales increase

# include code to get the monthly Sales
# include code to get the Increase in Sales
# include code to Calculate the Store Bonus
# include code to Calculate the Employee Bonus
# include code to print out all the results

# This code gets the monthly sales
monthlySales = float(input('Input monthly sales: '))

# This code determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input('Percent sales increase: '))
salesIncrease = salesIncrease / 100

# This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
	empAmount = 50
elif salesIncrease >= .03:
	empAmount = 40
else:
	empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')