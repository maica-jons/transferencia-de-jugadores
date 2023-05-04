from Persona import Persona
from Jugador import Jugador
from Arquero import Arquero
from JugadorDeCampo import JugadorDeCampo
from Club import Club
from Liga import Liga
from Usuario import *
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

def validar_goles(goles):
    while goles < 0:
        goles = int(input("Ingrese nuevamente una cantidad de goles válida: "))
    return goles

def validar_asistencia(asistencia):
    while asistencia < 0:
        asistencia = int(input("Ingrese nuevamente una cantidad de asistencias válida: "))
    return asistencia

def validar_vallas_invictas(vallas_invictas):
    while vallas_invictas < 0:
        vallas_invictas = int(input("Ingrese un numero válido de vallas invictas: "))
    return vallas_invictas

def validar_goles_recibidos(goles_recibidos):
    while goles_recibidos < 0:
        goles_recibidos = int(input("Ingrese una cantidad válida de goles recibidos: "))
    return goles_recibidos
    
def validar_presupuesto(presupuesto):
    while presupuesto < 0:
        presupuesto = float(input("Ingrese un monto de presupuesto válido: "))
    return presupuesto

def validar_valor_club(valor_del_club):
    while valor_del_club < 0:
        valor_del_club = float(input("Ingrese un valor de club válido: "))
    return valor_del_club

def elegir_liga():
    for i in range(len(Liga.lista_nombre_ligas)):
        print(Liga.lista_nombre_ligas[i])
    liga_nombre = str(input("Elija la liga de las que están disponibles: "))
    while liga not in Liga.lista_nombre_ligas:
        liga_nombre = str(input("Esa liga no existe. Elija la liga de las que están disponibles: "))
    for i in range(len(Liga.lista_ligas)):
        if liga_nombre == Liga.lista_ligas[i].nombre:
            liga = Liga.lista_ligas[i]
    return liga
    
def elegir_club(liga):
    for i in range(len(liga.lista_clubes)):
        print(liga.lista_clubes[i].id, liga.lista_clubes[i].nombre)
    esta = "No"
    while esta == "No":
        idclub = input("Ingrese el id del club de los que están disponibles: ")
        for i in liga.lista_clubes:
            if idclub == liga.lista_clubes[i].id:
                esta = "Sí"
    for i in range(len(liga.lista_clubes)):
        if idclub == liga.lista_clubes[i].id:
            club = liga.lista_clubes[i]
    return club

def elegir_jugador(club):
    for i in range(len(club.lista_jugadores)):
        print(club.lista_jugadores[i].dni, club.lista_jugadores[i].nombre, club.lista_jugadores[i].apellido)   
    esta = "No"
    while esta == "No":
        dni = input("Ingrese el dni del jugador de los que están disponibles: ")
        for i in club.lista_jugadores:
            if dni == club.lista_jugadores[i].dni:
                esta = "Sí"
    for i in range(len(club.lista_jugadores)):
        if dni == club.lista_jugadores[i].dni:
            jugador = club.lista_jugadores[i]
    return jugador

def guardar_usuarios():
    with open('./usuarios.txt','w') as archivo_usuarios:
        for usuario in Usuario.lista_usuarios:
            archivo_usuarios.write(f"{usuario.nom_usuario},{usuario.contra},{usuario.nombre},{usuario.apellido},{usuario.dni},{usuario.mail}\n")
        #    archivo_usuarios.writerow(usuario.nom_usuario + ',' + usuario.contra + ',' + usuario.nombre + ',' + usuario.apellido + ',' + usuario.dni + ',' + usuario.mail)

def leer_usuarios():
    try:
        with open('./usuarios.txt','r') as archivo_usuarios:
            for usuario in archivo_usuarios:
                datos_usuario = usuario.split(",")
                datos_usuario[5]= datos_usuario[5].rstrip("\n")
                obj_usuario = Usuario(datos_usuario[0], datos_usuario[1], datos_usuario[2], datos_usuario[3], datos_usuario[4], datos_usuario[5])
                Usuario.lista_usuarios.append(obj_usuario)
                Usuario.lista_nom_usuarios.append(obj_usuario.nom_usuario)
                Usuario.lista_mail.append(obj_usuario.mail)
    except:
        print("")

def menu_usuario():
    try:
        menu=int(input("""Elija una opción del menú (Ingrese el número):
    1- Iniciar sesión
    2- Registrarse
    3- Cambiar contraseña
    4- Salir

    """))
        return menu
    except:
        print("Error. Ingrese el numero de la opcion que desea hacer.")
    

def menu():
    menu=int(input("""Elija una opción del menú (Ingrese el número):
1- Agregar Liga
2- Agregar Club
3- Agregar Jugador
4- Modificar Club 
5- Modificar Jugador 
6- Jugar partido
7- Visualizar Liga
8- Visualizar Club
9- Visualizar Jugador   
10- Cerrar sesión (Salir)   

"""))
    return menu

#  revisar los try except
#  revisar el leer archivo 
    #MAICA REVISO GUARDAR ARCHIVO (antes de leer archivo() ), PARA MI EL ERROR ESTABA AHI. ENTIENDO QUE AHORA FUNCIONA
    #PROBARLO!!!

def menu_principal(usu):
    try:
        while(menu != 10):
            guardo = menu()
            if guardo == 1:
                nombre = str(input("Ingrese el nombre de la liga que desea agregar: "))
                while nombre in Liga.lista_nombre_ligas:   #No puede haber dos ligas con el mismo nombre ni dos ligas por pais
                    nombre = str(input("Ya existe una liga con ese nombre. Ingrese otro nombre para la liga: "))
                pais = str(input("Ingrese el país al que pertenece la liga: "))
                while pais in Liga.lista_paises_ligas:
                    pais = str(input("Ya existe una liga para ese país, no puede existir más de 1 liga por país. Ingrese otro país: "))
                liga = Liga(nombre,pais)
                Liga.lista_ligas.append(liga)
                Liga.lista_nombre_ligas.append(liga.nombre)
                Liga.lista_paises_ligas.append(liga.pais)

            elif guardo == 2:
                if len(Liga.lista_nombre_ligas) == 0:
                    print("No hay ninguna liga creada. Primero vaya a crear una.")
                else:
                    nombre = str(input("Ingrese el nombre del club que desea agregar: "))
                    id = int(input("Ingrese un ID para el club (nro. o nros. enteros): "))
                    while id in Club.lista_id_clubes: 
                        id = int(input("El ID ingresado ya existe para otro club. Ingrese otro ID para el club: "))
                    Club.lista_id_clubes.append(id)
                    for i in range(len(Liga.lista_nombre_ligas)):
                        print(Liga.lista_nombre_ligas[i])
                    liga = str(input("Elija la liga a la que va a agregar el club. Las ligas disponibles son las siguientes: "))
                    while liga not in Liga.lista_nombre_ligas:
                        liga = str(input("La liga ingresada no existe. Elija una de la lista que se le presentó: "))
                    presupuesto = int(input("Ingrese el presupuesto actual del club (ingrese solamente nros. a menos que sea un nro. decimal): "))
                    presupuesto = validar_presupuesto(presupuesto)
                    club = Club(nombre,id,liga,presupuesto)    
                    Club.lista_clubes.append(club)
                    for i in range(len(Liga.lista_ligas)):
                        if club.liga == Liga.lista_ligas[i].nombre:
                            Liga.lista_ligas[i].lista_clubes.append(club)
                            Liga.lista_ligas[i].cant_clubes+=1

            elif guardo == 3:
                if len(Club.lista_clubes) == 0:
                    print("No hay ningun club creado. Primero vaya a crear uno.")
                else: 
                    nombre = str(input("Ingrese el nombre del jugador que desea agregar: "))
                    apellido = str(input("Ingrese el apellido del jugador que desea agregar: "))
                    dni = int(input("Ingrese el DNI del jugador: "))
                    dni=validar_longitud_dni(dni)
                    while dni in Persona.lista_dni_personas: 
                        dni = int(input("El DNI ingresado ya existe para otro jugador. Intente de nuevo: "))
                        dni = validar_longitud_dni(dni)
                    Persona.lista_dni_personas.append(dni)
                    fecha_nacimiento = input("Ingrese la fecha de nacimiento del jugador en formato dd/mm/aaaa: ")
                    fecha_nacimiento = validar_fecha_nacimiento(fecha_nacimiento) 
                    edad = calcular_edad(fecha_nacimiento)
                    nacionalidad = input("Ingrese la nacionalidad del jugador: ")
                    estatura = int(input("Ingrese la estatura (en metros) del jugador: "))
                    estatura = validar_estatura(estatura)
                    peso = float(input("Ingrese el peso (en kilogramos) del jugador: "))
                    peso = validar_peso(peso)
                    valor = int(input("Ingrese el valor del jugador: "))
                    valor = validar_valor(valor)
                    for i in range(len(Club.lista_clubes)):
                        print(Club.lista_clubes[i].id, Club.lista_clubes[i].nombre)
                    idclub = input("Ingrese el ID del club al que desea agregar al jugador. Los clubes con sus respectivos IDs son los siguientes: ")
                    while idclub not in Club.lista_id_clubes:
                        idclub = str(input("El ID club ingresado no corresponde a ningún club existente. Elija una de las opciones que se le mostraron: "))
                    for i in range(len(Club.lista_clubes)):
                        if idclub == Club.lista_clubes[i].id:
                            club == Club.lista_clubes[i].nombre
                    estado= input("Ingrese el estado físico del jugador ('Activo' o 'Lesionado'): ")
                    estado = validar_estado(estado)
                    cantidad_partidos = int(input("Ingrese la cantidad de partidos jugados por el jugador: "))
                    cantidad_partidos = validar_cantidad_partidos(cantidad_partidos)
                    cantidad_tarjetas = int(input("Ingrese la cantidad de tarjetas que recibió el jugador: "))
                    cantidad_tarjetas = validar_cantidad_tarjetas(cantidad_tarjetas)
                    posicion = int(input("En qué posición juega? Ingrese sólo el nro. correspondiente a la posición (1. Arquero o 2. Jugador de campo): "))
                    while posicion != 1 and posicion != 2:
                        posicion = int(input("Ingresó un nro. que no corresponde a una posición. Intente de nuevo: "))
                    if posicion == 1:
                        posicion = "Arquero"
                        vallas_invictas = int(input("Ingrese la cantidad de vallas invictas que tiene el arquero: "))
                        vallas_invictas = validar_vallas_invictas(vallas_invictas)
                        goles_recibidos = int(input("Ingrese la cantidad de goles que recibio el arquero: "))
                        goles_recibidos = validar_goles_recibidos(goles_recibidos)
                        arquero=Arquero(nombre,apellido,dni,edad,nacionalidad,estatura,peso,valor,club,estado,cantidad_partidos,cantidad_tarjetas, posicion, vallas_invictas, goles_recibidos)
                        Arquero.lista_arqueros.append(arquero)
                    else: 
                        posicion = "Jugador de campo"
                        goles= int(input("Ingrese la cantidad de goles que marcó el jugador: "))
                        goles = validar_goles(goles)
                        asistencias = int(input("Ingrese la cantidad de asistencias que hizo el jugador: "))
                        asistencias = validar_asistencia(asistencias)
                        jugador_de_campo = JugadorDeCampo(nombre,apellido,dni,edad,nacionalidad,estatura,peso,valor,club,estado,cantidad_partidos,cantidad_tarjetas, posicion, goles, asistencias)
                        JugadorDeCampo.lista_jugadorescampo.append(jugador_de_campo)

            elif guardo == 4:
                if len(Club.lista_clubes) == 0:
                    print("No hay ningun club creado. Primero vaya a crear uno.")
                else:
                    try:
                        sub_menu = int(input("""Elija la acción que desea:
                        1- Comprar Jugador
                        2- Cambiar Presupuesto"""))
                        while sub_menu != 1 and sub_menu != 2:
                            sub_menu=int(input("""Elija la acción que desea:
                        1- Comprar Jugador
                        2- Cambiar Presupuesto"""))
                    except:
                        print("Error. Ingrese el numero de la opcion que desea hacer.")
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
                        monto = int(input("Ingrese el monto que desea agregar o restar al presupuesto (si desea restar, ingrese un '-' antes del número): "))
                        club.modificar_presupuesto(monto)

            elif guardo == 5:
                if len(Persona.lista_dni_personas) == 0:
                    print("No hay ningun jugador creado. Primero vaya a crear uno.")
                else:
                    print("Primero elija el jugador a modificar.")
                    liga = elegir_liga()
                    club = elegir_club(liga)
                    jugador = elegir_jugador(club)
                    try:
                        sub_menu=int(input("""Elija la acción que desea:
                        1- Retirar Jugador
                        2- Cambiar Estado de un Jugador
                        3. Cambiar Valor de un Jugador"""))
                        while sub_menu != 1 and sub_menu != 2 and sub_menu!= 3:
                            sub_menu=int(input("""Elija la acción que desea:
                        1- Retirar Jugador
                        2- Cambiar Estado de un Jugador
                        3. Cambiar Valor de un Jugador"""))
                    except:
                        print("Error. Ingrese el numero de la opcion que desea hacer.")
                    if sub_menu == 1:
                        jugador.retirar_jugador(club)
                    elif sub_menu == 2:
                        jugador.modificar_estado()
                    else:
                        jugador.modificar_valor()

            elif guardo == 6:
                if len(Liga.lista_nombre_ligas) == 0:
                    print("No hay ninguna liga creada. Primero vaya a crear una.")
                else:
                    liga = elegir_liga()
                    if len(liga.lista_clubes) < 2:
                        print("Se necesita al menos 2 clubes en la misma liga para jugar un partido. Vaya a crearlos.")
                    else:
                        print("Elija el club local que jugará el partido.")
                        club1 = elegir_club(liga)
                        print("Elija el club visitante que jugará el partido.")
                        club2 = elegir_club(liga)
                        liga.jugar_partido(club1, club2)

            elif guardo == 7:
                if len(Liga.lista_nombre_ligas) == 0:
                    print("No hay ninguna liga creada. Primero vaya a crear una.")
                else:
                    liga = elegir_liga()
                    print(liga)

            elif guardo == 8:
                if len(Club.lista_clubes) == 0:
                    print("No hay ningun club creado. Primero vaya a crear uno.")
                else:
                    liga = elegir_liga()
                    club = elegir_club(liga)
                    print(club)

            elif guardo == 9:
                if len(Persona.lista_dni_personas) == 0:
                    print("No hay ningun jugador creado. Primero vaya a crear uno.")
                else:
                    liga = elegir_liga()
                    club = elegir_club(liga)
                    jugador = elegir_jugador(club)
                    print(jugador)

            elif guardo < 1 or guardo >10 :
                print("Error al elegir acción. Intente de nuevo: ")
            elif guardo == 10:
                usu.guardar_archivos()
                break
    except:
        print("Error. Ingrese el numero de la opcion que desea hacer.")

while(menu_usuario != 4):
    leer_usuarios()
    entrar = "no"
    while entrar == "no":
        guardar = menu_usuario()
        if guardar in [1,2,3,4]:
            entrar = "si"
    if guardar == 1:
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado. Primero vaya a registrarse.")
        else: 
            esta = "No"
            while esta == "No":
                nom_usuario = input("Ingrese su nombre de usuario: ")
                for i in range(len(Usuario.lista_usuarios)):
                    if nom_usuario == Usuario.lista_usuarios[i].nom_usuario:
                        esta = "Sí"
                        contrasena = input("Ingrese su contraseña: ")
                        while contrasena != Usuario.lista_usuarios[i].contra:
                            contrasena = input("La contraseña es incorrecta. Intente nuevamente: ")
                        usu = Usuario.lista_usuarios[i]
                        print("Ingresado correctamente.")
                        usu.leer_archivo()
                        menu_principal(usu)
                if esta == "No":
                    print("El nombre de usuario no existe.")
    elif guardar == 2:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        dni = int(input("Ingrese su dni: "))
        dni = validar_longitud_dni(dni)
        mail = input("Ingrese su mail: ")
        while mail in Usuario.lista_mail:
            mail = input("Ese mail ya tiene un usuario. Ingrese su mail: ")
        Usuario.lista_mail.append(mail)
        nom_usuario = input("Ingrese un nombre de usuario: ")
        while (nom_usuario in Usuario.lista_nom_usuarios) or (nom_usuario == ""):
            nom_usuario = input("Ese nombre es inválido. Ingrese un nombre de usuario: ")
        Usuario.lista_nom_usuarios.append(nom_usuario)
        contrasena = input("Ingrese una contraseña: ")
        while len(contrasena) <= 0: 
            contrasena = input("No es una contraseña válida. Ingrese una contraseña: ")
        usuario = Usuario(nom_usuario, contrasena, nombre, apellido, dni, mail)
        Usuario.lista_usuarios.append(usuario)
        guardar_usuarios()
    elif guardar == 3 :
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado. Primero vaya a registrarse.")
        else:
            esta = "No"
            while esta == "No":
                nom_usuario = input("Ingrese su nombre de usuario: ")
                for i in range(len(Usuario.lista_usuarios)):
                    if nom_usuario == Usuario.lista_usuarios[i].nom_usuario:
                        esta = "Sí"
                        usu = Usuario.lista_usuarios[i]
                        contrasena = input("Primero ingrese su contraseña vieja: ")
                        while contrasena != Usuario.lista_usuarios[i].contra:
                            contrasena = input("La contraseña es incorrecta. Intente nuevamente: ")
                        contra_nueva = input("Ingrese su nueva contraseña: ")
                        usu.cambiar_contra(contra_nueva)
                if esta == "No":
                    print("El nombre de usuario no existe.")        
    elif guardar < 1 or guardar > 4 :
        print("Error al elegir acción. Intente de nuevo: ")
    elif guardar == 4:
        break
