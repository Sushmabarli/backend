from abc import ABC, abstractmethod

class CarPart(ABC):
    @abstractmethod
    def needs_service(self):
        pass