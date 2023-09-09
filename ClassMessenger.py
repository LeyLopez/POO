from ClassCustomers import *
from ClassEmployees import *
from ClassPackages import *
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
    def __init__(self, customer_list, employee_list, package_list):
        self.customer_list=customer_list
        self.employee_list=employee_list
        self.package_list=package_list
        
        
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
    

    def find_customer(self, customer_id):
        for customer in self.customer_list:
            if customer.get_id()==customer_id:
                return customer
        return None
            

    def delete_customer(self, customer_id):
        customer_to_delete=self.find_customer(customer_id)
        if customer_to_delete:
            self.customer_list.remove(customer_to_delete)
            print(f"Customer with ID {customer_id} deleted")
        else:
            print(f"Customer with ID {customer_id} not found")


    def find_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.get_id()==employee_id:
                return employee
        return None
    
    def delete_employee(self, employee_id):
        employee_to_delete=self.find_employee(employee_id)
        if employee_to_delete:
            self.employee_list.remove(employee_to_delete)
            print(f"Employee with ID {employee_id} deleted")
        else:
            print(f"Employee with ID {employee_id} not found")


    def find_package(self, package_number):
        for package in self.package_list:
            if package.get_id()==package_number:
                return package
        return None
    
    def delete_package(self, package_number):
        package_to_delete=self.find_package(package_number)
        if package_to_delete:
            self.package_list.remove(package_to_delete)
            print(f"Package with Tracking Number {package_number} deleted")
        else:
            print(f"Package with Tracking Number {package_number} not found")

    def search_delivered(self):
        for package in self.package_list:
            if package.get_state().lower()=="entregado":
                return package
        return None
            

    def show_delivered(self):
        package_delivered=self.search_delivered()
        if package_delivered:
            print(package_delivered.get_info())
        else:
            print("The packages in status 'DELIVERED' not found")

    

            

    
    

        
            


