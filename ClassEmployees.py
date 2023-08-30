class Employee():
    def __init__(self, name, id_employee, position):
        self.name=name
        self.id_employee=id_employee
        self.position=position
        
        def get_info(self):
            return f"Name: {self.name}\n" \
               f"ID Employed: {self.id_employee}\n" \
               f"Position: {self.position}"