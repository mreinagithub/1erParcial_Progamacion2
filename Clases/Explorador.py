
from Clases.Robot import Robot


class Explorador(Robot):
    """
    Clase que representa a un Robot Explorador:    
    velocidadMaxima: velocidad máxima que puede alcanzar un robot explorador medida en Km/h
    consumo: consumo a dicha velocidad medido en amperios hora Ah.    
    Ampliar detalle de sus elementos viendo su clase padre Robot
    """


    def __init__(self, nombre, dimensiones, camaras, bateria, kilos, costo, velocidadMaxima, consumo):
        super().__init__(nombre, dimensiones, camaras, bateria,kilos,costo)
        self.velocidadMaxima = velocidadMaxima
        self.consumo = consumo

    def __str__(self):
        txt = super().__str__()
        txt += f" | V.Máxima: {self.velocidadMaxima}Km"
        return txt    


    def consumoTotal(self):
        consumoAh = super().consumoTotal()
        return consumoAh + self.consumo