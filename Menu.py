from ClassCustomers import Customer
from ClassMessenger import Messenger_Service
from ClassEmployees import Employee
from ClassPackages import Package

def show_menu():
    print("1. Add new customer to the list")
    print("2. Add new employee to the list")
    print("3. Add new package to the list")
    print("4. Show customer list")
    print("5. Show employee list")
    print("6. Show package list")
    print("7. Delete customer for Costumer ID")
    print("8. Delete employee for Employee ID")
    print("9. Delete package for tracking number")
    print("10. Show packages delivered")
    print("11. Exit")

    return input("Enter your choise: ")


def main():
    menssenger_service=Messenger_Service([], [], [])


    while True:
        
        option=show_menu()

        if option == '1':
            name = input("Name: ")
            lastname=input("Lastname: ")
            address = input("Address: ")
            email=input("Email: ")
            phone = int(input("Phone: "))
            city=input("City: ")
            id_customer = input("Customer ID: ")
            customer = Customer(name, lastname,address, email, phone, city, id_customer)
            menssenger_service.add_customer(customer)
            print("The client was created and added to the client list correctly")

        elif option == '2':
            ename = input("Employee name: ")
            elastname=input("Lastname: ")
            employeeid = input("Employee ID: ")
            eemail=input("Email: ")
            ephone = int(input("Phone number: "))
            ecity=input("City: ")
            eposition = input("Position in the company: ")
            employee = Employee(ename, elastname, eemail, ephone, ecity, employeeid, eposition)
            menssenger_service.add_employee(employee)
            print("The employee has been created and added to the employee list correctly.")

        elif option == '3':
            tnumber = int(input("Traching number: "))
            saddress = input("Source address: ")
            daddress = input("Destination address: ")
            weight = int(input("Package weight: "))
            status = input("Shipment status: ")
            package = Package(tnumber, saddress, daddress, weight, status)
            menssenger_service.add_package(package)
            print("The package has been created and successfully added to the list of packages.")

        elif option == '4':
            menssenger_service.show_customers()

        elif option == '5':
            menssenger_service.show_employees()

        elif option == '6':
            menssenger_service.show_packages()

        elif option == '7':
            id = input("Enter customer ID to be removed: ")
            menssenger_service.delete_customer(id)

        elif option=='8':
            eid = input("Enter employee ID to be removed: ")
            menssenger_service.delete_employee(eid)


        elif option=='9':
            pid=input("Enter the tracking number of the package to be deleted: ")
            menssenger_service.delete_package(pid)

        elif option=='10':
            menssenger_service.show_delivered()

        elif option == '11':
            print("Exiting the program")
            break


if __name__ == "__main__":
    main()    
