import Jugador

class Arquero(Jugador):
    def __init__(self, nombre, apellido, dni, fechanacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, vallas_invictas, goles_recibidos, penales_atajados):
        Jugador.__init__(self, nombre, apellido, dni, fechanacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos)
        self.vallas_invictas = vallas_invictas
        self.goles_recibidos = goles_recibidos
        self.penales_atajados = penales_atajados

    def AtajarPenal(self):
        pass

    def TenerVallaInvicta(self):
        pass
        