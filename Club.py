class Club():
    lista_clubes=[]
    def __init__(self, nombre, id, pais, liga, presupuesto, valor_del_club):
        self.nombre=nombre
        self.id=id
        self.pais=pais
        self.liga=liga
        self.presupuesto=presupuesto
        self.valor_del_club=valor_del_club
        self.lista_jugadores=[]

    def verificarid_club(self,lista_clubes):
        while self.id in lista_clubes:
            print("El id del club ya existe. Ingrese otro.")
            self.nombre=str(input("Ingrese nombre del club: "))
            self.id=int(input("Ingrese id del club: "))
        lista_clubes.append(self.id)
        print("Club cargado exitosamente.")
        return lista_clubes