class Pasta:
  def __init__(self):
    self.ajies = 0
   
  def picante(self):
    if self.ajies <=10:
     self.ajies += 5
  def suavizar(self):
    self.ajies -= 1
  def muy_picante(self):
    return self.ajies > 10

class Pizza:
  def __init__(self):
    self.condimento = "adobo"
  def picante(self):
    self.condimento = "cayena"
  def suavizar(self):
    self.condimento = "oregano"
  def muy_picante(self):
    return self.condimento == "cayena"

class Chef:
  def __init__(self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
  
  def picantear(self):
    if self.plato_del_dia.muy_picante():
      raise Exception("El plato ya está demasiado picante")
    else:
      self.plato_del_dia.picante()
      
class AyudanteDeCocina:
  def suavizar(self, plato):
    plato.suavizar()