#TRABAJO RECURSIVIDAD

#EJERCICIO 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresa un número entero mayor que 0 "))

if numero < 1:
    print("Por favor ingresa un número mayor que 0")
else:
    print(f"Factoriales del 1 al {numero} ")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

#EJERCICIO 2

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingresa la posición hasta la cual deseas ver la serie de Fibonacci "))

if n < 0:
    print("Por favor ingresa un número entero positivo")
else:
    print(f"Serie de Fibonacci hasta la posición {n}")
    for i in range(n + 1):
        print(f"f({i}) = {fibonacci(i)}")

#EJERCICIO 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = float(input("Ingresa la base "))
exponente = int(input("Ingresa el exponente (entero no negativo) "))

if exponente < 0:
    print("El exponente debe ser un número entero no negativo")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

#EJERCICIO 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresa un número entero positivo "))

if numero < 0:
    print("Por favor ingresa un número entero positivo")
elif numero == 0:
    print("El número binario de 0 es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

#EJERCICIO 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("reconocer"))
print(es_palindromo("radar"))
print(es_palindromo("python"))
print(es_palindromo("neuquen"))

#EJERCICIO 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))

#EJERCICIO 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))
print(contar_bloques(5))

#EJERCICIO 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))