from Club import Club
from JugadorDeCampo import JugadorDeCampo
from Arquero import Arquero


class Liga():
    lista_ligas = [] #total de ligas
    lista_nombre_ligas = []
    lista_paises_ligas = [] #cada pais tiene maximo 1 liga (si creo una liga en un pais que ya tiene, no me deja)

    def __init__(self, nombre, pais):
        if nombre in Liga.lista_ligas:
            raise ValueError("La liga ya fue creada.")
        else:
            Liga.lista_ligas += nombre
        self.nombre = nombre
        self.pais = pais
        self.lista_clubes = [] #clubes de cada liga
        self.cant_clubes = 0 #Ver si lo mantenemos porque es medio innecesario

    def jugar_partido(self, club1, club2):
        goles = input("ingrese 's' si HUBO goles y 'n' si NO HUBO goles: ")
        while goles != "s" and goles != "n":
            goles = input("No ingreso una opcion valida. ingrese 's' si HUBO goles y 'n' si NO HUBO goles: ")
        if goles == "s":
            cant_goles = int(input("Cuantos goles totales hubo en el partido? "))
            while cant_goles <=0:
                cant_goles = int(input("El numero tiene que se mayor a 0. Cuantos goles totales hubo en el partido? "))
            cont=0
            cont_l=0
            cont_v=0
            while cont < cant_goles:
                que_club = input("que club hizo gol? para local ingrese l, para visitante ingrese v: ")
                if que_club == "l":
                    for i in range(len(club1.lista_jugadores)):
                        print(club1.lista_jugadores[i].dni, club1.lista_jugadores[i].nombre, club1.lista_jugadores[i].apellido)
                    esta_g='no'
                    while esta_g=='no':
                        goleador = int(input("ingrese el dni del jugador que metio gol: "))
                        for i in range(len(club1.lista_jugadores)):
                            if goleador == club1.lista_jugadores[i].dni:
                                goleador = club1.lista_jugadores[i]
                                goleador.hacer_gol()
                                esta_g='si'
                                cont_l+=1
                            else:
                                print("el jugador ingresado no existe.")
                    asistencia = input("el gol tuvo asistencia? ingrese s o n: ")
                    while asistencia != "s" and asistencia != "n":
                        asistencia = input("ingrese una respuesta válida. si el gol tuvo asistencia ingrese s, si no ingrese n: ")
                    if asistencia == 's':
                        for i in range(len(club1.lista_jugadores)):
                            print(club1.lista_jugadores[i].dni, club1.lista_jugadores[i].nombre, club1.lista_jugadores[i].apellido)
                        esta_as='no'
                        while esta_as=='no':
                            asistente = int(input("ingrese el dni del jugador que metio gol: "))
                            for i in range(len(club1.lista_jugadores)):
                                if asistente == club1.lista_jugadores[i].dni:
                                    asistente = club1.lista_jugadores[i]
                                    asistente.dar_asistencia()
                                    esta_as='si'
                                else:
                                    print("el jugador ingresado no existe.")
                    for i in range(len(club2.lista_jugadores)):
                        if club2.lista_jugadores[i].posicion == "Arquero":
                            print(club2.lista_jugadores[i].dni, club2.lista_jugadores[i].nombre, club2.lista_jugadores[i].apellido)
                    esta_a='no'
                    while esta_a=='no':   
                        arquero= int(input("ingrese el dni del arquero al que le metieron gol: "))
                        for i in range(len(club2.lista_jugadores)):
                            if arquero == club2.lista_jugadores[i].dni:
                                arquero = club2.lista_jugadores[i]
                                arquero.recibir_gol()
                                esta_a='si'
                                cont+=1
                            else:
                                print("el jugador ingresado no existe.")
                    
                else: #club visitante
                    for i in range(len(club2.lista_jugadores)):
                        print(club2.lista_jugadores[i].dni, club2.lista_jugadores[i].nombre, club2.lista_jugadores[i].apellido)
                    esta_g='no'
                    while esta_g=='no':
                        goleador = int(input("ingrese el dni del jugador que metio gol: "))
                        for i in range(len(club2.lista_jugadores)):
                            if goleador == club2.lista_jugadores[i].dni:
                                goleador = club2.lista_jugadores[i]
                                goleador.hacer_gol()
                                esta_g='si'
                                cont_v+=1
                            else:
                                print("el jugador ingresado no existe.")
                    asistencia = input("el gol tuvo asistencia? ingrese s o n: ")
                    while asistencia != "s" and asistencia != "n":
                        asistencia = input("ingrese una respuesta válida. si el gol tuvo asistencia ingrese s, si no ingrese n: ")
                    if asistencia == 's':
                        for i in range(len(club2.lista_jugadores)):
                            print(club2.lista_jugadores[i].dni, club2.lista_jugadores[i].nombre, club2.lista_jugadores[i].apellido)
                        esta_as='no'
                        while esta_as=='no':
                            asistente = int(input("ingrese el dni del jugador que metio gol: "))
                            for i in range(len(club2.lista_jugadores)):
                                if asistente == club2.lista_jugadores[i].dni:
                                    asistente = club2.lista_jugadores[i]
                                    asistente.dar_asistencia()
                                    esta_as='si'
                                else:
                                    print("el jugador ingresado no existe.")
                    for i in range(len(club1.lista_jugadores)):
                        if club2.lista_jugadores[i].posicion == "Arquero":
                            print(club1.lista_jugadores[i].dni, club1.lista_jugadores[i].nombre, club1.lista_jugadores[i].apellido)
                    esta_a='no'
                    while esta_a=='no':   
                        arquero= int(input("ingrese el dni del arquero al que le metieron gol: "))
                        for i in range(len(club1.lista_jugadores)):
                            if arquero == club1.lista_jugadores[i].dni:
                                arquero = club1.lista_jugadores[i]
                                arquero.recibir_gol()
                                esta_a='si'
                                cont+=1
                            else:
                                print("el jugador ingresado no existe.")
        if cont_l ==0:
            for i in range(len(club2.lista_jugadores)):
                if club2.lista_jugadores[i].posicion == "Arquero":
                    print(club2.lista_jugadores[i].dni, club2.lista_jugadores[i].nombre, club2.lista_jugadores[i].apellido)
            esta_a='no'
            while esta_a=='no':   
                arquero= int(input("ingrese el dni del arquero al que le metieron gol: "))
                for i in range(len(club2.lista_jugadores)):
                    if arquero == club2.lista_jugadores[i].dni:
                        arquero = club2.lista_jugadores[i]
                        arquero.recibir_gol()
                        esta_a='si'
                        cont+=1
                    else:
                        print("el jugador ingresado no existe.")

        else:

        tarjetas = input("ingrese 's' si HUBO tarjetas y 'n' si NO HUBO tarjetas: ")
        while tarjetas != "s" and tarjetas != "n":
            tarjetas = input("No ingreso una opcion valida. ingrese 's' si HUBO tarjetas y 'n' si NO HUBO tarjetas: ")
        if goles == "s":
            cant_tarjetas = int(input("Cuantas taretas totales hubo en el partido? "))
            cont=0
            while cont < cant_tarjetas:
                
        
    def __str__(self):
        return("La liga del país '{}' se llama '{}' y está conformada por los siguientes {} clubes: {}").format(self.pais, self.nombre, self.cant_clubes, self.lista_clubes)

            
#preguntar si hubo asistencia y si hubo ingresarsela al jugador que la hizo


    #while hasta que sea no
    #asistencia
    #tarjetas
    #cont de goles 0
    #valla invicta si termina en 0
    # hubo goels
    #     quien
    #     ingresarlo
    # sumarle +1
    # while hasta que sea no
    # asistencia
    # tarjetas
    # cont de goles 0
    # valla invicta si termina en 0
