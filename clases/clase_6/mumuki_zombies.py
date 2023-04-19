class Zombi:
  def __init__(self, un_hambre):
    self.hambre = un_hambre
  
  def sabe_correr(self):
    return self
      
  def es_un_peligro(self):
    return self.hambre > 50
  
  def recibir_danio(self, daño):
    self.hambre -= daño * 2
    
class SuperZombi:
  def __init__(self, un_hambre):
    self.hambre = un_hambre
    
  def sabe_correr(self):
    return self
    
  def es_un_peligro(self):
    return self
  def recibir_danio(self, daño):
    self.hambre -= daño
  
  def regenerarse(self):
    self.hambre += 100