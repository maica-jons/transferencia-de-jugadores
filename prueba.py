def leer_ligas():
    try:
        with open('./ligas.txt','r') as archivo_ligas:
            for liga in archivo_ligas:
                datos_liga = liga.split(',')
                datos_liga[3] = datos_liga[3].rstrip("\n")
                obj_liga = Liga(datos_liga[0],datos_liga[1],datos_liga[2],datos_liga[3])
                Liga.lista_ligas.append(obj_liga)
                Liga.lista_nombre_ligas.append(obj_liga.nombre)
                Liga.lista_paises_ligas.append(obj_liga.pais)
        archivo_ligas.close()
    except:
        print("")
    
def leer_clubes():
    try:
        with open('./clubes.txt','r') as archivo_clubes:
            for club in archivo_clubes:
                datos_club = club.split(',')
                datos_club[5] = datos_club[5].rstrip("\n")
                obj_club = Club(datos_club[0],datos_club[1],datos_club[2],datos_club[3],datos_club[4],datos_club[5])
        archivo_clubes.close()
    except:
        print("")

def leer_arqueros():
    try:
        with open('./arqueros.txt','r') as archivo_arqueros:
            for arquero in archivo_arqueros:
                datos_arquero = arquero.split(',')
                datos_arquero[14] = datos_arquero[14].rstrip("\n")
                obj_arquero = Arquero(datos_arquero[0],datos_arquero[1],datos_arquero[2],datos_arquero[3],datos_arquero[4],datos_arquero[5],datos_arquero[6],datos_arquero[7],datos_arquero[8],datos_arquero[9],datos_arquero[10],datos_arquero[11],datos_arquero[12],datos_arquero[13],datos_arquero[14])
                Arquero.lista_arqueros.append(obj_arquero)
        archivo_arqueros.close()
    except:
        print("")

def leer_jugadorescampo():
    try:
        with open('./jugadorescampo.txt','r') as archivo_jugadorescampo:
            for jugadorcampo in archivo_jugadorescampo:
                dato_jugadorcampo = jugadorcampo.split(',')
                dato_jugadorcampo[14] = dato_jugadorcampo[14].rstrip("\n")
                obj_jugadorcampo = JugadorDeCampo(dato_jugadorcampo[0],dato_jugadorcampo[1],dato_jugadorcampo[2],dato_jugadorcampo[3],dato_jugadorcampo[4],dato_jugadorcampo[5],dato_jugadorcampo[6],dato_jugadorcampo[7],dato_jugadorcampo[8],dato_jugadorcampo[9],dato_jugadorcampo[10],dato_jugadorcampo[11],dato_jugadorcampo[12],dato_jugadorcampo[13],dato_jugadorcampo[14])
                Persona.lista_dni_personas.append(obj_jugadorcampo.dni)
        archivo_jugadorescampo.close()
    except:
        print("")