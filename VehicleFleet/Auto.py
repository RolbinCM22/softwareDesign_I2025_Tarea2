from Vehicle import Vehiculo

class Auto(Vehiculo):
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
    
    def necesita_inspeccion(self):
        necesita_inspeccion = False
        if self.peso > 2000:
            necesita_inspeccion = True
        else:
            necesita_inspeccion = False
        
        return necesita_inspeccion
    
    def imprimir_datos(self):
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Eléctrico: {self.electric}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Estado: {self.estado}")
        print(f"Costo: {self.calcular_costo()}")
        print(f"Necesita inspección: {Si if self.necesita_inspeccion() else No}")
        print("===================================")

