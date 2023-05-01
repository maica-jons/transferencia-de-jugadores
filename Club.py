from Jugador import Jugador
import Liga

class Club():
    lista_clubes = []
    lista_id_clubes = []
    def __init__(self, nombre, id, liga, presupuesto = 100000):
        self.nombre = nombre
        self.id = id
        self.liga = liga
        self.presupuesto = presupuesto
        self.valor_del_club = 0
        self.lista_jugadores = []
    
    def comprar_jugador(self, club_vendedor, jugador):
        if jugador.valor <= self.presupuesto:
            club_vendedor.lista_jugadores.remove(jugador)
            self.lista_jugadores.append(jugador)
            jugador.club = self.nombre
            self.presupuesto -= jugador.valor
            self.valor_del_club += jugador.valor
        else:
            print("No hay presupuesto suficiente para comprar ese jugador.")

    def modificar_presupuesto(self, nuevo):
        self.presupuesto = nuevo
        return self.presupuesto
    
    def __str__(self):
        return("Nombre del club: {}, id del club: {}, nombre de la liga a la que pertenece: {}, presupuesto del club: {}, valor del club: {} y lista de los jugadores que tiene el club:").format(self.nombre,self.id,self.liga,self.presupuesto,self.valor_del_club,self.lista_clubes)