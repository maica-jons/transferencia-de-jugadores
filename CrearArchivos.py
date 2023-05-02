
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





def guardarEnArchivo(self,archivo_cuentas,archivo_depositos,archivo_retiros):
     archivo_cuentas.writerow(self.titular.nombre + "," + self.titular.dni + "," + self.titular.genero + "," + self.cbu)

     for monto in self.depositos:
          archivo_depositos.writerow(self.cbu + "," + monto)

     for monto in self.retiros:
          archivo_retiros.writerow(self.cbu + "," + monto)

# def guardarPrograma():
#      with open("./cuentas.csv","w") as archivo_cuentas:
#           with open("./depositos.csv","w") as archivo_depositos:
#                with open("./retiros.csv","w") as archivo_retiros:
#                     for cuentas in Cuenta.dict_cuentas.values():
#                          Cuenta.guardarEnArchivo(archivo_cuentas,archivo_depositos,archivo_retiros)

# def cargarPrograma():
#      with open("./cuentas.csv","r") as archivo_cuentas:
#           with open("./depositos.csv","r") as archivo_depositos:
#                with open("./retiros.csv","r") as archivo_retiros:
#                     for cuenta in archivo_cuentas:
#                          datos_cuenta =cuenta.split(",")
#                          Cuenta(datos_cuenta[0],datos_cuenta[1],datos_cuenta[2],datos_cuenta[3])

#                     for deposito in archivo_depositos:
#                          datos_deposito =deposito.split(",")
#                          Cuenta.obternerPorCBU(datos_deposito[0]).depositar(int(datos_deposito[1]))
#                     for retiro in archivo_retiros:
#                          datos_retiro =retiro.split(",")
#                          Cuenta.obternerPorCBU(datos_retiro[0]).retirar(int(datos_retiro[1]))