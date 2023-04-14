class Golondrina:
  def __init__(self, energia): #definimos el estado del objeto
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
  
  def esta_feliz(self):
    return self.energia > 50

class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_feliz(self):
    return self.energia > 500

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)

#Tareas: Hacer que las golondrinas entiendan el mensaje esta_feliz(), y que devuelva si está feliz (que es cuando tienen de energía más de 50) y para los dragones, implementar ese método, pero están felices cuando tienen más de 500 de energía
