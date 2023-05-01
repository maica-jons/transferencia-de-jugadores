from Jugador import Jugador
from Liga import Liga

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
            club_vendedor.presupuesto += jugador.valor
            club_vendedor.valor_del_club -= jugador.valor
            print("Jugador comprado correctamente.")
        else:
            print("No hay presupuesto suficiente para comprar ese jugador.")

    def modificar_presupuesto(self, monto):
        self.presupuesto += monto
        print("El nuevo presupuesto del club es", self.presupuesto)
    
    def __str__(self):
        return("El nombre del club es {}, cuyo ID es {}. El nombre de la liga a la que pertenece es {}, tiene {} de presupuesto y {} de valor. La lista de los jugadores que tiene el club es {}").format(self.nombre, self.id, self.liga, self.presupuesto, self.valor_del_club, self.lista_jugadores)