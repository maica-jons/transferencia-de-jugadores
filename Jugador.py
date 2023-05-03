import datetime
import math
from Persona import Persona
from Club import Club

class Jugador(Persona):

    #lista_jugadores = []

    def __init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, cantidad_tarjetas, posicion):
        Persona.__init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso)
        self.valor = valor
        self.club = club
        self.estado = estado   # (Estado físico)
        self.cantidad_partidos = cantidad_partidos
        self.cantidad_tarjetas = cantidad_tarjetas
        self.posicion=posicion

    def retirar_jugador(self, club): 
        self.estado = "Retirado"
        self.club = ""
        for i in range(len(club.lista_jugadores)):
            if self.dni == club.lista_jugadores[i].dni:
                club.lista_jugadores.remove(club.lista_jugadores[i])
        print("Jugador retirado.")

    def modificar_valor(self):
        monto = float(input("Ingrese el monto en el que varió el valor del jugador (Si es negativo ponga un '-' antes del número): "))
        self.valor += monto
        print("El nuevo valor del jugador es", self.valor)
        
    def modificar_estado(self):
        if self.estado == "Activo":
            self.estado = "Lesionado"
        else:
            self.estado = "Activo"
        print("El nuevo estado del jugador es", self.estado)
