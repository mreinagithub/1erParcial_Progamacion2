
from Clases.Robot import Robot

class SondaEspacial(Robot):
    """
    Clase que representa al tipo de Robot Sonda Terrestre:
    altitudMinima: altitud mínima operativa medida en Km 
    consumoMinimo: consumo mínimo medido en Ah (amperios hora)   
    Ampliar detalle de sus elementos viendo su clase padre Robot     
    """


    def __init__(self, nombre, dimensiones, camaras, bateria, kilos, costo,  altitudMinima, consumoMinimo):
        super().__init__(nombre, dimensiones, camaras, bateria,kilos, costo)
        self.altitudMinima = altitudMinima
        self.consumoMinimo = consumoMinimo

    def __str__(self):
        txt = super().__str__()
        txt += f" | Al.Mínima: {self.altitudMinima}Km"
        return txt


    def consumoTotal(self):
       consumoAh = super().consumoTotal()
       return consumoAh + self.consumoMinimo
        