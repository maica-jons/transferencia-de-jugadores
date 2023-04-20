from Club import *
from JugadorDeCampo import *
from Arquero import *

class Liga():
    lista_ligas = [] #total de ligas
    lista_paises_ligas = [] #cada pais tiene maximo 1 liga (si creo una liga en un pais que ya tiene, no me deja)

    def __init__(self,nombre,pais):
        if nombre in Liga.lista_ligas:
            raise ValueError("La liga ya fue creada.")
        else:
            Liga.lista_ligas += nombre
        self.nombre = nombre
        self.pais = pais
        self.lista_clubes = [] #clubes de cada liga
        self.cant_clubes = 0
        cant_partidos_liga = 0

    def jugar_partido(self,club1,club2):
        goles = input("ingrese s si HUBO goles y n si NO HUBO goles: ")
        while goles != "s" and goles != "n":
            goles = input("no ingreso una opcion valida. ingrese s si HUBO goles y n si NO HUBO goles: ")
        while goles == "s":
            que_club = input("que club hizo gol? para titular ingrese t, para visitante ingrese v: ")
            if que_club == "t":
                goleador = input("ingrese el nombre del jugador que metio gol: ")
                for i in range(len(club1.lista_jugadores)):
                    if goleador == club1.lista_jugadores[i][0]:
                        goleador = club1.lista_jugadores[i]
                        goleador = JugadorDeCampo.HacerGol()
                        arquero = club2.lista_jugadores[i][posicion=arq]
                        arquero = Arquero.RecibirGol()
                    else:
                        print("el jugador ingresado no existe.")
            else: #club visitante
                goleador = input("ingrese el nombre del jugador que metio gol: ")
                for i in range(len(club2.lista_jugadores)):
                    if goleador == club2.lista_jugadores[i][0]:
                        goleador = club2.lista_jugadores[i]
                        goleador = JugadorDeCampo.HacerGol()
                        arquero = club1.lista_jugadores[i][posicion=arq]
                        arquero = Arquero.RecibirGol()
                    else:
                        print("el jugador ingresado no existe.")
            assist = input("el gol tuvo asistencia? ingrese s o n: ")
            while assist != "s" and assist != "n":
                assist = input("ingrese una respuesta válida. si el gol tuvo asistencia ingrese s, si no ingrese n: ")
            while assist == "s":
                asistente = input("ingrese el nombre del jugador que realizo la asistencia: ")
                for i in range(len(que_club.lista_jugadores)):
                    if asistente == que_club.lista_jugadores[i][0]:
                        asistente = que_club.lista_jugadores[i]
                        asistente = 
            goles = input("si hubo mas goles, ingrese s, si no, ingrese n: ")
            while goles != "s" or goles != "n":
                goles = input("no ingreso una opcion valida. ingrese s si HUBO goles y n si NO HUBO goles: ")
        

            
#preguntar si hubo asistencia y si hubo ingresarsela al jugador que la hizo


    while hasta que sea no
    asistencia
    tarjetas
    cont de goles 0
    valla invicta si termina en 0
