from abc import ABC
import CarPart
class Engine(CarPart, ABC):
    @abstractmethod
    def engine_should_be_serviced(self):
        pass