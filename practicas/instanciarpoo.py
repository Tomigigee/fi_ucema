from practicapoo import mac, contador, calculadora, titan1, enterprise

#3
print(mac.precio)
mac.descuento(3)
print(mac.precio)


#4
contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
contador.valorNuevo(27)
print(contador.ultimoComando())
contador.dis()
contador.dis()
print(contador.valorActual())
print(contador.ultimoComando())

#6
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print(calculadora.valorActual())

#modelo
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())

#modelo2
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.potencia)
print(enterprise.coraza)
print(enterprise.fortalezaDefensiva())
print(enterprise.fortalezaOfensiva())
print(enterprise.necesitaFortalecerse())
print(enterprise.coraza_actual())