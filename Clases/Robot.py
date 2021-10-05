
from Clases.Bateria import Bateria
from Clases.Camara import Camara
from Clases.EspecificacionElemento import EspecificacionElemento


class Robot:
    """
    Clase que donde se abstraen los atributos y comportamientos comunes a cualquier robot:
    nombre: nombre del robot
    dimensiones: un vector de dos posiciones, siendo X=Alto e Y=Ancho
    camaras: lista que contiene la lista de elementos necesarios para construir una cámara según su especificación en la clase Camara
    bateria: lista de los elementos para construir una bateria según su especificación en la clase Bateria 
    peso: medido en Kg
    costo: valor en dólares del robot    
    """
   

    def __init__(self, nombre, dimensiones, camaras, bateria,
                kilosRobot, costoRobot):
        self.nombre = nombre
        self.dimensiones = dimensiones        
        self.bateria = Bateria(bateria[0], bateria[1], bateria[2])
        self.especificacionElemento = EspecificacionElemento(kilosRobot, costoRobot)
        self.diasFuncionando = 0
        self.camaras = []
        #Las camaras forman parte del constructor del robot dado que estas lo componen
        for camara in camaras:
            self.camaras.append(Camara(camara[0], camara[1], camara[2], camara[3], camara[4], camara[5]))

    def __str__(self):
        #Mostramos información del robot
        return (f"Tipo: {type(self).__name__} | Nombre: {self.nombre} | Alto: {self.dimensiones[0]}m | Ancho: {self.dimensiones[1]}m"
                f" | Dias Funcionando: {self.diasFuncionando}\n"
                f"   Kilos: {self.especificacionElemento.kilos}kg | Costo total: usd {self.obtenerCosto()}"
                f" | Bateria: {self.bateria.amperesHora}Ah | Consumo total: {self.consumoTotal()}Ah | Autonomía de la batería: {self.estimarDuracionBateria():.2f}Hs")
    
    def __eq__(self, otro):
        if (isinstance(otro, Robot)):
            return self.nombre.upper() == otro.nombre.upper()
        else: return False


    def agregarDiaFuncionando(self):
        self.diasFuncionando += 1

    def consumoTotal(self):
        #Obtiene el consumo relativo a sus camaras
        consumoAh = 0
        for camara in self.camaras:
            consumoAh += camara.consumo
        return consumoAh

    def estimarDuracionBateria(self):
        duracionEstimada = 0
        try:
            duracionEstimada = self.bateria.amperesHora / self.consumoTotal()
        except ZeroDivisionError:
            print("No puede dividir por cero. El consumo total de este robot es inválido.")
            duracionEstimada = 0
        
        return duracionEstimada;

    def obtenerCosto(self):
        costo = self.especificacionElemento.costo
        costo += self.bateria.especificacionElemento.costo
        costoCamaras = sum([camara.especificacionElemento.costo for camara in self.camaras]) #list comprehension
        return costo + costoCamaras
    






    
    

