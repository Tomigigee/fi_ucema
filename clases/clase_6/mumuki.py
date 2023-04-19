class EstudianteDeVeterinaria:
  def alimentar(self, animal, gramos):
    self.animal = animal
    animal.comer(gramos)
    
  def rehabilitar(self, animal):
    animal.recibir_rehabilitacion()
  def puede_dar_el_alta(self, animal):
    return animal.esta_feliz()
    


class Gato:
  def __init__(self,una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad
    

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
  
  def recibir_rehabilitacion(self):
    self.comer(400)
  def esta_feliz(self):
    return self.energia > 30

    
    
    
    



    

class Caballo:
  def __init__(self,una_energia, una_raza):
    self.energia = una_energia
    self.raza = una_raza

  def comer(self,gramos):
    self.energia += gramos * 2

  def galopar(self,kms):
    self.energia -= kms
  
  def recibir_rehabilitacion(self):
    self.galopar(3)
    self.comer(3000)
    self.galopar(5)
  def esta_feliz(self):
    return self


class Golondrina:
  def __init__(self,una_energia, una_ciudad):
    self.energia = una_energia
    self.ciudad = una_ciudad

  def comer(self,gramos):
    self.energia += gramos / 2

  def volar_hacia(self,destino):
    self.ciudad = destino
    self.energia /=  2 
  
  def recibir_rehabilitacion(self):
    self.volar_hacia("Lihuel Calel")
  def esta_feliz(self):
    return self.ciudad == "Lihuel Calel"
    