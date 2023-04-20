import Persona
import Jugador
import Arquero
import JugadorDeCampo
import Club
import Liga


def validar_longitud_dni(dni):
    while dni <= 10000000 or dni >= 99999999:
        dni = int(input("Ingrese nuevamente un DNI valido: "))
    return dni

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


def menu():
    menu=int(input("""Elija que accion desea
1- Agregar Liga
2- Agregar Club
3- Agregar Jugador
4- Modificar Liga
5- Modificar Club
6- Modificar Jugador
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
        pais=str(input("Ingrese el pais de la liga: "))
        liga=Liga(nombre,pais)

    elif guardo==2:
        nombre=str(input("Ingrese el nombre del club: "))
        id=int(input("Ingrese el ID del club: "))
        liga=str(input("Ingrese la liga del club: "))
        presupuesto=str(input("Ingrese el presupuesto del club: "))
        presupuesto=validar_presupuesto(presupuesto)
        club1=Club(nombre,id,liga,presupuesto)
        Club.lista_clubes= club1.verificarid_club(Club.lista_clubes)
        

    elif guardo==3:
        nombre=str(input("Ingrese el nombre del jugador: "))
        apellido=str(input("Ingrese el apellido del jugador: "))
        dni=int(input("Ingrese el dni del jugador: "))
        dni=validar_longitud_dni(dni)


    elif guardo==4:
        pass

    elif guardo==5:
        pass

    elif guardo==6:
        pass

    elif guardo==7:
        pass

    elif guardo==8:
        pass

    elif guardo==9:
        pass

    elif guardo<1 or guardo>11:
        print("Error al elegir accion. Intente de nuevo.")
        guardo=menu()
    elif guardo==1:
        break
