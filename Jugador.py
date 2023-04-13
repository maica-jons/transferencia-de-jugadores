import datetime

class Jugador():

    lista_jugadores = []

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        self.valor = valor
        self.club = club 
        self.estado = estado 
        self.cantidad_partidos = cantidad_partidos
        
    #validaciones aca adentro

    def CrearJugador(self): #todo esto dentro del main. usuario solo interactua con el main. 
        nombre = input("Ingrese el nombre del jugador: ")
        apellido = input("Ingrese el apellido del jugador: ")
        fechanacimiento = input("Ingrese la fecha de nacimiento del jugador: ")  #ver si hay que usar datetime
        nacionalidad = input("Ingrese la nacionalidad del jugador: ")
        estatura = int(input("Ingrese la estatura del jugador: "))
        peso = float(input("Ingrese el peso del jugador: "))
        valor = float(input("Ingrese el valor del jugador: "))
        club = input("Ingrese el club al que pertenece el jugador: ")
        estado = input("Ingrese el estado del jugador (si esta lesionado o no): ")

    def RetirarJugador(self):
        pass

    def ModificarJugador(self):
        pass
