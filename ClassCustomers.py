class Customer():
    def __init__(self, name, address, phone_number, id_customer):
        self.name=name
        self.address=address
        self.phone_number=phone_number
        self.id_customer=id_customer

    '''def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_id_costummer(self):
        return self.__id_customer'''
    

    def get_info(self):
        return f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"ID Customer: {self.id_customer}"
    

    def get_id_customer(self):
        return self.id_customer