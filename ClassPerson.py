class Person:
    def __init__(self, name, lastname, email, phone_number, city):
        self.name=name
        self.lastname=lastname
        self.email=email
        self.phone_number=phone_number
        self.city=city

    def get_info(self):
        return f"Name: {self.name} Lastname: {self.lastname} Email: {self.email} Phone Number: {self.phone_number} City: {self.city}"
    