from ClassPerson import Person
class Employee(Person):
    def __init__(self, name, lastname, email, phone_number, city, id_employee, position):
        super().__init__(name, lastname, email, phone_number, city)
        self.id_employee=id_employee
        self.position=position

    def get_info(self):
        return f"Name: {self.name} Lastname: {self.lastname} Email: {self.email} Phone Number{self.phone_number} City: {self.city} Employee ID: {self.id_employee} Position: {self.position}"
        

    def get_id(self):
        return self.id_employee