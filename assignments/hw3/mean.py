# Stephanie Pittman
# CSCI 220

# This program will calculate the mean

# Certificate of Authenticity: I certify that this assignment is entirely my work.

# this program will calculate the average of a given set of numbers
# the inputs will be from the user
# the output will be

from math import sqrt
def main():
    n = eval(input("Enter the values to be entered: "))
    acc = 0
    harm_acc = 0
    rms_acc = 0
    geo_acc = 1

    for i in range(n):
        number = int(input("Enter value " + str(i + 1) + ": "))
        acc = acc + number
        harm_acc = harm_acc + 1 / number
        rms_acc = rms_acc + (number) ** 2
        geo_acc = geo_acc * number

    harm_avg = n / harm_acc
    rms_avg = sqrt(rms_acc / n)
    geo_avg = (geo_acc) ** (1 / n)

    print(round(rms_avg, 3))
    print(round(harm_avg, 3))
    print(round(geo_avg, 3))

if __name__ == '__main__':
    main()
