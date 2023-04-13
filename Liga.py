from Club import *

class Liga():
    lista_ligas = [] #total de ligas
    lista_paises_ligas = [] #cada pais tiene maximo 1 liga (si creo una liga en un pais que ya tiene, no me deja)
    def __init__(self,nombre,pais):
        if nombre in Liga.lista_ligas:
            raise ValueError("La liga ya fue creada.")
        else:
            Liga.lista_ligas+=nombre
        self.nombre = nombre
        self.pais = pais
        self.lista_clubes = [] #clubes de cada liga
        self.cant_clubes = 0
    def ingresar_club_a_liga(self,club:Club):
        

    def validar_club(self,club):
        pass
