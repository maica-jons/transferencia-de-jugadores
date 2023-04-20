from Club import *
from JugadorDeCampo import *

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
        while goles != "s" or goles != "n":
            goles = input("no ingreso una opcion valida. ingrese s si HUBO goles y n si NO HUBO goles: ")
        while goles == "s":
            que_club = input("que club hizo gol? para titular ingrese t, para visitante ingrese v: ")
            if que_club == "t":
                goleador = input("ingrese el nombre del jugador que metio gol: ")
                for i in range(len(club1.lista_jugadores)):
                    if goleador == club1.lista_jugadores[i][0]:
                        goleador = club1.lista_jugadores[i]
                        goleador = JugadorDeCampo.HacerGol()

        

    # hubo goels
    #     quien
    #     ingresarlo
    # sumarle +1
    # while hasta que sea no
    # asistencia
    # tarjetas
    # cont de goles 0
    # valla invicta si termina en 0
