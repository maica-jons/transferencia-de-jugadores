from Jugador import Jugador

class JugadorDeCampo(Jugador):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, goles, asistencia):
        Jugador.__init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos)
        self.goles = goles
        self.asistencia = asistencia

    def HacerGol(self):
        self.goles += 1
        
    def DarAsistencia(self):
        self.asistencia += 1
    
    def __str__(self):
        return("El nombre del jugador es {} {}, cuyo DNI es {}, nacio en la fecha {}, y cuya nacionalidad es {}. Su estatura es {} metros, su peso es {} kg. Su valor es {}, pertenece al club {}. Su estado actual es {}, tiene {} partidos jugados, hizo {} goles, y tiene {} asistencias. ").format(self.nombre, self.apellido, self.dni, self.fecha_nacimiento, self.nacionalidad, self.estatura, self.peso, self.valor, self.club, self.estado, self.cantidad_partidos, self.goles, self.asistencia)