# Asignación 1 - Técnicas de Programación - Pedro Rodriguez Quesada

import math

# Funcion que suma 2 números
def sumaNumeros(x, y):
    return x + y

# Funcion que resta 2 números
def restaNumeros(x, y):
    return x - y

# Funcion que multiplica 2 números
def multiplicaNumeros(x, y):
    return x * y

# Funcion que divide 2 números
def divideNumeros(x, y):
    return x / y

# Funcion que determina si un numero es primo
def esPrimo(x):
    if x < 1:
        return 'El numero si es primo'
    elif x == 2:
        return 'El numero no es primo'
    else:
        for i in range(2, x):
            if x % i == 0:
                return 'El numero no es primo'
        return 'El numero si es primo'  

# Funcion que determina si un numero es palíndromo
def esPalidromo(x): 
    x = str(x)
    if x == x[::-1]: 
        print("Si es palíndromo")
    else: 
        print("No es palíndromo")

#Menú de opciones
print("Seleccione una opción.")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5.Verificar número primo")
print("6.Veficar número palíndromo")

while True:
    # Usuario ingresa la opción
    opcion = input("Indique la operación deseada: ")

    # Verificar las opciones
    if opcion in ('1', '2', '3', '4', '5', '6'):
       
        if opcion in ('1', '2', '3', '4'):
         num1 = float(input("Ingrese el primer número: "))
         num2 = float(input("Ingrese el segundo número: "))

         if opcion == '1':
            print(num1, "+", num2, "=", sumaNumeros(num1, num2))

         elif opcion == '2':
            print(num1, "-", num2, "=", restaNumeros(num1, num2))

         elif opcion == '3':
            print(num1, "*", num2, "=", multiplicaNumeros(num1, num2))

         elif opcion == '4':
            print(num1, "/", num2, "=", divideNumeros(num1, num2))

        
        if opcion in ('5', '6'):
            num = int(input("Ingrese el número que desea analizar: "))
            if opcion == '5':
                print(esPrimo(num))

            elif opcion == '6':
                esPalidromo(num)

        # Verificar si el usiario tiene otra operacion pendiente
        siguienteOperacion = input("¿Desea realizar otra oparación? (si/no): ")
        if siguienteOperacion == "no" or siguienteOperacion == "n":
            break    

    else:
        print("Opción invalida")