#Entrada input del usuario 
nombre = input('Introduce tu nombre: ') 
# Salida 
print("Hola, " + nombre) 
print(type(nombre)) 

#Entrada por parte del usuario como número entero 
num = int(input('Introduce un número: ')) 
add = num+1 
# Salida 
print(add) 

a, b, c = map(int, input("Introduzca los números: ").split()) 
print("Los números son: ", end = " ") 
print(a, b, c) 

""" List = list() 
Set = set() 
l = int(input("Introduzca el tamaño de lalista: ")) 
s = int(input("Introduzca el tamaño del Set: ")) 
print("Introduzca los elementos de lalista:") 
for i in range(0, 1): 
    list.append(int(input())) 
print("Introduzca los elementos del Set:") 
for i in range(0, 5): 
    Set.add(int(input())) 
print(list) 
print(set)  """

List = list(map(int, input("Introduzca los elementos de la lista:").split())) 
Set = set(map(int, input("Introduzca los elementos del Set: ").split())) 
print(List) 
print(Set) 

T = (2, 3, 4, 5, 6) 
print("Tupla inicial") 
print(T) 
L = list(T) 
L.append(int(input("Introduzca el nuevo elemento: "))) 
L = tuple(L) 
print("Tupla final") 
print(T) 