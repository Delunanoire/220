"""
Name: Stephanie Pittman
sales_force.py

Problem: Develop a Python program that uses an object with a list
        Use a list of objects

Certificate of Authenticity:
I certify that this assignment is my work and was discussed with Tutor Brooke Duvall.

"""

from sales_person import SalesPerson


class SalesForce:
    """
    header goes here
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):

        with open(file_name, 'r') as file:

            for line in file.readlines():
                new_list = line.split(', ')
                employee_id = new_list[0]
                name = new_list[1]
                all_sales = new_list[2]
                all_sales = all_sales.split(' ')
                person = SalesPerson(employee_id, name)
                for sales in all_sales:
                    person.enter_sale(float(sales))
                self.sales_people.append(person)

    def quota_report(self, quota):
        report = []
        for people in self.sales_people:
            info_list = [people.get_id(), people.get_name(),
                         people.total_sales(), people.met_quota(quota)]
            report.append(info_list)
        return report

    def individual_sales(self, employee_id):
        for item in self.sales_people:
            if item.get_id() == employee_id:
                return item
        return None

    def top_seller(self):
        max_sales = -1

        for item in self.sales_people:
            if item.total_sales() > max_sales:
                max_sales = item.total_sales()
        new_array = []
        for whatever in self.sales_people:
            if max_sales == whatever.total_sales():
                new_array.append(whatever)
        return new_array
