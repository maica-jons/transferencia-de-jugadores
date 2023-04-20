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

    def CalcularEdad(self):
        fechanacimiento = datetime.datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y").date()
        fecha_actual = datetime.date.today()
        diferencia = fecha_actual - fechanacimiento
        edad = math.floor(diferencia.days / 365)
        return edad

    def verificardni_jugador(self,lista_personas):
        if len(self.dni)!=8:
            print('El DNI {} no cumple con el formato.Debe contener 8 digitos'.format(self.dni))
            return False
        for persona in Persona.lista_personas:
            if persona.dni == self.dni:
                print('El usuario esta registrado OK')
                return True
            else:
                print('El usuario no esta registrado, para cargar las notas primero debe registrarlo')
                return False
        while self.dni in lista_personas:
            print("El dni de la persona ya existe. Ingrese otro.")
            self.nombre = str(input("Ingrese nombre de la persona: "))
            self.dni = int(input("Ingrese dni de la persona: "))
        lista_personas.append(self.dni)
        print("Persona cargada exitosamente.")
        return lista_personas