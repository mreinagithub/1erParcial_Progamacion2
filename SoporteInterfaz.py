
from Clases.Robot import Robot
from Clases.SondaTerrestre import SondaTerrestre
from Clases.SondaEspacial import SondaEspacial
from Clases.Explorador import Explorador

def mostrarMenuPrincipal():
    limpiarPantalla()
    menu = ("Alta de Robot", "Mostrar Robots", "Obtener Robot cuya batería se acaba más rapido", "Obtener robot más caro",
            "Obtener robot más barato","Obtener total de días en funcionamiento de todos los robots",
            "Comparar costos robots","Sumar un día de funcionamiento a todos los robots") 
    encabezado = "#################################\n######## MENU PRINCIPAL #########\n#################################"
    opcionSalida = "Salir del sistema"
    textoInput = "Seleccione la opción deseada:"

    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione una opción:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    return opt;

def mostrarRobotsParaComparar(robots):
    limpiarPantalla()
    menu = [r.nombre for r in robots]
    encabezado = "#################################\n#### COMPARACIÓN DE ROBOTS #####\n#################################"
    opcionSalida = "Volver al menú anterior"

    #Seleccion primer robot
    textoInput = "Seleccione el primer robot:"   
    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione el primer robot:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    if(opt == "0"): return opt
    r1 = robots[int(opt)-1]
    #Seleccion segundo robot
    limpiarPantalla()
    textoInput = "Seleccione el segundo robot:"
    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione el segundo robot:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)    
    if(opt == "0"): return opt
    r2 = robots[int(opt)-1]
    return r1, r2,

def altaRobot(robots):
    limpiarPantalla()
    #Variables
    tipoRobot = None
    nombre = None 
    alto = None 
    ancho = None
    kilos = None 
    costo = None    
    bateriaAmperes = None
    bateriaPeso = None
    bateriaCosto = None
    velocidadMaxima = None
    consumo = None
    altitud = None
    consumoMinimo = None
    sensorSismo = None
    sensorViento = None
    sensorCalor = None   
    camaras = []
    qCamaras = 0
    #Inputo de datos   
    tipos = sorted([s for s in Robot.__subclasses__()], key = lambda s: s.__name__)
    menu = [s.__name__ for s in tipos]
    opcionSalida = "Cancelar alta"
    textoInput = "Seleccione la opción según el tipo de robot que desea crear:"
    opt = generarPantalla("", menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta.\nSeleccione la opción según el tipo de robot que desea crear:"
        limpiarPantalla()
        opt = generarPantalla("", menu, opcionSalida, textoInput)
    if(opt == "0"): return
    tipoRobot = tipos[int(opt)-1]
    print(f"-----> {tipoRobot.__name__}")
    while(nombre is None):
        nombre = procesarYValidarInput("Indique el NOMBRE del Robot (0 para cancelar): ",str)
        if(nombre is not None):
            if(nombre == "0"): return
            if(len(nombre) < 3): 
                print("El nombre debe tener al menos 3 caractéres")
                nombre = None
            elif(any([r.nombre.upper() == nombre.upper() for r in robots])):
                print("El nombre de robot ya existe ingresado.")
                nombre = None
    while(alto is None):
        alto = procesarYValidarInput("Indique el ALTO en métros del Robot (0 para cancelar): ",float)
        if(alto is not None):
            if(alto == "0"): return
            if(alto < 0): 
                print("El alto no puede ser negativo.")
                alto = None
    while(ancho is None):
        ancho = procesarYValidarInput("Indique el ANCHO en métros del Robot (0 para cancelar): ",float)
        if(ancho is not None):
            if(ancho == "0"): return
            if(ancho < 0): 
                print("El ancho no puede ser negativo.")
                ancho = None
    while(kilos is None):
        kilos = procesarYValidarInput("Indique el PESO en kilogramos del Robot (0 para cancelar): ",float)
        if(kilos is not None):
            if(kilos == "0"): return
            if(kilos < 0): 
                print("El peso en kg no puede ser negativo")
                kilos = None
    while(costo is None):
        costo = procesarYValidarInput("Indique el COSTO en dólares del Robot (0 para cancelar): ",float)
        if(costo is not None):
            if(costo == "0"): return
            if(costo < 0): 
                print("El costo no puede ser negativo")
                costo = None
    if(tipoRobot == Explorador):
        while(velocidadMaxima is None):
            velocidadMaxima = procesarYValidarInput("Indique la VELOCIDAD MÁXIMA en Km/h del Robot (0 para cancelar): ",float)
        if(velocidadMaxima is not None):
            if(velocidadMaxima == "0"): return
            if(velocidadMaxima < 0): 
                print("La velocidad máxima no puede ser negativa")
                velocidadMaxima = None
        while(consumo is None):
            consumo = procesarYValidarInput("Indique el CONSUMO por desplazamiento en ampéres/hora del Robot (0 para cancelar): ",float)
        if(consumo is not None):
            if(consumo == "0"): return
            if(consumo < 0): 
                print("El consumo no puede ser negativo")
                consumo = None
    elif(tipoRobot == SondaEspacial):
        while(altitud is None):
            altitud = procesarYValidarInput("Indique la ALTITUD MÍNIMA en Km del Robot (0 para cancelar): ",float)
        if(altitud is not None):
            if(altitud == "0"): return
            if(altitud < 0): 
                print("La altitud mínima no puede ser negativa")
                altitud = None
        while(consumoMinimo is None):
            consumoMinimo = procesarYValidarInput("Indique el CONSUMO MINIMO en ampéres/hora del Robot (0 para cancelar): ",float)
        if(consumoMinimo is not None):
            if(consumoMinimo == "0"): return
            if(consumoMinimo < 0): 
                print("El consumo mínimo no puede ser negativo")
                consumoMinimo = None
    elif(tipoRobot == SondaTerrestre):
        while(sensorSismo is None):
            sensorSismo = procesarYValidarInput("Indique el CONSUMO del sensor de SISMOS en ampéres/hora del Robot (0 para cancelar): ",float)
        if(sensorSismo is not None):
            if(sensorSismo == "0"): return
            if(sensorSismo < 0): 
                print("El consumo del sensor de sismos no puede ser negativo")
                sensorSismo = None
        while(sensorViento is None):
            sensorViento = procesarYValidarInput("Indique el CONSUMO del sensor de VIENTO en ampéres/hora del Robot (0 para cancelar): ",float)
        if(sensorViento is not None):
            if(sensorViento == "0"): return
            if(sensorViento < 0): 
                print("El consumo del sensor de viento no puede ser negativo")
                sensorViento = None
        while(sensorCalor is None):
            sensorCalor = procesarYValidarInput("Indique el CONSUMO del sensor de CALOR en ampéres/hora del Robot (0 para cancelar): ",float)
        if(sensorCalor is not None):
            if(sensorCalor == "0"): return
            if(sensorCalor < 0): 
                print("El consumo del sensor de calor no puede ser negativo")
                sensorCalor = None
    else:
        print("No se encontró el tipo de robot especificado")
        esperarYVolver()
        return

    print("-------------------------------")
    print("ACERCA DE LA BATERIA:")
    while(bateriaAmperes is None):
        bateriaAmperes = procesarYValidarInput("Indique los AMPERES/HORA de la batería (0 para cancelar): ",float)
        if(bateriaAmperes is not None):
            if(bateriaAmperes == "0"): return
            if(bateriaAmperes < 0): 
                print("El amperaje de la batería no puede ser negativo")
                bateriaAmperes = None
    while(bateriaPeso is None):
        bateriaPeso = procesarYValidarInput("Indique el PESO en kilogramos de la batería (0 para cancelar): ",float)
        if(bateriaPeso is not None):
            if(bateriaPeso == "0"): return
            if(bateriaPeso < 0): 
                print("El peso de la batería no puede ser negativo")
                bateriaPeso = None
    while(bateriaCosto is None):
        bateriaCosto = procesarYValidarInput("Indique el COSTO en dólares de la batería (0 para cancelar): ",float)
        if(bateriaCosto is not None):
            if(bateriaCosto == "0"): return
            if(bateriaCosto < 0): 
                print("El costo de la batería no puede ser negativo")
                bateriaCosto = None
    print("-------------------------------")
    print("ACERCA DE LAS CAMARAS (todo robot debe tener al menos una cámara):")
    masCamaras = ""
    while masCamaras.upper() != "F":
        qCamaras += 1
        camaraAlcance = None
        camaraZoom = None
        camaraMP = None
        camaraConsumo = None
        camaraKilos = None
        camaraCosto = None
        while(camaraAlcance is None):            
            camaraAlcance = procesarYValidarInput(f"Indique el ALCANCE en métros de la cámara {qCamaras} (0 para cancelar): ",float)
            if(camaraAlcance is not None):
                if(camaraAlcance == "0"): return
                if(camaraAlcance < 0): 
                    print("El alance de la cámara no puede ser negativo")
                    camaraAlcance = None
        while(camaraZoom is None):            
            camaraZoom = procesarYValidarInput(f"Indique el ZOOM en X distancia focal de la cámara {qCamaras} (0 para cancelar): ",int)
            if(camaraZoom is not None):
                if(camaraZoom == "0"): return
                if(camaraZoom < 0): 
                    print("El zoom de la cámara no puede ser negativo")
                    camaraZoom = None
        while(camaraMP is None):            
            camaraMP = procesarYValidarInput(f"Indique los Pixeles en millones de la cámara {qCamaras} (0 para cancelar): ",int)
            if(camaraMP is not None):
                if(camaraMP == "0"): return
                if(camaraMP < 0): 
                    print("Los Pixeles de la cámara no pueden ser negativos")
                    camaraMP = None
        while(camaraConsumo is None):            
            camaraConsumo = procesarYValidarInput(f"Indique el CONSUMO en amperes/hora de la cámara {qCamaras} (0 para cancelar): ",float)
            if(camaraConsumo is not None):
                if(camaraConsumo == "0"): return
                if(camaraConsumo < 0): 
                    print("El consumo de la cámara no puede ser negativo")
                    camaraConsumo = None
        while(camaraKilos is None):            
            camaraKilos = procesarYValidarInput(f"Indique el PESO en Kg. de la cámara {qCamaras} (0 para cancelar): ",float)
            if(camaraKilos is not None):
                if(camaraKilos == "0"): return
                if(camaraKilos < 0): 
                    print("El peso de la cámara no puede ser negativo")
                    camaraKilos = None
        while(camaraCosto is None):            
            camaraCosto = procesarYValidarInput(f"Indique el COSTO en dólares de la cámara {qCamaras} (0 para cancelar): ",float)
            if(camaraCosto is not None):
                if(camaraCosto == "0"): return
                if(camaraCosto < 0): 
                    print("El costo de la cámara no puede ser negativo")
                    camaraCosto = None
        
        camaras.append([camaraAlcance,camaraZoom, camaraMP, camaraConsumo, camaraKilos, camaraCosto])
        masCamaras = input("¿Desea ingresar más cámaras? (Presione 'F' para Finalizasr o cualquier tecla para seguir agregando):")
    
    
    nuevoRobot = None
    if(tipoRobot == Explorador):
        nuevoRobot = Explorador(nombre,[alto,ancho],camaras,
                                [bateriaAmperes,bateriaPeso,bateriaCosto],kilos,costo,velocidadMaxima,consumo)
    elif(tipoRobot == SondaEspacial):
       nuevoRobot = SondaEspacial(nombre,[alto,ancho],camaras,
                                  [bateriaAmperes,bateriaPeso,bateriaCosto],kilos,costo,altitud,consumoMinimo)
    elif(tipoRobot == SondaTerrestre):
        nuevoRobot = SondaTerrestre(nombre,[alto,ancho],camaras,
                                    [bateriaAmperes,bateriaPeso,bateriaCosto],kilos,costo,sensorSismo,sensorViento,sensorCalor)

    if(nuevoRobot is not None):
        print("-------------------------------")
        print("Robot dado de alta -->")
        print(nuevoRobot)
        robots.append(nuevoRobot)
        esperarYVolver()
            
        

def procesarYValidarInput(textoInput, validarComo):
    
    dato = input(textoInput)
    if(dato == "0"):
        return dato
    if(dato == ""):
        print("El campo no puede estar vacío")
        return None
    try:
        datoPars = validarComo(dato)
    except Exception:
        print("El formato ingresado es inválido")
        return None
    else:     
        return datoPars


def limpiarPantalla():    
    import os
    os.system("cls")

def generarPantalla(encabezado, menu, opcionSalida, textoInput):    
    print(encabezado)    
    indice = 1
    for item in menu:
        print(f"{indice} - {item}")
        indice += 1    
    print(f"{0} - {opcionSalida}")
    return input(textoInput)

def esperarYVolver():
    print("\n")
    input("Presione ENTER para continuar.")



