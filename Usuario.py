from Persona import Persona
from Jugador import Jugador
from Arquero import Arquero
from JugadorDeCampo import JugadorDeCampo
from Club import Club
from Liga import Liga

class Usuario():

    lista_usuarios = []
    lista_mail = []
    lista_nom_usuarios = []

    def __init__(self, nom_usuario, contra, nombre, apellido, dni, mail):
        self.nom_usuario = nom_usuario
        self.contra = contra
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

    def guardar_archivos(self):
        with open('./ligas.txt','r+') as archivo_ligas:
            with open('./clubes.txt','r+') as archivo_clubes:
                with open('./arqueros.txt','r+') as archivo_arqueros:
                    with open('./jugadorescampo.txt','r+') as archivo_jugadorescampo:
                        for liga in Liga.lista_ligas:
                            archivo_ligas.writerow(liga.nombre + ',' + liga.pais + ',' + liga.lista_clubes + ',' + liga.cant_clubes)
                        for club in Club.lista_clubes:
                            archivo_clubes.writerow(club.nombre + ',' + club.id + ',' + club.liga + ',' + club.presupuesto + ',' + club.valor_del_club + ',' + club.lista_jugadores)
                        for arquero in Arquero.lista_arqueros:
                            archivo_arqueros.writerow(arquero.nombre + ',' + arquero.apellido + ',' + arquero.dni + ',' + arquero.edad + ',' + arquero.nacionalidad + ',' + arquero.estatura + ',' + arquero.peso + ',' + arquero.valor + ',' + arquero.club + ',' + arquero.estado + ',' + arquero.cantidad_partidos + ',' + arquero.cantidad_tarjetas + ',' + arquero.posicion + ',' + arquero.vallas_invictas + ',' + arquero.goles_recibidos)
                        for jugadorcampo in JugadorDeCampo.lista_jugadorescampo:
                            archivo_jugadorescampo.writerow(jugadorcampo.nombre + ',' + jugadorcampo.apellido + ',' + jugadorcampo.dni + ',' + jugadorcampo.edad + ',' + jugadorcampo.nacionalidad + ',' + jugadorcampo.estatura + ',' + jugadorcampo.peso + ',' + jugadorcampo.valor + ',' + jugadorcampo.club + ',' + jugadorcampo.estado + ',' + jugadorcampo.cantidad_partidos + ',' + jugadorcampo.cantidad_tarjetas + ',' + jugadorcampo.posicion + ',' + jugadorcampo.goles + ',' + jugadorcampo.asistencias)

    def leer_archivo(self):
        try: 
            with open('./ligas.txt','r') as archivo_ligas:
                with open('./clubes.txt','r') as archivo_clubes:
                    with open('./arqueros.txt','r') as archivo_arqueros:
                        with open('./jugadorescampo.txt','r') as archivo_jugadorescampo:
                            for liga in archivo_ligas:
                                datos_liga = liga.split(',')
                                obj_liga = Liga(datos_liga[0],datos_liga[1],datos_liga[2],datos_liga[3])
                                Liga.lista_ligas.append(obj_liga)
                                Liga.lista_nombre_ligas.append(obj_liga.nombre)
                                Liga.lista_paises_ligas.append(obj_liga.pais)
                            for club in archivo_clubes:
                                datos_club = club.split(',')
                                obj_club = Club(datos_club[0],datos_club[1],datos_club[2],datos_club[3],datos_club[4],datos_club[5])
                                Club.lista_clubes.append(obj_club)
                                Club.lista_id_clubes.append(obj_club.id)
                            for arquero in archivo_arqueros:
                                datos_arquero = arquero.split(',')
                                obj_arquero = Arquero(datos_arquero[0],datos_arquero[1],datos_arquero[2],datos_arquero[3],datos_arquero[4],datos_arquero[5],datos_arquero[6],datos_arquero[7],datos_arquero[8],datos_arquero[9],datos_arquero[10],datos_arquero[11],datos_arquero[12],datos_arquero[13],datos_arquero[14])
                                Arquero.lista_arqueros.append(obj_arquero)
                                Persona.lista_dni_personas.append(obj_arquero.dni)
                            for jugadorcampo in archivo_jugadorescampo:
                                dato_jugadorcampo = jugadorcampo.split(',')
                                obj_jugadorcampo = JugadorDeCampo(dato_jugadorcampo[0],dato_jugadorcampo[1],dato_jugadorcampo[2],dato_jugadorcampo[3],dato_jugadorcampo[4],dato_jugadorcampo[5],dato_jugadorcampo[6],dato_jugadorcampo[7],dato_jugadorcampo[8],dato_jugadorcampo[9],dato_jugadorcampo[10],dato_jugadorcampo[11],dato_jugadorcampo[12],dato_jugadorcampo[13],dato_jugadorcampo[14])
                                Persona.lista_dni_personas.append(obj_jugadorcampo.dni)
        except:
            print("")

    def cambiar_contra(self,nueva):
        self.contra = nueva
        print("Se ha cambiado la contraseña con éxito.")