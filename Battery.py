from abc import ABC
import CarPart

class Battery(CarPart, ABC):
    @abstractmethod
    def battery_should_be_replaced(self):
        pass