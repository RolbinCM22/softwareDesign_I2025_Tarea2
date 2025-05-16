from abc import ABC, abstractmethod

class Report(ABC):
    """
    Abstract base class for generating reports.
    """

    @abstractmethod
    def calcular_datos_reporte(self):
        """
        Calculate report data.
        """
        pass
    
    @abstractmethod
    def generate_report(self):
        """
        Generate a report.
        """
        pass