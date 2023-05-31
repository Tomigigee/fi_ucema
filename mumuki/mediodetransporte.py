class MedioDeTransporte:
  def __init__(self, un_combustible):
    self.combustible = un_combustible
  
  def cargar_combustible(self, cantidad):
    self.combustible += cantidad
  
  def entran_personas(self, personas):
    return personas <= self.maximo_personas()
  
class Moto(MedioDeTransporte):
  def maximo_personas(self): 
    return 2
  def recorrer(self, distancia):
    self.combustible -= distancia
    
class Auto(MedioDeTransporte):
  def maximo_personas(self):
    return 5
  def recorrer(self, distancia):
    self.combustible -= (distancia/2)

class Colectivo(MedioDeTransporte):
  def __init__(self):
    super().__init__(100)
    self.pasajeros = 0
  def recorrer(self, kilometros):
    self.combustible -= (kilometros * 2)
    
  def entran_personas(self, personas):
    return True
  
  def cargar_combustible(self, combustible_nuevo):
    super().cargar_combustible(combustible_nuevo)
    self.pasajeros = 0  
