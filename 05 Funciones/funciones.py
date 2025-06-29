#EJERCICIO 1

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#EJERCICIO 2

def saludar_usuario(nombre):
    return f"Hola {nombre}"

nombre_usuario = input("Ingrese su nombre ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#EJERCICIO 3 

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
residencia = input("Ingrese su lugar de residencia ")

informacion_personal(nombre, apellido, edad, residencia)

#EJERCICIO 4

def calcular_area_circulo(radio):
    return 3.14 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingrese el radio del círculo "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print("El área del círculo es ", area)
print("El perímetro del círculo es ", perimetro)

#EJERCICIO 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print("Equivale a", horas, "horas.")

#EJERCICIO 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
num = int(input("Ingrese un número para mostrar su tabla de multiplicar "))
tabla_multiplicar(num)

#EJERCICIO 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número "))
b = float(input("Ingrese el segundo número "))

resultados = operaciones_basicas(a, b)

print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])

#EJERCICIO 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos "))
altura = float(input("Ingrese su altura en metros "))

imc = calcular_imc(peso, altura)

print(f"Su IMC es: {imc:.2f}")

#EJERCICIO 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius "))
fahrenheit = celsius_a_fahrenheit(celsius)

print("La temperatura en Fahrenheit es ", fahrenheit)

#EJERCICIO 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número "))
b = float(input("Ingrese el segundo número "))
c = float(input("Ingrese el tercer número "))

promedio = calcular_promedio(a, b, c)

print("El promedio es:", promedio)