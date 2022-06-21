from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self):
       raise NotImplementedError("Method needs to be implemented")
