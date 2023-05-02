
def crear_matriz(que_matriz_es):
     atributos = int(input("ingresa cantidad de atributos: "))
     matriz = [None]*(atributos+1)
     print(matriz)
     for columna in range(len(matriz)):
          if columna == 0:
               matriz[columna] = (que_matriz_es)
          else:
               atributo = input("ingresa título columna que representa atributo: ")
               matriz[columna] = atributo
     return matriz

#def completar_matriz(matriz,lista):
    # for objeto in lista:
        #  lista_atributos = 

matriz_ligas = crear_matriz("LIGAS")
print(matriz_ligas)