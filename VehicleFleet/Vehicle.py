from abc import ABC, abstractmethod

def Vehiculo(ABC):
    """
    Abstract base class for all vehicles.
    """
    @abstractmethod
    def calcular_costo(self):
        """
        Calculate the cost of the vehicle.
        """
        pass

    @abstractmethod
    def necesita_inpeccion(self):
        """
        Check if the vehicle needs inspection.
        """
        pass

    @abstractmethod
    def imprimir_datos(self):
        """
        Print vehicle information.
        """
        pass