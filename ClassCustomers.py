from ClassPerson import Person
class Customer(Person):
    def __init__(self, name, lastname, address, email, phone_number, city, id_customer):
        super().__init__(name, lastname, email, phone_number, city)
        self.address=address
        self.id_customer=id_customer

    

    def get_info(self):
        return f"Name: {self.name} Lastname: {self.lastname} Address: {self.address} Email: {self.email} Phone Number: {self.phone_number} City: {self.city} ID Customer: {self.id_customer}"
    

    def get_id(self):
        return self.id_customer
    