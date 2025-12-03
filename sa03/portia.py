# File: portia.py
# Author: Gift Christian
# Date: September 28, 2025
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
# Description: A method to determine how long it takes for Brutus to catch up to Portia.
#              The program uses a while loop to calculate the compound interest for both
#              Brutus and Portia each year until Brutus's balance exceeds Portia's balance
#              and prints out the year and balances for both each year.

#Constants
#Brutus's account
BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 5

#Portia's account
PORTIA_INITIAL_DEPOSIT = 100000
PORTIA_INTEREST_RATE = 4

#Common constants
START_YEAR = 0
END_YEAR = 2023

#Variables
#Brutus's account
brutus_interest = 0                                     #Interest earned by Brutus each year, the starting value is 0
brutus_balance = BRUTUS_INITIAL_DEPOSIT                 #Current balance of Brutus's account  
brutus_percentage_interest = BRUTUS_INTEREST_RATE/100   #Brutus's interest rate in decimal form

#Portia's account
portia_interest = 0                                     #Interest earned by Portia each year, the starting value is 0
portia_balance = PORTIA_INITIAL_DEPOSIT                 #Current balance of Portia's account
portia_percentage_interest = PORTIA_INTEREST_RATE/100   #Portia's interest rate in decimal form

#Common variables
current_year = START_YEAR                               #The current year, starting from the year both Brutus and Portia made their deposits

#Loop to calculate compound interest for both Brutus and Portia each year from START_YEAR to END_YEAR
while current_year <= END_YEAR:
    
    #Continue the loop as long as Brutus's balance is less than Portia's balance
    if brutus_balance < portia_balance:
        #For Brutus's account
        brutus_interest = brutus_balance * brutus_percentage_interest          #Calculate interest for Brutus's account
        brutus_balance = brutus_interest + brutus_balance                      #Update Brutus's balance with the interest earned
        
        #For Portia's account
        portia_interest = portia_balance * portia_percentage_interest   #Calculate interest for Portia's account
        portia_balance = portia_interest + portia_balance               #Update Portia's balance with the interest earned

        current_year += 1                                               #Increment the year for the next iteration. Its the same for both Brutus and Portia since they start and end in the same years
        
    #If Brutus's balance exceeds or equals Portia's balance, exit the loop by setting current_year beyond END_YEAR, hence the while loop condition becomes false
    else:
        print("The year Brutus surpasses Portia is: " + str(current_year - 1))       #Subtract 1 from current_year to get the year Brutus's balance exceeded Portia's balance (current_year += 1, it takes out the plus 1 that happens at the end of the loop)
        print("Brutus's balance: $" + str(brutus_balance))                           #Print Brutus's final balance
        print("Portia's balance: $" + str(portia_balance))                           #Print Portia's final balance
        # break                                                                      #an alternative
        current_year = END_YEAR + 1                                                  #Manually set current_year beyond END_YEAR to exit the while loop (Break)
        
