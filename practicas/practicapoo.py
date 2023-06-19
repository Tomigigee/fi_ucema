#3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
    def descuento(self, descuento):
        return self.precio == (self.precio * descuento)

mac = Notebook("Apple", "5", "500")

#4
class Contador:
    def __init__(self):
        self.valor = 0
    
    def inc(self):
        self.valor += 1
        self.ultimo_comando = "incremento"
    def dis(self):
        self.valor -= 1
        self.ultimo_comando = "disminucion"
    def reset(self):
        self.valor = 0
        self.ultimo_comando = "reset"
    def valorActual(self):
        return self.valor
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
        self.ultimo_comando = "actualizacion"
    def ultimoComando(self):
        return self.ultimo_comando  

contador = Contador()

#5 Agregar metodo ultimocomando que nos diga cual fue el ultimo comando que utlizamos
 
#6
class Calculadora:
    def __init__(self):
        self.numero = 0
    def cargar(self, numero):
        self.numero = numero
    def sumar(self,numero):
        self.numero += numero
    def restar(self, numero):
        self.numero -= numero
    def multiplicar(self, numero):
        self.numero = (self.numero * numero)
    def valorActual(self):
        return self.numero 

calculadora = Calculadora()

#7 Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorrion:
    def __init__(self):
        self.kilometro = [] 
        self.gramos = []

    def volar(self, km):
        self.kilometro.append(km)
    def comer(self, gramos):
        self.gramos.append(gramos)
    
    def css(self):
        if sum(self.gramos):
            return sum(self.kilometro) / sum(self.gramos)
    def cssp(self):
        pass
    def cssv(self):
        pass


#modelos 1

class Titan:
    def __init__(self, salud):
        self.salud = salud

    def recibir_ataque(self ,cantidad):
        self.salud -= (cantidad * 1.5)
    
    def esta_vivo(self):
        return (self.salud > 0)

    def destruir_casas(self):
        if (self.cuantas_casas() > 1):
            if ((self.cuantas_casas() % 1) > 0):
                self.salud -= (self.cuantas_casas() // 1) * 12.5
            else:
                self.salud -= (self.cuantas_casas() - 1) * 12.5
        else:
            print("No se puede destruir ninguna casa")
    def cuantas_casas(self):
        return self.salud / 12.5 
    def grito(self):
        return "¡Aaaarrrg!"
    def salud_actual(self):
        return self.salud
        
titan1 = Titan(100)

#modelos 2

class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5
    def encontrarPilaAtomica(self):
        if self.potencia +25 <= 100:
            self.potencia += 25
        else:
            self.potencia = 100
    def encontrarEscudo(self):
        if self.coraza +10 <= 20:
            self.coraza += 10
        else:
            self.coraza = 20

    def coraza_actual(self):
        return self.coraza
    
    def potencia_actual(self):
        return self.potencia
    
    def recibirAtaque(self, puntos):
        if self.coraza <= puntos:
            self.potencia -= puntos - self.coraza
            self.coraza = 0
        else:
            self.coraza -= puntos
            
    def fortalezaDefensiva(self):
        return (self.potencia + self.coraza)
    
    def necesitaFortalecerse(self):
        return (self.coraza == 0 and self.potencia < 20)
    
    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return 0
        else:
            return ((self.potencia - 20) / 2)

enterprise = Enterprise()


#modelos estudiantes
class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.felicidad = False

    def energia_actual(self):
        return self.energia

    def dormir(self, horas):
        if (self.energia + (horas * 12.5)) > 100:
            self.energia = 100
        else:
            self.energia += (horas * 12.5)
    
    def hacer_ejercicio(self, minutos):
        if self.energia - (minutos / 1.2) < 0:
            self.energia = 0
        else:
            self.energia -= minutos / 1.2

    def comer(self):
        if self.energia + 10 > 100:
            self.energia = 100
        else:
            self.energia += 10

class Estudiante(Persona):
    def estudiar(self, horas):
        if (self.energia - (horas * 20)) < 0:
            self.energia = 0
        else:
            self.energia -= (horas * 20)
    def aprobar(self):
        return True

estudiante = Estudiante(100)
    
        




