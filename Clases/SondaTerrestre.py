
from Clases.Robot import Robot

class SondaTerrestre(Robot):
    """
    Clase que representa al tipo de Robot Sonda Terrestre:
    consumoSensorSismo: consumo medido en Ah (amperios hora)
    consumoSensorViento: consumo medido en Ah
    consumoSensorCalor: consumo medido en Ah
    Ampliar detalle de sus elementos viendo su clase padre Robot
    """


    def __init__(self, nombre, dimensiones, camaras, bateria, kilos, costo, 
                 consumoSensorSismo, consumoSensorViento, consumoSensorCalor):
        super().__init__(nombre, dimensiones, camaras, bateria, kilos, costo)
        self.consumoSensorSismo = consumoSensorSismo
        self.consumoSensorViento = consumoSensorViento
        self.consumoSensorCalor = consumoSensorCalor    

    
    def consumoTotal(self):
        consumoAh = super().consumoTotal()
        return consumoAh + self.consumoSensorSismo + self.consumoSensorViento + self.consumoSensorCalor