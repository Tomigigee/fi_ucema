class Sobreviviente:
  def __init__(self, una_adrenalina):
    self.adrenalina = una_adrenalina
  def atacar(self, contrincante):
    if not contrincante.es_un_peligro():
      contrincante.recibir_danio(self.adrenalina/2)
      self.adrenalina += 20
    else:
      raise Exception("Es peligroso atacar a este zombi")
    