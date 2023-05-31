# Los árboles de casi todas las especies se comportan de manera similar, casi sin importar las condiciones de luz o climáticas.

# Se propone modelar este comportamiento en una clase, sabiendo que los árboles tienen como principal característica
# si son perennes (no pierden las hojas), una cantidad de agua, nutrientes y altura.
# hacer_fotosistesis(tiempo), la cual aumenta los nutrientes de la misma (1 punto cada 10 minutos),
# absorber_agua(cantidad), el cual aumenta el agua en cierta cantidad
# crecer(), en el cual, si se cumplen las condiciones de nutrientes y agua (100 puntos de cada uno),
# se aumenta la altura en 1 cm.

# El manzano tiene como característica un poco más particular,
# que genera frutos, las manzanas.

# Esto hace que la planta gaste energía en formar estos frutos,
# por lo que para crecer 1 cm necesita 150 puntos de agua
# y 200 de nutrientes.
# Además este árbol no es perenne.
# Definí las clases Arbol y Manzano,
# hacé que esta último herede de la primera agregando y/o redefiniendo los métodos necesarios.

class Arbol:
    def __init__(self):
        self.agua = 0
        self.nutrientes = 0 
        self.altura = 0
        self.perennes = True
    
    def hacer_fotosintesis(self, tiempo):
        self.nutrientes += (0.1 * tiempo)
    
    def absorber_agua(self, cantidad):
        self.agua += cantidad
    
    def crecer(self):
        if self.agua >= 100 and self.nutrientes >= 100:
            self.altura += 1
        else:
            print("no puede crecer")

class Maranzo(Arbol):
    def __init__(self):
        self.perennes = False

    def generar_manzanas(self):
        if self.agua >= 150 and self.nutrientes >= 200:
            self.altura += 1


