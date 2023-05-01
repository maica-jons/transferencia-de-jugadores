import datetime
import math
import Persona
import Club

class Jugador(Persona):

    #lista_jugadores = []

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, cantidad_tarjetas):
        Persona.__init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso)
        self.valor = valor
        self.club = club
        self.estado = estado   # (Estado físico)
        self.cantidad_partidos = cantidad_partidos
        self.cantidad_tarjetas = cantidad_tarjetas

    def retirar_jugador(self):
        pass

    def modificar_valor(self, nuevo):
        self.valor = nuevo
        return self.valor
        
    def modificar_estado(self, nuevo):
        self.estado = nuevo
        return self.estado
