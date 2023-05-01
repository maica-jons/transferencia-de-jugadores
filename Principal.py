from Persona import Persona
from Jugador import Jugador
from Arquero import Arquero
from JugadorDeCampo import JugadorDeCampo
from Club import Club
from Liga import Liga
import datetime
import math

def validar_longitud_dni(dni):
    while dni <= 10000000 or dni >= 99999999:
        dni = int(input("Ingrese nuevamente un DNI valido: "))
    return dni

def validar_fecha_nacimiento(fecha_nacimiento):
    try:
        datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    except ValueError:
        raise ValueError("La fecha de nacimiento debe estar en formato dd/mm/aaaa")

def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    fecha_actual = datetime.date.today()
    diferencia = fecha_actual - fecha_nacimiento
    edad = math.floor(diferencia.days / 365)
    return edad

def validar_estatura(estatura):
    while estatura <= 1 or estatura >= 2.5:
        estatura = float(input("Ingrese nuevamente una estatura en metros valida: "))
    return estatura

def validar_peso(peso):
    while peso <= 30 or peso >= 200:
        peso = float(input("Ingrese el peso nuevamente, en kilogramos. "))
    return peso

def validar_valor(valor):
    while valor <= 0 or valor >= 2000000:
        valor = float(input("Ingrese nuevamente un valor del jugador válido: "))
    return valor

def validar_estado(estado):
    while estado != "Activo" and estado != "activo" and estado != "Lesionado" and estado != "lesionado":
        estado = input("Ingrese nuevamente un estado físico del jugador correctamente: ")
    return estado

def validar_cantidad_partidos(cantidad_partidos):
    while cantidad_partidos < 0:
        cantidad_partidos = int(input("Ingrese 0 o la cantidad de partidos que disputó el jugador correctamente: "))
    return cantidad_partidos

def validar_cantidad_tarjetas(cantidad_tarjetas):
    while cantidad_tarjetas < 0:
        cantidad_tarjetas = int(input("Ingrese 0 o la cantidad de tarjetas que le sacaron al jugador correctamente: "))
    return cantidad_tarjetas

def validar_vallas_invictas(vallas_invictas):
    while vallas_invictas < 0:
        vallas_invictas = int(input("Ingrese un numero valido de vallas invictas: "))
    return vallas_invictas

def validar_goles_recibidos(goles_recibidos):
    while goles_recibidos < 0:
        goles_recibidos = int(input("Ingrese una cantidad valida de goles recibidos: "))
    return goles_recibidos

def validar_goles(goles):
    while goles < 0:
        goles = int(input("Ingrese nuevamente una cantidad de goles valida: "))
    return goles

def validar_asistencia(asistencia):
    while asistencia < 0:
        asistencia = int(input("Ingrese nuevamente una cantidad de asistencia: "))
    return asistencia
    
def validar_presupuesto(presupuesto):
    while presupuesto < 0:
        presupuesto = float(input("Ingrese un monto de presupuesto valido: "))
    return presupuesto

def validar_valor_club(valor_del_club):
    while valor_del_club < 0:
        valor_del_club = float(input("Ingrese un valor de club valido: "))
    return valor_del_club

def elegir_liga():
    for i in range(len(Liga.lista_nombre_ligas)):
        print(Liga.lista_nombre_ligas[i])
    liga_nombre=str(input("Elija la liga de las que estan disponibles: "))
    while liga not in Liga.lista_nombre_ligas:
        liga_nombre=str(input("Esa liga no existe. Elija la liga de las que estan disponibles: "))
    for i in range(len(Liga.lista_ligas)):
        if liga_nombre == Liga.lista_ligas[i].nombre:
            liga = Liga.lista_ligas[i]
    return liga
    
def elegir_club(liga):
    for i in range(len(liga.lista_clubes)):
        print(liga.lista_clubes[i].id, liga.lista_clubes[i].nombre)
    esta='no'
    while esta=="no":
        idclub = input("Ingrese el id del club  de los que estan disponibles: ")
        for i in liga.lista_clubes:
            if idclub == liga.lista_clubes[i].id:
                esta="si"
    for i in range(len(liga.lista_clubes)):
        if idclub == liga.lista_clubes[i].id:
            club = liga.lista_clubes[i]
    return club

def elegir_jugador(club):
    for i in range(len(club.lista_jugadores)):
        print(club.lista_jugadores[i].dni, club.lista_jugadores[i].nombre, club.lista_jugadores[i].apellido)   
    esta='no'
    while esta=="no":
        dni = input("Ingrese el dni del jugador de los que estan disponibles: ")
        for i in club.lista_jugadores:
            if dni == club.lista_jugadores[i].dni:
                esta="si"
    for i in range(len(club.lista_jugadores)):
        if dni == club.lista_jugadores[i].dni:
            jugador = club.lista_jugadores[i]
    return jugador

def menu():
    menu=int(input("""Elija que accion desea
1- Agregar Liga
2- Agregar Club
3- Agregar Jugador
4- Modificar Club 
5- Modificar Jugador (retirar jugador, cambiar estado, cambiar valor)
6- Jugar partido
7- Ver Liga
8- Ver Club
9- Ver Jugador   
10- Salir      
               """))
    return menu

while(menu!=10 ):
    guardo=menu()
    if guardo==1:
        nombre=str(input("Ingrese el nombre de la liga: "))
        while nombre in Liga.lista_nombre_ligas:   #no puede haber dos ligas con el mismo nombre ni dos ligas por pais
            nombre=str(input("El nombre de liga ya existe. Ingrese el nombre de la liga: "))
        pais=str(input("Ingrese el pais de la liga: "))
        while pais in Liga.lista_paises_ligas:
            pais=str(input("El pais de liga ya esta tomado. Ingrese el pais de la liga: "))
        liga=Liga(nombre,pais)
        Liga.lista_ligas.append(liga)
        Liga.lista_nombre_ligas.append(liga.nombre)
        Liga.lista_paises_ligas.append(liga.pais)

    elif guardo==2:
        nombre=str(input("Ingrese el nombre del club: "))
        id=int(input("Ingrese el ID del club: "))
        while id in Club.lista_id_clubes: 
            id=int(input("El id ya existe. Ingrese el ID del club: "))
        for i in range(len(Liga.lista_nombre_ligas)):
            print(Liga.lista_nombre_ligas[i])
        liga=str(input("Elija la liga del club de las que estan disponibles: "))
        while liga not in Liga.lista_nombre_ligas:
            liga=str(input("Esa liga no existe. Elija la liga del club de las que estan disponibles: "))
        presupuesto=str(input("Ingrese el presupuesto del club: "))
        presupuesto=validar_presupuesto(presupuesto)
        club=Club(nombre,id,liga,presupuesto)    
        for i in range(len(Liga.lista_ligas)):
            if club.liga == Liga.lista_ligas[i].nombre:
                Liga.lista_ligas[i].lista_clubes.append(club)
                Liga.lista_ligas[i].cant_clubes+=1

    elif guardo==3:
        nombre=str(input("Ingrese el nombre del jugador: "))
        apellido=str(input("Ingrese el apellido del jugador: "))
        dni=int(input("Ingrese el dni del jugador: "))
        dni=validar_longitud_dni(dni)
        while dni in Persona.lista_dni_personas: 
            dni=int(input("El dni ya existe. Ingrese el dni del jugador: "))
            dni=validar_longitud_dni(dni)
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del jugador en formato dd/mm/aaaa: ")
        fecha_nacimiento = validar_fecha_nacimiento(fecha_nacimiento) 
        edad = calcular_edad(fecha_nacimiento) # falta validar que ingrese bien la fecha de nacimiento
        nacionalidad = input("Ingrese la nacionalidad del jugador: ")
        estatura = int(input("Ingrese la estatura en metros del jugador: "))
        estatura = validar_estatura(estatura)
        peso = float(input("Ingrese el peso en kilogramos del jugador: "))
        peso = validar_peso(peso)
        valor = int(input("Ingrese el valor del jugador: "))
        valor = validar_valor(valor)
        for i in range(len(Club.lista_clubes)):
            print(Club.lista_clubes[i].id, Club.lista_clubes[i].nombre)
        idclub = input("Ingrese el id del club del jugador de los que estan disponibles: ")
        while idclub not in Club.lista_id_clubes:
            idclub=str(input("Ese club no existe. Elija club del jugador de los que estan disponibles: "))
        for i in range(len(Club.lista_clubes)):
            if idclub == Club.lista_clubes[i].id:
                club == Club.lista_clubes[i].nombre
        estado= input("Ingrese el estado fisico del jugador ('Activo' o 'Lesionado'): ")
        estado = validar_estado(estado)
        cantidad_partidos= int(input("Ingrese la cantidad de partidos jugados del jugador: "))
        cantidad_partidos= validar_cantidad_partidos(cantidad_partidos)
        cantidad_tarjetas= int(input("Ingrese la cantidad de tarjetas que recibio el jugador: "))
        cantidad_tarjetas= validar_cantidad_tarjetas(cantidad_tarjetas)
        posicion=int(input("Ingrese solamente el numero de la posicion del jugador (1. Arquero o 2. Jugador de campo): "))
        while posicion != 1 and posicion != 2:
            posicion=int(input("Ingrese solamente el numero de la posicion del jugador (1. Arquero o 2. Jugador de campo): "))
        if posicion == 1:
            vallas_invictas = int(input("Ingrese la cantidad de vallas invictas que tiene el arquero: "))
            vallas_invictas = validar_vallas_invictas(vallas_invictas)
            goles_recibidos = int(input("Ingrese la cantidad de goles que recibio el arquero: "))
            goles_recibidos = validar_goles_recibidos(goles_recibidos)
            arquero=Arquero(nombre,apellido,dni,edad,nacionalidad,estatura,peso,valor,club,estado,cantidad_partidos,cantidad_tarjetas, vallas_invictas, goles_recibidos)
        else: 
            goles= int(input("Ingrese la cantidad de goles que marco el jugador: "))
            goles = validar_goles(goles)
            asistencias = int(input("Ingrese la cantidad de asistencias que hizo el jugador: "))
            asistencias = validar_asistencia(asistencias)
            jugador_de_campo = JugadorDeCampo(nombre,apellido,dni,edad,nacionalidad,estatura,peso,valor,club,estado,cantidad_partidos,cantidad_tarjetas, goles, asistencias)

    elif guardo==4:
        sub_menu=int(input("""Elija que accion desea:
        1- Comprar Jugador
        2- Cambiar Presupuesto"""))
        while sub_menu != 1 and sub_menu != 2:
            sub_menu=int(input("""Elija que accion desea:
        1- Comprar Jugador
        2- Cambiar Presupuesto"""))
        if sub_menu == 1: 
            print("Primero hay que elegir el club que va a comprar.")
            liga_comprador = elegir_liga()
            club_comprador = elegir_club(liga_comprador)
            print("Ahora hay que elegir el jugador a comprar y su club.")
            liga_vendedor = elegir_liga()
            club_vendedor = elegir_club(liga_vendedor)
            jugador = elegir_jugador(club_vendedor)
            club_comprador.comprar_jugador(club_vendedor,jugador)
        else:
            liga = elegir_liga()
            club = elegir_club(liga)
            monto = int(input("Ingrese el monto que se le agregue o reste al presupuesto (si es negativo ingrese un '-' antes del numero): "))
            club.modificar_presupuesto(monto)





    elif guardo==5:
        pass

    elif guardo==6:
        pass

    elif guardo==7:
        liga = elegir_liga()
        print(liga)

    elif guardo==8:
        liga = elegir_liga()
        club = elegir_club(liga)
        print(club)

    elif guardo==9:
        liga = elegir_liga()
        club = elegir_club(liga)
        jugador = elegir_jugador(club)
        print(jugador)

    elif guardo<1 or guardo>10:
        print("Error al elegir accion. Intente de nuevo.")
        guardo=menu()
    elif guardo==10:
        break
