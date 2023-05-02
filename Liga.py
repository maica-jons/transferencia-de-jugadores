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
                    club1.buscar_goleador()
                    asistencia = input("el gol tuvo asistencia? ingrese s o n: ")
                    while asistencia != "s" and asistencia != "n":
                        asistencia = input("ingrese una respuesta válida. si el gol tuvo asistencia ingrese s, si no ingrese n: ")
                    if asistencia == 's':
                        club1.buscar_asistidor()
                    club2.buscar_arquero_recibio_gol()
                    cont_l+=1
                    cont+=1 
                else: #club visitante
                    club2.buscar_goleador()
                    asistencia = input("el gol tuvo asistencia? ingrese s o n: ")
                    while asistencia != "s" and asistencia != "n":
                        asistencia = input("ingrese una respuesta válida. si el gol tuvo asistencia ingrese s, si no ingrese n: ")
                    if asistencia == 's':
                        club2.buscar_asistidor()
                    club1.buscar_arquero_recibio_gol()
                    cont_v+=1
                    cont+=1
            if cont_l ==0:
                club2.buscar_arquero_valla_invicta()
            if cont_v==0:
                club1.buscar_arquero_valla_invicta()
        else:
            club1.buscar_arquero_valla_invicta()
            club2.buscar_arquero_valla_invicta()

        # tarjetas = input("ingrese 's' si HUBO tarjetas y 'n' si NO HUBO tarjetas: ")
        # while tarjetas != "s" and tarjetas != "n":
        #     tarjetas = input("No ingreso una opcion valida. ingrese 's' si HUBO tarjetas y 'n' si NO HUBO tarjetas: ")
        # if goles == "s":
        #     cant_tarjetas = int(input("Cuantas taretas totales hubo en el partido? "))
        #     cont=0
        #     while cont < cant_tarjetas:
        #         pass
                
        
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
