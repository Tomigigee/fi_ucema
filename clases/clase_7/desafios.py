#!usr/bin/env python3
class AnimalAlado:
  def esta_feliz(self):
    return self.energia >= 100
  
  def comer():
    pass

class Entrenador_de_dragones:
  def __init__(self, discipulos):
    self.discipulos = discipulos
  
  def entrenar_equipo(self, discipulos):
    for discipulo in discipulos:
      discipulo.volar_en_circulos(20)
      discipulo.comer(3)
    
  def entrenamiento_intensivo(self, discipulos):
    for discipulo in discipulos:
      if not discipulo.esta_debil():
        discipulo.volar_en_circulos(50)
      else:
        raise Exception("Ya esta debil")

class Golondrina:
  def __init__(self, energia): #definimos el estado del objeto, es el constructor
    self.energia = energia

  def comer_alpiste(self, cantidad):
    self.energia += 4 * cantidad

  def comer(self, cantidad):
    self.comer_alpiste(cantidad)


  def volar_en_circulos(self, vueltas):
    self.volar(vueltas)

  def volar(self, kms):
    self.energia -= 10 + kms
  
  def esta_feliz(self):
    return self.energia > 500
  
  def esta_debil(self):
    return self.energia < 10

class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def comer(self, cantidad):
    self.comer_peces(cantidad)

  def volar_en_circulos(self, vueltas):
    self.energia -= vueltas

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_feliz(self):
    return self.energia > 500
 
  def esta_debil(self):
    return self.energia < 50


maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = Entrenador_de_dragones([chimuelo, maria])