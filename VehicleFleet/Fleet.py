class fleet:    
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):  
            self.vehiculos.append(vehiculo)
            print("Vehículo agregado!")
        else:
            print("Error: El objeto no es de tipo Vehiculo")
        print("Vehículo agregado!")