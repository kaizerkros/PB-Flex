
class Inventario:

    def __init__(self):
        self.objetos = []
    #metodo para agregar objeto 
    def agregar_objetos(self, objeto):

        self.objetos.append(objeto)
        print(f"{objeto.nombre} a sido agregado al inventario")

    def mostrar_Inventario(self):

        print("\n---Inventario---")
        #contar inventario
        if len(self,self.objetos)==0:
            print("El inventario esta vacio")
        else:

            for objeto in self.objetos:
                print(f" - {objeto.nombre} ({objeto.tipo})")