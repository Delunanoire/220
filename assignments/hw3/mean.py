# Stephanie Pittman
# CSCI 220

# This program will calculate the mean

# Certificate of Authenticity: I certify that this assignment is entirely my work.

# this program will calculate the average of a given set of numbers
# the inputs will be from the user
# the output will be

from math import *
def main():
    n = eval(input("Enter the values to be entered: "))
    n = int(n)
    total = 0
    value = 0

    for i in range(n):
        total = total + 1
        value += int(input("Enter value " + str(total) + ": "))


        geo_mean = value ** (1/n)
        har_mean = value / n
        rms_mean = value + 1

    print(round(geo_mean, 2), round(har_mean, 3), round(rms_mean, 3))

if __name__ == '__main__':
    main()