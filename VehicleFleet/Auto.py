from Vehicle import Vehicle

class Auto(Vehicle):
    def __init__(self, color, peso, electrico, capacidad_pasajeros):
        self.color = color
        self.peso = peso
        self.ruedas = 4
        self.electric = electrico
        self.capacidad_pasajeros = capacidad_pasajeros        
        self.estado = "nuevo"
    
    def calcular_costo(self):
        base = 15000
        extra = self.peso * 100
        if self.electric:
            extra += 5000
        return base + extra
    
    