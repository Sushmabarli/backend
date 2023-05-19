from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def needs_service(self):
        for part in self.parts:
            if isinstance(part, CarPart) and part.needs_service():
                return True
        return False