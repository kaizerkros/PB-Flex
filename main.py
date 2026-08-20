from jugador import Jugador 
from mago import Mago 
from personaje import Personaje
from guerrero import Guerrero
from objeto import Objeto 

#Método principal

def main():

    #crear jugador 

    jugador = Jugador("Scott")

    #crear personaje 

    magician= Mago("Alkzar",1000,999999,999999)
    
    Asesino= Guerrero("MUÑAÑO",1000,1999999,19000000)

    #asociar jugador con personaje
    jugador.seleccionar_personaje(Asesino)

    #mostrar info del mago

    Asesino.mostrar_informacion()

    #mago ataque 
    Asesino.atacar()

    #Crear objeto

    pocion = Objeto("pocion de vida ","consumible")
    espada = Objeto("excalibur","arma")

    Asesino.inventario.agregar_objetos(espada)
    Asesino.inventario.agregar_objetos(pocion)

    #recibir danio
    Asesino.recibir_Danio(9999999999999)

    Asesino.mostrar_informacion()

if __name__ == "__main__":
    main()