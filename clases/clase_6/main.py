from aves import pepita, anastasia, roberta

#pepita sabe volar 
print(pepita.volar_en_circulos())
#pepita no sabe hablar
#print(pepita.hablar())
print(pepita.comer_alpiste(200))

"""" 
Sabemos que pepita es yun objeto individual/unico,
 en particular de la clase golondrinas,
 que entiende mensajes (lo que las golondrinas entienden) 
 y que tiene las caracteristicas de una golondrina (atributos)
 """

print("al comienzo", pepita.energia)
pepita.volar_en_circulos()
print("despues de volar", pepita.energia)
pepita.comer_alpiste(200)
print("despues de comer", pepita.energia)

"""Ahora sabemos que pepita cuando le damos ordenes está haciendo algo.
Y algo en su estado cambia (la energia).
"""

print("En el caso de Anastasia tiene de energía: ", anastasia.energia)
anastasia.volar_en_circulos()
print(anastasia.energia )
anastasia.comer_alpiste(200)
print(anastasia.energia)

""""Los objetos pueden entender los mismos mensajes """
print(roberta.energia)
roberta.volar_en_circulos()
print(roberta.energia)
roberta.escupir_fuego()
print(roberta.energia)
roberta.comer_peces(200)
print("energia despues de comer peces:", roberta.energia)

""""
Los objetos no saben si son polimorficos. 
Los objetos que comparten su interfaz son polimorficos. En este caso vemos un polimorfico parcial.
Para ver polimorfismo necesitamos un actor
 """