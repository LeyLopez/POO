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
    print("10. Change package status")
    print("11. Show packages delivered")
    print("12. Assign packages to employee")
    print("13. Salir")

    return input("Enter your choise: ")


def main():
    menssenger_service=Messenger_Service([], [], [])


    while True:
        
        option=show_menu()

        if option == '1':
            name = input("Name: ")
            address = input("Address: ")
            phone = input("Phone: ")
            id_customer = input("Customer ID: ")
            customer = Customer(name, address, phone, id_customer)
            menssenger_service.add_customer(customer)
            print("El cliente fue creado y agregado a la lista de clientes correctamente")

        elif option == '2':
            Ename = input ("Employee name: ")
            Elastname = input("Employee last name: ")
            employeeid = input("Employee ID: ")
            eposition = input("Position in the company: ")
            employee = Employee(Ename, Elastname, employeeid, eposition)
            menssenger_service.add_employee(employee)
            print("El empleado ha sido creado y agregado a la lista de empleados correctamente")

        elif option == '3':
            tnumber = input("Traching number: ")
            saddress = input("Source address: ")
            daddress = input("Destination address: ")
            status = input("Shipment status: ")
            package = Package(tnumber, saddress, daddress, status)
            menssenger_service.add_package(package)
            print("El paquete ha sido creado y agregado correctamente a la lista de paquetes")

        elif option == '4':
            menssenger_service.show_customers()

        elif option == '5':
            menssenger_service.show_employees()

        elif option == '6':
            menssenger_service.show_packages()

        elif option == '7':
            id = input("Enter the Customer ID: ")
            if id==Customer.get_id_customer:
                menssenger_service.customer_list.remove(id)


if __name__ == "__main__":
    main()    
            