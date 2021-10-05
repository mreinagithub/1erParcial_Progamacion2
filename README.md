# 1erParcial_Progamacion2
1er Parcial de la matería Programación 2, hecho en Python.

### Contenido del cuestionario

Los elementos comunes que se requieren cargar en los robots son:

- Nombre
- Dimensiones 
- Cámaras
- Batería
- Días de funcionamiento (atributo que debe actualizarse diariamente)

Los tipos de robots son:
- Exploradores que permiten desplazarse para los que se registra la velocidad máxima, el consumo de energía del desplazamiento.
- Las sondas que pueden ser de tierra, que poseen sensores para medir sismos, vientos y calor. Cada sensor debe tener un consumo especificado por el fabricante.
- las sondas espaciales que orbitan un cuerpo celeste, del que se registra la altitud mínima requerida, y el consumo mínimo de sus funcionalidades.

Las baterías tienen una capacidad que se mide en horas de uso.

De las cámaras se registra el alcance, zoom, megapixels y consumos.

De todos los elementos se registra el peso en kilos, y el costo en dólares.

Desarrollar un sistema orientado a objetos en Python que permita:

1) Alta de robots 
2) Buscar el robot cuya batería se consuma más rápido en función del consumo de sus componentes
3) Obtener el robot más caro
4) Obtener el robot más barato
5) Obtener la cantidad total de días de funcionamiento de todos los robots utilizando "reduce"
6) Crear una función estática que permita comparar la diferencia de costos entre los robots
7) Crear una función que incremente en 1 la cantidad de días que los robots van funcionando utilizando "map"
8) Control de carga de datos y manejo de excepciones
