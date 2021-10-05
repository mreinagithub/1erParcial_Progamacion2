from functools import reduce
from os import stat

class SoporteCalculos:

    @staticmethod
    def obtenerRobotMenorDuracionBateria(robots):
        #Buscamos la minima duracion
        minDuracion = min([robot.estimarDuracionBateria() for robot in robots])
        #devolvemos una lista filtrada con el/los robots que tengan esa duracion minima    
        robotsADevolver = []
        for robot in robots:
            if robot.estimarDuracionBateria() == minDuracion:
                robotsADevolver.append(robot)
        return robotsADevolver

    @staticmethod
    def aumentarDiasFuncionando(robots):
        #usamos map para invocar a la función que agrega dias de funcionamiento para cada robot
        return list(map(lambda robot: robot.agregarDiaFuncionando(),robots))



    @staticmethod
    def obtenerTotalDiasFuncionamiento(robots):
        #creamos una lista de dias funcionando de cada robot
        arrDias = [r.diasFuncionando for r in robots]
        #usamos reduce para sumar los dias funcionado del array de dias de los robots
        return reduce(lambda x,y: x+y ,arrDias)

    @staticmethod
    def compararCostos(robot1, robot2):
        c1 = robot1.obtenerCosto()
        c2 = robot2.obtenerCosto()

        if c1 == c2:  print(f"Ambos robot tienen el mismo costo:")
        elif c1 > c2: print(f"El robot {robot1.nombre} es más CARO que el robot {robot2.nombre}")
        else:         print(f"El robot {robot1.nombre} es más BARATO que el robot {robot2.nombre}")        

        print(f"- Tipo: {type(robot1).__name__} - Nombre: {robot1.nombre} - Costo: usd {c1:.2f}\n"
              f"- Tipo: {type(robot2).__name__} - Nombre: {robot2.nombre} - Costo: usd {c2:.2f}")


    @staticmethod
    def obtenerRobotMasCaro(robots):
        #Buscamos el mas caro
        masCaro = max([robot.obtenerCosto() for robot in robots])
        #devolvemos una lista filtrada con el/los robots que tengan el valor más caro
        robotsADevolver = []
        for robot in robots:
            if robot.obtenerCosto() == masCaro:
                robotsADevolver.append(robot)
        return robotsADevolver

    @staticmethod
    def obtenerRobotMasBarato(robots):
        #Buscamos el mas barato
        masBarato = min([robot.obtenerCosto() for robot in robots])
        #devolvemos una lista filtrada con el/los robots que tengan el valor más barato
        robotsADevolver = []
        for robot in robots:
            if robot.obtenerCosto() == masBarato:
                robotsADevolver.append(robot)
        return robotsADevolver



    
    