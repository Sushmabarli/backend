
from abc import ABC

import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear_array)
