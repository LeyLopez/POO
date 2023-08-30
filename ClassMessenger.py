# Add customer
# Add Employee
# Add Package
# Delete customer
# Delete Employee
# Delete Package
# Show Employee list
# Show customer list
# show package list
# change shipping status
# show packages delivered
# Assign packages to employee

class Messenger_Service():
    def __init__(self, customer_list, package_list, employee_list):
        self.customer_list=customer_list
        self.package_list=package_list
        self.employee_list=employee_list
        
    def add_customer(self, customer):
        self.customer_list.append(customer)

    def add_package(self, package):
        self.package_list.append(package)

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def show_customers(self):
        for customer in self.customer_list:
            print(customer.get_info())
    

    def show_employees(self):
        for employee in self.employee_list:
            print(employee.get_info())
            

    def show_packages(self):
        for package in self.package_list:
            print(package.get_info())

    def get_customer_list(self):
        return self.customer_list