#Actividad 1

# Definimos una lista de números enteros
"""numeros = [3, 5, 20, 40, 90]

# Usamos una comprensión de listas para elevar cada número al cuadrado
cuadrados = [numero ** 2 for numero in numeros]

# Mostramos el resultado
print("Lista de números elevados al cuadrado:", cuadrados)"""

#Actividad 2

# Definimos variables de diferentes tipos
"""nombre = "Andrés"
edad = 30

# Usamos un formato de cadena f-string para insertar variables en una cadena de texto
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."

print(mensaje)"""

#Actividad 3

# Definimos una variable para la edad
"""edad = 17

# Usamos un condicional para verificar la mayoría de edad
if edad >= 18:
 print("Eres mayor de edad.")  

else:

 print("Eres menor de edad.")"""

#Actividad 4

# Definimos una variable de tipo flotante
"""saldo = 100.0

# Simulamos un ciclo de retiros de saldo hasta que el saldo sea menor que 10
while saldo > 10:
  retiro = 15.0
  saldo -= retiro
  print(f"Se ha retirado {retiro}, saldo actual: {saldo}")"""

#Actividad 5
# Definimos un diccionario con información personal
"""persona = {
    "nombre": "Erik",
    "edad": 17,
    "ciudad": "Cali"
}
# Iteramos sobre las claves y valores del diccionario
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")"""

#Actividad 6
# Usamos recursión con memoización para calcular números de Fibonacci
"""def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
# Calcular el número de Fibonacci de 50
resultado = fibonacci(50)
print("Fibonacci de 50 es:", resultado)"""

#Actividad 7

"""from decimal import Decimal, getcontext  

# Establecemos un contexto de precisión alta
getcontext().prec = 50

# Realizamos una operación matemática precisa
numero1 = Decimal('1.123456789123456789')
numero2 = Decimal('2.987654321987654321')

resultado = numero1 * numero2

# Mostramos el resultado con alta precisión
print(f"Resultado preciso: {resultado}")"""

#Actividad 8

"""import re
# Usamos una expresión regular avanzada para extraer palabras en mayúsculas de una cadena
cadena = "ESTO es un EJEMPLO de uso AVANZADO de CADENAS y Expresiones REGULARES."
# Expresión regular que busca palabras completamente en mayúsculas
patron = r'\b[A-Z]{2,}\b'
# Encontramos todas las coincidencias
palabras_mayusculas = re.findall(patron, cadena)
print("Palabras en mayúsculas:", palabras_mayusculas)"""

#Actividad 9

# Verificación de condiciones complejas usando operadores lógicos
"""a = True
b = False
c = True

# Uso de operadores lógicos avanzados (AND, OR, XOR)
resultado = (a and b) or (a and c) ^ b

print("Resultado de la operación lógica compleja:", resultado)"""

#Actividad 10

# Función que combina valores numéricos y maneja valores nulos
"""def sumar_o_default(a, b):

    # Si uno de los valores es None, retornamos 0 como valor predeterminado
    return (a or 0) + (b or 0)

# Ejemplo con diferentes combinaciones de enteros y valores None
print(sumar_o_default(5, None))  # Debería retornar 5
print(sumar_o_default(None, None))  # Debería retornar 0
print(sumar_o_default(10, 20))  # Debería retornar 30"""











