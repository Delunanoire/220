# Stephanie Pittman


# print that this program calculates the value of investment after 10 years
# input the initial principal from the user
# input the annual percentage rate
# loop through 10 years
# calculate principal + interest
# print the result
def main():
    print("This program calculates the value of investment after 10 years")
    apr      = eval(input("enter the annual interest rate: "))
    billing  = eval(input("enter number of days in billing cycle: "))
    net_bal  = eval(input("Enter the previous net balance: "))
    payment  = eval(input("Enter the payment amount: "))
    pay_date = eval(input("Enter the day of the billing cycle in which the payment was made: "))
    dbec = billing - pay_date
    step1 = net_bal * billing
    step2 = payment * dbec
    step3 = step1 - step2
    step4 = step3 / billing
    interest_rate = (apr / 12) / 100
    interest_charge = step4 * interest_rate

    print("The monthly interest charge is", round(interest_charge, 2))

    # for i in range(10):
    #     total = total * (1 + apr)
    # print("your total is:", total)

if __name__ == '__main__':
    main()
