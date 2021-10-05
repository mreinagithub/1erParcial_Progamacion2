
from Clases.EspecificacionElemento import EspecificacionElemento


class Camara:
    """
    Clase Camara que forma parte de una coleccion que componen a un robot:
    alcance: distancia en metros a la que puede alcanzar.
    zoom: distancia focal X.
    megapixeles: cantidad de pixeles en millones que tiene la cámara.
    consumo: cantidad medida en Ah que consume.
    kilos: peso de la cámara
    costo: costo en USD de la cámara.
    """

    def __init__(self, alcance, zoom, megapixeles, consumo, kilos, costo):
        self.alcance = alcance
        self.zoom = zoom
        self.megapixeles = megapixeles
        self.consumo = consumo
        self.especificacionElemento = EspecificacionElemento(kilos, costo)