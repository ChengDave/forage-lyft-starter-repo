from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        raise NotImplementedError("Method needs to be implemented")