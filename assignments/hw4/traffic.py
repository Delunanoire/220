"""
Name: Stephanie Pittman
traffic.py

Problem: Calculate the average number of vehicles that travel each road per day.
         Calculate the overall number and average of vehicles on all roads.

Certificate of Authenticity:
I certify that this assignment is entirely my work.

Input : User information from DOT
Output: Average cars per road per day ; Average cars on all roads

"""

def main():
    # number of roads
    roads = int(input("How many roads were surveyed? "))

    # counters
    complete_days = 0
    complete_cars = 0

    # first outer loop
    for day_count in range(roads):

        days = int(input("How many days was road " + str(day_count + 1) + " surveyed? "))

        cars_total = 0

        # second loop
        for car_count in range(days):
            cars = int(input("How many cars were surveyed on road " + str(car_count + 1) + "? "))
            cars_total = cars_total + cars

        avg = cars_total / days

        print("the average is:" + str(round(avg, 2)))
        complete_cars += cars_total
        complete_days += days

    avg2 = complete_cars / roads

    print("Total amount of vehicles traveled on all roads: " + str(complete_cars))
    print("Average number of vehicles per road: " + str(round(avg2, 2)))

if __name__ == '__main__':
    main()
