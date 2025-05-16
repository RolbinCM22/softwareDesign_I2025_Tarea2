from report import Report

class ReportFleet(Report):

    def __init__(self, vehiculos):
        self.vehiculos = vehiculos

    def calcular_datos_reporte(self):
        total = 0
        electricos = 0
        requiere_inspeccion = 0

        for v in self.vehiculos:
            total += v.calcular_costo()
            if v.es_electrico:
                electricos += 1
            if v.necesita_inspeccion():
                requiere_inspeccion += 1

        return {
            "total": total,
            "electricos": electricos,
            "requiere_inspeccion": requiere_inspeccion,
            "cantidad": len(self.vehiculos)
        }

    def generate_report(self):
        return self.calcular_datos_reporte()