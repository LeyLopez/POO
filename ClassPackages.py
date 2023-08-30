class Package():
    def __init__(self, tracking_number, source_address, destination_address, weight, state):
        self.tracking_number=tracking_number
        self.source_address=source_address
        self.destination_address=destination_address
        self.weight=weight
        self.state=state


    def get_info(self):
        return f"Tracking Number: {self.tracking_number}\n" \
               f"Origin: {self.source_address}\n" \
               f"Destination: {self.destination_address}\n" \
               f"Weight: {self.weight} kg"
        