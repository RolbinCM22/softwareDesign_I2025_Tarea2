from Vehicle import Vehicle

class Moto(Vehicle):
    def __init__(self, color, peso, electrico):
        self.tipo = "Moto"
        self.color = color
        self.peso = peso
        self.ruedas = 2
        self.capacidad_pasajeros = 2        
        self.estado = "nuevo"
    
    def calcular_costo(self):
        base = 8000
        extra = self.peso * 50
        if self.electric:
            extra += 3000
        return base + extra
    
    def necesita_inspeccion(self):
            if self.peso > 300:
                return True
            return False
    
    def imprimir_datos(self):
         print(f"Vehículo tipo: {self.tipo}")        
         print(f"Color: {self.color}")        
         print(f"Peso: {self.peso} kg")        
         print(f"Ruedas: {self.ruedas}")               
         print(f"Capacidad: {self.capacidad_pasajeros} pasajeros")        
         print(f"Costo: ${self.calcular_costo()}")     