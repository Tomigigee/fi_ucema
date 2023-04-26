class Dispositivo:
  def __init__(self, una_bateria):
    self.bateria = una_bateria
  def tiene_bateria(self):
    return self.bateria > 20
  def tiene_bateria_maxima(self):
    return self.bateria == 100
  def cargar_a_tope(self):
    self.bateria = 100
  def sin_carga(self):
    return not self.tiene_bateria()

class Tablet(Dispositivo):
  def utilizar(self, minutos):
    self.bateria -= (minutos/2)

class Notebook(Dispositivo):  
  def utilizar(self, minutos):
    self.bateria -= minutos



#Vamos de paseo
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
    self.combustible = 100
    self.pasajeros = 0
  def recorrer(self, kilometros):
    self.combustible -= (kilometros * 2)
    
  def entran_personas(self, personas):
    return True
  
  def cargar_combustible(self, combustible_nuevo):
    super().cargar_combustible(combustible_nuevo)
    self.pasajeros = 0  

class Biblioteca:
  def __init__(self):
    self.libros = []
 
  def agregar_libro(self, libro):
    return self.libros.append(libro)
  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
  def titulos_disponibles(self):
    return [libro.titulo for libro in self.libros ] 

class Libro:
  def __init__(self, titulo, paginas, genero):
    self.paginas = paginas
    self.titulo = titulo
    self.genero = genero
  def es_largo(self):
    return self.paginas > 300