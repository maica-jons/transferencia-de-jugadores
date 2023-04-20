import datetime
import math

class Persona():

    lista_personas = []

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, nacionalidad, estatura, peso):  
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso

    def calcular_edad(self):
        fechanacimiento = datetime.datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y").date()
        fecha_actual = datetime.date.today()
        diferencia = fecha_actual - fechanacimiento
        edad = math.floor(diferencia.days / 365)
        return edad
    
    def validar_longitud_dni(self):
        while self.dni <= 10000000 or self.dni >= 99999999:
            self.dni = int(input("Ingrese nuevamente un DNI valido: "))

    def verificar_dni_jugador(self,lista_personas):
        while self.dni in lista_personas:
            print("El dni de la persona ya existe. Ingrese otro.")
            self.nombre = str(input("Ingrese nombre de la persona: "))
            self.dni = int(input("Ingrese dni de la persona: "))
        lista_personas.append(self.dni)
        print("Persona cargada exitosamente.")
        return lista_personas