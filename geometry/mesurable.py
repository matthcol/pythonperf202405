from abc import ABC, abstractmethod


class Mesurable2D(ABC):
    
    @abstractmethod
    def surface(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass