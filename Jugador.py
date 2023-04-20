import datetime
import math
import Persona

class Jugador(Persona):

    # lista_jugadores = []

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, cantidad_tarjetas):
        Persona.__init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso)
        self.valor = valor
        self.club = club 
        self.estado = estado   # (estado fisico)
        self.cantidad_partidos = cantidad_partidos
        self.cantidad_tarjetas = cantidad_tarjetas

    #validaciones aca adentro

    # def CalcularEdad(self):
    #     fechanacimiento = datetime.datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y").date()
    #     fecha_actual = datetime.date.today()
    #     diferencia = fecha_actual - fechanacimiento
    #     edad = math.floor(diferencia.days / 365)
    #     return edad

    # def verificardni_jugador(self,lista_jugadores):
    #     while self.dni in lista_jugadores:
    #         print("El dni del jugador ya existe. Ingrese otro.")
    #         self.nombre = str(input("Ingrese nombre del jugador: "))
    #         self.dni = int(input("Ingrese dni del jugador: "))
    #     lista_jugadores.append(self.dni)
    #     print("Jugador cargado exitosamente.")
    #     return lista_jugadores

    def CrearJugador(self): #todo esto dentro del main. usuario solo interactua con el main. 
        nombre = input("Ingrese el nombre del jugador: ")
        apellido = input("Ingrese el apellido del jugador: ")
        fechanacimiento = input("Ingrese la fecha de nacimiento del jugador en formato dd/mm/aaaa: ")  #ver si hay que usar datetime
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
