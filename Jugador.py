import datetime
import math
import Persona
import Club

class Jugador(Persona):

    # lista_jugadores = []

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, cantidad_tarjetas):
        Persona.__init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso)
        self.valor = valor
        self.club = club 
        self.estado = estado   # (Estado físico)
        self.cantidad_partidos = cantidad_partidos
        self.cantidad_tarjetas = cantidad_tarjetas

    def validar_valor(self):
        while self.valor <= 0 or self.valor >= 2000000:
            self.valor = float(input("Ingrese nuevamente un valor del jugador válido: "))
        return self.valor
    
    def validar_club(self):
        while self.club in Club.lista_clubes:
            self.club = input("Ingrese un club que se encuentre creado: ")
        return self.club
        
    def validar_estado(self):
        while self.estado != "Activo" and self.estado != "activo" and self.estado != "Lesionado" and self.estado != "lesionado":
            self.estado = input("Ingrese nuevamente un estado físico del jugador correctamente: ")
        return self.estado

    def validar_cantidad_partidos(self):
        while self.cantidad_partidos < 0:
            self.cantidad_partidos = int(input("Ingrese 0 o la cantidad de partidos que disputó el jugador correctamente: "))
        return self.cantidad_partidos
    
    def validar_cantidad_tarjetas(self):
        while self.cantidad_tarjetas < 0:
            self.cantidad_tarjetas = int(input("Ingrese 0 o la cantidad de tarjetas que le sacaron al jugador correctamente: "))
        return self.cantidad_tarjetas

    def CrearJugador(self): #todo esto dentro del main. usuario solo interactua con el main. 
        nombre = input("Ingrese el nombre del jugador: ")
        apellido = input("Ingrese el apellido del jugador: ")
        fechanacimiento = input("Ingrese la fecha de nacimiento del jugador en formato dd/mm/aaaa: ")  #ver si hay que usar datetime
        nacionalidad = input("Ingrese la nacionalidad del jugador: ")
        estatura = int(input("Ingrese la estatura en metros del jugador: "))
        peso = float(input("Ingrese el peso en kilogramos del jugador: "))
        valor = float(input("Ingrese el valor del jugador: "))
        club = input("Ingrese el club al que pertenece el jugador: ")
        estado = input("Ingrese el estado del jugador (si esta lesionado o no): ")

    def RetirarJugador(self):
        pass

    def ModificarJugador(self):
        pass
