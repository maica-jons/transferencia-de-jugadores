from Jugador import Jugador

class Club():
    lista_clubes=[]
    def __init__(self, nombre, id, liga, presupuesto=100000, valor_del_club=0):
        self.nombre=nombre
        self.id=id
        self.liga=liga
        self.presupuesto=presupuesto
        self.valor_del_club=valor_del_club
        self.lista_jugadores=[]

    def verificarid_club(self,lista_clubes):
        while self.id in lista_clubes:
            print("El id del club ya existe. Ingrese otro.")
            self.nombre=str(input("Ingrese nombre del club: "))
            self.id=int(input("Ingrese id del club: "))
        lista_clubes.append(self.id)
        print("Club cargado exitosamente.")
        return lista_clubes

    def comprar_jugador(self, club_vendedor, jugador):
        if jugador.valor <= self.presupuesto:
            club_vendedor.lista_jugadores.remove(jugador)
            self.lista_jugadores.append(jugador)
            jugador.club=self.nombre
            self.presupuesto-=jugador.valor
            self.valor_del_club+=jugador.valor
        else:
            print("No hay presupuesto suficiente para comprar ese jugador.")

