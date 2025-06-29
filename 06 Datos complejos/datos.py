#EJERCICIO NUMERO 1
precios_frutas= {
    'banana': 1200,
    'anana': 2500,
    'melon': 3000,
    'uva': 1450
}
precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300

print(precios_frutas)

#EJERCICIO NUMERO 2
precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['pera'] = 2800

print(precios_frutas)

#EJERCICIO NUMERO 3
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#EJERCICIO NUMERO 4
contactos = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre del contacto que querés buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'.")

#EJERCICIO 5
frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

#EJERCICIO 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(int(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

#EJERCICIO 7
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos uno:", al_menos_uno)
