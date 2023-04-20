import Persona
import Jugador
import Arquero
import JugadorDeCampo
import Club
import Liga

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
        club1=Club(nombre,id,liga,presupuesto)
        Club.lista_clubes= club1.verificarid_club(Club.lista_clubes)
        

    elif guardo==3:
        pass

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
