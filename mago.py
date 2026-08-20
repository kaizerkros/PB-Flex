from personaje import Personaje 

class Mago(Personaje):

    def __init__(self, nombre, nivel, vida,mana):
        super().__init__(nombre, nivel, vida)
        self.mana = mana 

    def atacar(self):
        print(f"{self.nombre} lanza un hechizo"
              f"con {self.mana} de poder magico")

    def usar_habilidad(self):
        print(f"{self.nombre} ejercito de no muertos")