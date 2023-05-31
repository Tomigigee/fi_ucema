# Dada la siguiente clase resolvé los siguientes ejercicios y respondé las preguntas:

class BrujoHogwarts:
    def __init__(self, mascota, casa, escoba):
        self.puntos = 10
        self.mascota = mascota
        self.casa = casa
        self.escoba = escoba

    def get_mascota(self):
        return self.mascota

    def get_casa(self):
        return self.casa

    def entrenar_quidditch(self, escoba_alternativa):
        self.escoba == escoba_alternativa
        self.puntos += 1

    def jugar_quidditch(self):
        self.puntos += 4
    
    def recitar_himno_de_casa(self):
        print("Y cuando al final de los siete años te marches por rumbos inciertos y extraños llévate el espíritu de Hogwarts contigo.\n¡Y que Gryffindor guíe tu camino!")

# a) ¿Cuál es el nombre de la clase? el nombre de la clase es BrujoHogwarts
 
# ¿Cuál es el estado de un BrujoHogwarts? El estado es self.puntos, self.maascota, self.casa, self.escoba
 
# ¿Qué mensajes entiende el BrujoHogwarts? entiende get_mascota, get_casa, entrenar_quidditch, jugar_quiditch, recitar_himno_de_casa

# b) Instanciá al BrujoHogwarts Harry, que es tiene como mascota una lechuza, es de la casa de gryffindor,
# tiene una escoba nimbus 2000

# c) Definir el método jugar_quidditch que por anota 4 puntos de Harry
# d) Definir un método recitar_himno_de_casa que retorne las últimas dos frases del himno de la casa, las cuales son:

# "Y cuando al final de los siete años te marches por rumbos inciertos y extraños llévate el espíritu de Hogwarts contigo.
# ¡Y que Gryffindor guíe tu camino!"
