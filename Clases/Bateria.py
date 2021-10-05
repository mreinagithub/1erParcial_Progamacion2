from Clases.EspecificacionElemento import EspecificacionElemento


class Bateria:
    """
    Los robots cuentan con baterias de las que se regitra la duración (para poder contrastar contra consumo se mide en amperes-hora), kilos y costo.
    Ej. Si la bateria es de 100Ah, esta puede soportar consumos de 1 Amperio durante 100 horas.    
    Kilos: el peso de la bateria
    Costo: el costo en dólares de la bateria
    """
    def __init__(self, amperesHora, kilos, costo):
        self.amperesHora = amperesHora
        self.especificacionElemento = EspecificacionElemento(kilos, costo)

        