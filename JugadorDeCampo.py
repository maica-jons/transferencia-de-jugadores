import Jugador

class JugadorDeCampo(Jugador):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, goles, asistencia):
        Jugador.__init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos)
        self.goles = goles
        self.asistencia = asistencia

    def HacerGol(self):
        self.goles+=1
        

    def DarAsistencia(self):
        self.asistencia+=1
        