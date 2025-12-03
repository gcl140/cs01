# File: how_rich.py
# Author: Gift Christian
# Date: September 28, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: Using functions to calculate compound interest for any given principal,
#               interest rate, start year, and end year. The program is inspired by the
#               Brutus problem, but generalized to work for any inputs. 


#Brutus's Constants
BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 5 
START_YEAR = 0
END_YEAR = 2023

#The function to calculate compound interest, takes four parameters: principal amount, starting year, ending year, and interest rate
def calculate_compound_interest(principal, year_now, end_year, rate):
        balance = principal             #Set the initial balance to the principal amount from the parameters
        current_year = year_now         #Set the current year to the starting year from the parameters
        final_year = end_year           #Set the final year to the ending year from the parameters
        interest_in_decimal = rate/100  #Convert the interest rate given in the parameters from percentage to decimal form

        #Loop to calculate compound interest for each year from starting year to ending year
        while current_year < final_year:                    #Loop until the current year is greater than the final year
            balance = balance * (1 + interest_in_decimal)   #Same as balance = balance + (balance * interest_in_decimal). Update the balance by multiplying it by (1 + interest rate in decimal form). 
            current_year += 1                               #Increment the current year by 1 for the next iteration

        final_interest = balance - principal                #When the while loop ends, calculate the total interest earned by subtracting the initial principal from the final balance

        print("At year " + str(current_year) + ", the balance is $" + str(balance) + ".")                #Using string concatenation to print the final year and balance
        print("At year " + str(current_year) + ", the interest earned is $" + str(final_interest) + ".") #Using string concatenation to print the final year and interest earned


print("Brutus:")                                                                                        #Heading for Brutus's account
calculate_compound_interest(BRUTUS_INITIAL_DEPOSIT, START_YEAR, END_YEAR, BRUTUS_INTEREST_RATE)         #Call the function with Brutus's parameters