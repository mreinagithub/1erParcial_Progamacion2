from SoporteInterfaz import *
from Clases.SondaTerrestre import SondaTerrestre
from Clases.SondaEspacial import SondaEspacial
from Clases.Explorador import Explorador
from SoporteCalculos  import SoporteCalculos

robots = []

def main():

    precargarRobots()
    opt = ""
    while True:        
        #bucle hasta que eliga salir del sistema
        opt = mostrarMenuPrincipal()
        if(opt == "0"):
            #decidió salir del sistema
            print("\n")
            print("GRACIAS POR VISITAR MI PROGRAMA !!!")
            quit()   
        else:
            procesarSeleccion(opt)



def precargarRobots():

    #nombre, alto, ancho, camara: alcance, zoom, mpx, consumo, kg, costo; bateria: amperes, kg, costo; kg, costo, vmax, consumo
    robots.append(Explorador("Rover",[3,5],[[1500,10,65,10,100,1500],[3800,10,65,20,80,3580]],[3500,250,980],1780,18990,55,50))
    #Bateria: 3500Ah
    #Consumo total: 10+20+50=80Ah
    #Autonomia: 43.75Hs
    #Costo total: 1500+3580+980+18990= usd 25050
    robots.append(Explorador("Curiosity",[2.55,3.78],[[9280.25,20,190,33,50,2360],[10110,25,250,35,80,3580]],[8266,250,1980],1990,25260,75,73.1))
    #Bateria: 8266Ah // 
    #Consumo total: 33+35+73.1=141.1Ah
    #Autonomia: 58.58Hs
    #Costo total: 2360+3580+1980+25260= usd 33180

    #nombre, alto, ancho, camara: alcance, zoom, mpx, consumo, kg, costo; bateria: amperes, kg, costo; kg, costo, conssismo, consviento, conscalor
    robots.append(SondaTerrestre("Sputnik I",[2,2],[[8260,55,365,29,13,7690],[10665,65,365,30.7,15,6760],[3220,25,190,25,80,1320]],[4290,30,1870],220,5360,25,10,15))
    #Bateria: 4290Ah
    #Consumo total: 29+30.7+25+25+10+15=134.7Ah
    #Autonomia: 31.85Hs
    #Costo total: 7690+6760+1320+1870+5360= usd 23000
    robots.append(SondaTerrestre("Nahuel 1A",[3,8],[[15266,110,1260,17,10,3760],[18256,55,1000,18,20,5320]],[9900,30,9870],2000,19879,14,10,20))
    #Bateria: 9900Ah
    #Consumo total: 17+18+14+10+20=79Ah
    #Autonomia: 125.35Hs
    #Costo total: 3760+5320+9870+19879= usd 38829

    #nombre, alto, ancho, camara: alcance, zoom, mpx, consumo, kg, costo; bateria: amperes, kg, costo; kg, costo, altitud, consMinimo
    robots.append(SondaEspacial("Voyager I",[7,8.53],[[99290,800,9290,35,25,8000]],[12320,25,1180],1300,88890,37000,95))
    #Bateria: 12320Ah
    #Consumo total: 35+95=130Ah
    #Autonomia: 94.77Hs
    #Costo total: 8000+1180+88890= usd 98070
    robots.append(SondaEspacial("Voyager II",[5.34,6],[[85000,750,7248,22,20,7660],[85000,750,7248,22,20,7660]],[10000,20,1260],1190,78260,37000,90))
    #Bateria: 10000Ah
    #Consumo total: 22+22+90=134Ah
    #Autonomia: 74.63Hs
    #Costo total: 7660+7660+1260+78260= usd 94840

def procesarSeleccion(opt):
    if(opt == "1"):
        altaRobot(robots)                    
    if(opt == "2"):
        limpiarPantalla()
        print("Robots en funcionamiento:")
        for robot in robots:
            print(f"-> {robot}")
            print("------------------------------------------------------------------------------")
        esperarYVolver()
    if(opt == "3"):
        limpiarPantalla()
        print("Robots cuya batería se agota más rapido (con relación al consumo de sus elementos)")
        robotosDurMin = SoporteCalculos.obtenerRobotMenorDuracionBateria(robots)    
        for robot in robotosDurMin:        
            print("--->")
            print(f"Nombre: {robot.nombre}")        
            print(f"Bateria: {robot.bateria.amperesHora}Ah")
            print(f"Consumo total: {robot.consumoTotal()}Ah")
            print(f"Duracion bateria en horas: {robot.estimarDuracionBateria():.2f}")
            esperarYVolver()
    if(opt == "4"):
        limpiarPantalla()
        print("Robots más CAROS según el precio de dólares de sus elementos")
        robotsMasCaros = SoporteCalculos.obtenerRobotMasCaro(robots)    
        for robot in robotsMasCaros:        
            print("--->")
            print(f"Nombre: {robot.nombre}")        
            print(f"El costo total del robot es de: USD{robot.obtenerCosto():.2f}")
            esperarYVolver()
    if(opt == "5"):
        limpiarPantalla()
        print("Robots más BARATOS según el precio de dólares de sus elementos")
        robotsMasBaratos = SoporteCalculos.obtenerRobotMasBarato(robots)    
        for robot in robotsMasBaratos:        
            print("--->")
            print(f"Nombre: {robot.nombre}")        
            print(f"El costo total del robot es de: USD{robot.obtenerCosto():.2f}")
            esperarYVolver()
    if(opt == "6"):
        limpiarPantalla()        
        ttlDiasFuncionando = SoporteCalculos.obtenerTotalDiasFuncionamiento(robots)    
        print(f"El total de días de funcionamiento de todos los robots es de: {ttlDiasFuncionando}")
        esperarYVolver()
    if(opt == "7"):
        seleccion = mostrarRobotsParaComparar(robots)
        if(seleccion != "0"):
            limpiarPantalla()
            if seleccion[0] == seleccion[1]:
                print("Ha seleccionado el mismo robot; no se puede realizar la comparación")
            else: 
                print("Comparación de costos:")
                SoporteCalculos.compararCostos(seleccion[0], seleccion[1])
            esperarYVolver()        
    if(opt == "8"):
        limpiarPantalla()
        SoporteCalculos.aumentarDiasFuncionando(robots)
        print("Se a incrementado el total de días en funcionamiento de cada robot.")
        esperarYVolver()


if __name__ == "__main__":
    main()



 



