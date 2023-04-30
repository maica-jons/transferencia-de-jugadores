import Jugador

class JugadorDeCampo(Jugador):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, goles, asistencia):
        Jugador.__init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos)
        self.goles = goles
        self.asistencia = asistencia

    def HacerGol(self):
        self.goles += 1
        
    def DarAsistencia(self):
        self.asistencia += 1

    # def validar_goles(self):
    #     while self.goles < 0:
    #         self.goles = int(input("Ingrese nuevamente una cantidad de goles valida: "))
    #     return self.goles
    
    def validar_asistencia(self):
        while self.asistencia < 0:
            self.asistencia = int(input("Ingrese nuevamente una cantidad de asistencia: "))
        return self.asistencia
