class Zombi:
  def __init__(self, un_hambre):
    self.hambre = un_hambre

  def sabe_correr(self):
    return True

  def es_un_peligro(self):
    return self.hambre > 50

  def recibir_danio(self,puntos_de_danio):
    self.hambre -= puntos_de_danio * 2
  
  def descansar(self, minutos):
    self.hambre += minutos

class SuperZombi(Zombi):

  def es_un_peligro(self):
    return True

  def recibir_danio(self,puntos_de_danio):
    self.hambre -= puntos_de_danio

  def regenerarse(self):
    self.hambre = 100
