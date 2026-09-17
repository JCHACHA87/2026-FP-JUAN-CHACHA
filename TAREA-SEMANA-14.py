# 1. Definición de la función con parámetros de entrada
def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio  # Uso de la palabra clave 'return'


# --- Programa Principal ---

# Entrada de datos
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

# 2. Llamada a la función enviando los argumentos
resultado = calcular_promedio(n1, n2, n3)

# 3. Mostrar el resultado en pantalla
print(f"\nEl promedio final es: {resultado:.2f}")