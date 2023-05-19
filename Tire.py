
from abc import ABC
import CarPart


class Tire(CarPart, ABC):
    @abstractmethod
    def needs_service(self):
        pass
