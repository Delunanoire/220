"""
Name: Stephanie Pittman
sales_person.py

Problem: Use an object with a list
         Use a list of objects

Certificate of Authenticity:
I certify that this assignment is my work and was discussed with Tutor Brooke Duvall.

"""

class SalesPerson:

    """
    sales person class
    """

    def __init__(self, employee_id, name):

        self.employee_id = int(employee_id)
        self.name = str(name)
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def get_sales(self):
        return self.sales

    def set_name(self, name):
        self.name = name

    def total_sales(self):
        total = 0
        for item in self.sales:
            total = total + item
        return total

    def __str__(self):
        return str(self.employee_id) + '-' + self.name + ': ' + str(self.total_sales())

    def enter_sale(self, sale):
        self.sales.append(sale)

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        return 0
