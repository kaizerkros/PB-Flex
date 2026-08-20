from inventario import Inventario

# clase Personaje

class Personaje:
    #metodo constructor 
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario = Inventario()
    
    def atacar(self):
        print(f"{self.nombre} realiza un ataque.")

    def recibir_Danio(self,danio):

        self.vida -= danio 

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibio {danio} puntos por daño ")

    def mostrar_informacion(self):

        print("\n ---Informacion PJ---")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"vida:{self.vida}")

    def usar_habilidad(self):
        print(f"{self.nombre} utiliza habilidad ")
    