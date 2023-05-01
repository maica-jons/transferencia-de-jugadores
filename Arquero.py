from Jugador import Jugador

class Arquero(Jugador):
    def __init__(self, nombre, apellido, dni, fechanacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, vallas_invictas, goles_recibidos):
        Jugador.__init__(self, nombre, apellido, dni, fechanacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos)
        self.vallas_invictas = vallas_invictas
        self.goles_recibidos = goles_recibidos

    def TenerVallaInvicta(self):
        self.vallas_invictas += 1

    def RecibirGol(self):
        self.goles_recibidos += 1
    
    def __str__(self):
        return("El nombre del jugador es {} {}, cuyo DNI es {}, nacio en la fecha {}, y cuya nacionalidad es {}. Su estatura es {} metros, su peso es {} kg. Su valor es {}, pertenece al club {}. Su estado actual es {}, tiene {} partidos jugados, tiene {} vallas invictas, y tiene {} goles recibidos. ").format(self.nombre, self.apellido, self.dni, self.fecha_nacimiento, self.nacionalidad, self.estatura, self.peso, self.valor, self.club, self.estado, self.cantidad_partidos, self.vallas_invictas, self.goles_recibidos)