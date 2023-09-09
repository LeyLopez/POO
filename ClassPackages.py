class Package():
    def __init__(self, tracking_number, source_address, destination_address, weight, status):
        self.tracking_number=tracking_number
        self.source_address=source_address
        self.destination_address=destination_address
        self.weight=weight
        self.status=status


    def get_id(self):
        return self.tracking_number
    
    def get_state(self):
        return self.status
    
    def get_info(self):
        return f"Tracking Number: {self.tracking_number} Origin: {self.source_address} Destination: {self.destination_address} Weight: {self.weight} kg Status: {self.status}"