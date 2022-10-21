from tires.tires import Tires
from array import array

class CarriganTires (Tires):
    def __init__(self, worn):
        worn = [range (0,1.1)]
        worn = worn [:4]
        self.worn = worn
    def needs_service(self):
        for tire in self.worn:
            if tire >= 0.9:
                return True
        return False
