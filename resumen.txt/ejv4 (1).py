"""
En un curso lleno de buenas personas, Tomás Gigena se revela y comienza a hacer desastres. 
Tiene una ira inicial la cual puede ir aumentando o disminuyendo, al igual que una orientacion sexual (homo) y una personalidad (ñoqui)
Puede pegarle_al_profe y esto incrementará su ira en la cantidad de fuerza con que le haya pegado. 
También es capaz de dar_el_presente cuando no dijeron su nombre, lo que lo hace enfurece aún más y su ira aumenta en 20. 
También sabe responder si esta_en_su_prime, cuando su ira es mayor a 90. 
Finalmente, es capaz de matar_compañeros, y esto depende de su ira. Si es máxima (ira=100), puede matar 10 tipos, 
si no es másxima, matará siguiendo la proporción.

Tiene un compañero, Alejandro Arias, que comparte los mismos metodos, pero el tiene una orientacion distinta (bi) y una personalidad
distinta (ex-ceo)
Ale no sabe estudiar, cuando le preguntan si estudia el responde: "no puedo, tengo basquet"
Con Gige pelean mucho, ambos saben atacarse y recibir golpes entre si.
Si alguno de los dos se queda sin vida, se muere y el otro se suicida
"""

class AlumnoRebelde:

    def esta_vivo(self):
        return self.vida >= 0

    def suicidar(self,persona):
        if persona.esta_vivo() is False:
            self.vida = -1
        self.verificar_estado()

    def verificar_estado(self):
        if not self.esta_vivo():
            raise Exception(f"{self.nombre} ha muerto, la sociedad ahora es mejor")

    def pegarle_al_profe(self, fuerza):
        self.verificar_estado()
        self.ira += fuerza

    def dar_el_presente(self):
        self.verificar_estado()
        self.ira += 20
        return ("AAAAAAA ESTOY ENOJADO")

    def matar_compañeros(self):
        self.verificar_estado()
        kills = int(self.ira / 10)
        return (f"VOY A MATAR {kills} PIQUETEROS")

    def recibir_ataque(self, daño):
        self.verificar_estado()
        self.vida -= daño
        self.ira += daño
        return ("a sos un forro")

    def atacar(self, persona, fuerza):
        self.verificar_estado()
        persona.recibir_ataque(fuerza)
        return (f"{self.nombre}: toma {persona.nombre} puto",f"{persona.nombre}: {persona.recibir_ataque(fuerza)} {self.nombre}")

    def esta_en_su_prime(self):
        self.verificar_estado()
        return self.ira >= 90

class TomasGigena(AlumnoRebelde):
    def __init__(self,ira,vida):
        self.nombre = "gige"
        self.ira = ira
        self.vida = vida
        self.orientacion = "homo"
        self.personalidad = "ñoqui"

class AlejandroArias(AlumnoRebelde):
    def __init__(self,ira,vida):
        self.nombre = "ale"
        self.ira = ira
        self.vida = vida
        self.orientacion = "bi"
        self.personalidad = "ex-ceo"
    
    def estudiar(self):
        return ("No puedo, tengo basquet")
    
class AlumnoProdigio:

    def atacar(self):
        return "yo no ataco pa"

    def esta_en_su_prime(self):
        return "siempre estoy en mi primee"

    def dar_el_presente(self):
        return ("Acaa matias brunn")

    def reir(self):
        return f"{self.nombre}: jajajajjaajajaja"

class LuchitoBrun(AlumnoProdigio):
    def __init__(self):
        self.nombre = "mati"
        self.ira = 0
        self.vida = 100
        self.orientacion = "hetero"
        self.personalidad = "superdotado"
    
    def compañero(self,persona):
        if persona.esta_vivo() is False:
            return self.reir()
        else: return f"ya te va a tocar {persona.nombre}"


ale_arias = AlejandroArias(50,100)
gige = TomasGigena(50,100)
mati = LuchitoBrun()


print(gige.matar_compañeros())
print(ale_arias.atacar(gige,50))
print(gige.atacar(ale_arias,50))
print(mati.compañero(ale_arias))
print(mati.esta_en_su_prime())
print(ale_arias.estudiar())

    

