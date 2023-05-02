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
            club_vendedor.presupuesto += jugador.valor
            club_vendedor.valor_del_club -= jugador.valor
            print("Jugador comprado correctamente.")
        else:
            print("No hay presupuesto suficiente para comprar ese jugador.")

    def modificar_presupuesto(self, monto):
        self.presupuesto += monto
        print("El nuevo presupuesto del club es", self.presupuesto)
    
    def buscar_arquero_valla_invicta(self):
        for i in range(len(self.lista_jugadores)):
            if self.lista_jugadores[i].posicion == "Arquero":
                print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_a='no'
        while esta_a=='no':   
            arquero= int(input("ingrese el dni del arquero que no recibio goles: "))
            for i in range(len(self.lista_jugadores)):
                if arquero == self.lista_jugadores[i].dni:
                    arquero = self.lista_jugadores[i]
                    arquero.tener_valla_invicta()
                    esta_a='si'
                else:
                    print("el jugador ingresado no existe.")
        return arquero

    def buscar_arquero_recibio_gol(self):
        for i in range(len(self.lista_jugadores)):
            if self.lista_jugadores[i].posicion == "Arquero":
                print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_a='no'
        while esta_a=='no':   
            arquero= int(input("ingrese el dni del arquero al que le metieron gol: "))
            for i in range(len(self.lista_jugadores)):
                if arquero == self.lista_jugadores[i].dni:
                    arquero = self.lista_jugadores[i]
                    arquero.recibir_gol()
                    esta_a='si'
                else:
                    print("el jugador ingresado no existe.")
        return arquero

    def buscar_goleador(self):
        for i in range(len(self.lista_jugadores)):
            print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_g='no'
        while esta_g=='no':
            goleador = int(input("ingrese el dni del jugador que metio gol: "))
            for i in range(len(self.lista_jugadores)):
                if goleador == self.lista_jugadores[i].dni:
                    goleador = self.lista_jugadores[i]
                    goleador.hacer_gol()
                    esta_g='si'
                else:
                    print("el jugador ingresado no existe.")
        return goleador
    
    def buscar_asistidor(self):
        for i in range(len(self.lista_jugadores)):
            print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_as='no'
        while esta_as=='no':
            asistente = int(input("ingrese el dni del jugador que dio la asistencia: "))
            for i in range(len(self.lista_jugadores)):
                if asistente == self.lista_jugadores[i].dni:
                    asistente = self.lista_jugadores[i]
                    asistente.dar_asistencia()
                    esta_as='si'
                else:
                    print("el jugador ingresado no existe.")
        return asistente

    def buscar_jugador_tarjeta(self):
        for i in range(len(self.lista_jugadores)):
            print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_j='no'
        while esta_j=='no':
            jugador = int(input("ingrese el dni del jugador que metio gol: "))
            for i in range(len(self.lista_jugadores)):
                if jugador == self.lista_jugadores[i].dni:
                    jugador = self.lista_jugadores[i]
                    jugador.hacer_gol()
                    esta_j='si'
                else:
                    print("el jugador ingresado no existe.")
        return goleador

    def __str__(self):
        return("El nombre del club es {}, cuyo ID es {}. El nombre de la liga a la que pertenece es {}, tiene {} de presupuesto y {} de valor. La lista de los jugadores que tiene el club es {}").format(self.nombre, self.id, self.liga, self.presupuesto, self.valor_del_club, self.lista_jugadores)