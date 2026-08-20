class Objeto:
    def __init__(self,nombre,tipo):

        self.nombre = nombre
        self.tipo = tipo 

    def mostrar_Informacion(self):
        print(f"objeto:{self.nombre}")
        print(f"tipo:{self.tipo}")