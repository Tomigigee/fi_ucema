from desafios import hipo, chimuelo, maria

print("energia antes de entrenamiento", chimuelo.energia)
print("energia antes de entrenamiento", maria.energia)
print(hipo.entrenar_equipo([chimuelo, maria]))
print("energia luego del entrenamiento", chimuelo.energia)
print("energia luego del entrenamiento", maria.energia)
print(hipo.entrenamiento_intensivo([chimuelo, maria]))
print(chimuelo.energia)

""""
Ahora hacé las modificaciones en las clases Golondrina y Dragones para que un Entrenador pueda entrenar tanto a aves como dragones.
Creá una clase de AvesNoVoladoras, que come_alpiste y como su nombre indica no puede volar_en_circulos pero si correr_en_circulos disminuyendo su energía en 25.
¿Las AvesNoVoladoras son polimórficas con las aves Golondrinas desde el punto de vista del Entrenedor?¿Cómo podemos solucionar este inconveniente?
Bibliografía
"""

