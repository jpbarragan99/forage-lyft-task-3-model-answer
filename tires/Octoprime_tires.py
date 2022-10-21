from tires.tires import Tires
from array import array

class OctoprimeTires (Tires):
    def __init__(self, worn):
        self.worn = worn
    def needs_service(self):
        return sum(self.worn) >= 3.0
