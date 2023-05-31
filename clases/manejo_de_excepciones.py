import cmath 

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d)/(2*a))
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


def eneavo(numero):
    try:
        return 1 / numero
    except ZeroDivisionError:
        return "no se puede dividir por 0"

print(eneavo(0)) 

def check_int_type():
  if type(x)  != int:
    raise TypeError("Only integers are allowed") 
  
#practica


lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super.append("arroz")
except "arroz" in lista_super:
    print("no puedo agregar arroz")

print(lista_super)

#Definir una función que tenga como parámetros una lista de números por un lado y un número por otro y devuelva una lista con la división de cada elemento por el número dado. Por ejemplo, si le paso ([2,4,6,8], 2), debería retornar [1,2,3,4]. Tomar las precauciones necesarias.

def lista_parametro(lista, numero_div):
    lista_nueva = []
    try:
        for numero in lista:
            numero_nuevo = numero / numero_div
            lista_nueva.append(numero_nuevo)
            print(lista_nueva)
    except ZeroDivisionError:
        print("no podes dividir por 0 pedazo de burro")
        
lista_parametro([2, 4, 6], 0)

#Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número a la lista solo si el número es positivo. De lo contrario debería generar un error indicando que el número no es positivo.

def ejercicio3(lista, num):
    try:
        if num > 0:
            lista3.append(num)
        return lista
    except:
        print("solo se puede agregar numeros positivos")
lista3 = [1,2,3,4,5]
print(ejercicio3(lista3, -8)) 