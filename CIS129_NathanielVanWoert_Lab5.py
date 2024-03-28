# Nathaniel Van Woert
# 27 March 2024
# This program takes bottles per day and calculates the number collected per week, as well as the payout

keepGoing = "y"
while keepGoing == "y":
    # initialize variables
    total_bottles = 0
    today_bottles = 0
    counter = 1
    # input total bottles
    while counter <= 7:
        print('Enter number of bottles returned for day #',counter,":")
        today_bottles = int(input())
        total_bottles = total_bottles + today_bottles
        counter = counter + 1
    # run payout calculations
    total_payout = 0
    total_payout = total_bottles*0.1
    # print final results
    print("Total bottles collected:", total_bottles)
    print("Total payout: $", (f'{total_payout:.2f}'))
    # statement to restart loop
    keepGoing = input("Would you like to enter another week's worth of data?\n(Enter y or n)")