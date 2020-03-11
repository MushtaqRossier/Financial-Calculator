#Requesting the user to choose the calculation of their choice
calculation = input("Would you like to do an 'investment' or 'bond' calculation?: ").capitalize()


#Conditions if user chooses 'investment'.
#Depending on the type of interest the user chooses, the if statement calculates and displays the final amount the user will receive.
if calculation == "Investment":
    money = int(input("Enter the amount of money you'd like to deposit: "))
    interest_rate = float(input("Enter the amount of interest(%) you want on your deposit: "))
    years = int(input("Enter the amount of years you plan on investing for: "))
    type_of_interest = input("Would you like simple or compound interest: ")
    if type_of_interest == "simple":
        amount = money*(1 + (interest_rate/100)*years)
    else:
        amount = round((money*(1 + (interest_rate/100))**years), 2)
    print("The amount you'll receive after", years,"years = R",amount) 

#Conditions if user chooses 'bond'.
#Calculates and displays the amount that needs to be repaid each month for the bond
else:    
    present_value = int(input("Enter the present value of the house: "))
    interest_rate = int(input("Enter the interest rate (%): "))
    months = int(input("Enter the number of months you plan to take to repay the bond: "))
    r = (interest_rate/100)/12  #Monthly interest rate
    numerator = r*(1 + r)**months
    denominator = ((1 + r)**months - 1)
    repayment = round((present_value*(numerator/denominator)), 2)
    print("The amount of money that needs to be repaid each month =", repayment)

  