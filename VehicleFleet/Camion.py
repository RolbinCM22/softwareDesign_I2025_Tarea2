from Vehicle import Vehicle

class Camion(Vehicle):
    def __init__(self, color, peso, electrico, capacidad_pasajeros):
        self.tipo = "Camión"
        self.color = color
        self.peso = peso
        self.ruedas = 4
        self.capacidad_pasajeros = capacidad_pasajeros        
        self.estado = "nuevo"
    def calcular_costo(self):
        base = 45000
        extra = self.peso * 200
        return base + extra
    
    def necesita_inspeccion(self):
            return True
    def imprimir_datos(self):
         print(f"Vehículo tipo: {self.tipo}")        
         print(f"Color: {self.color}")        
         print(f"Peso: {self.peso} kg")        
         print(f"Ruedas: {self.ruedas}")               
         print(f"Capacidad: {self.capacidad_pasajeros} pasajeros")        
         print(f"Costo: ${self.calcular_costo()}")        
                 
                                                                                                                                                                                                                                                                                                                                                                                    