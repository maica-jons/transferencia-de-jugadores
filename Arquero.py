import Jugador

class Arquero(Jugador):
    def __init__(self, nombre, apellido, dni, fechanacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos, vallas_invictas, goles_recibidos):
        Jugador.__init__(self, nombre, apellido, dni, fechanacimiento, nacionalidad, estatura, peso, valor, club, estado, cantidad_partidos)
        self.vallas_invictas = vallas_invictas
        self.goles_recibidos = goles_recibidos

    def TenerVallaInvicta(self):
        self.vallas_invictas += 1

    def RecibirGol(self):
        self.goles_recibidos += 1

    # def validar_vallas_invictas(self):
    #     while self.vallas_invictas < 0:
    #         self.vallas_invictas = int(input("Ingrese un numero valido de vallas invictas: "))
    #     return self.vallas_invictas
    
    def validar_goles_recibidos(self):
        while self.goles_recibidos < 0:
            self.goles_recibidos = int(input("Ingrese una cantidad valida de goles recibidos: "))
        return self.goles_recibidos