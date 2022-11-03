import math 
# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''
print('¡Nuestra primera calculadora!')

# Empezar aquí la resolución del ejercicio

print('ingrese un numero real')
nro1 = float(input())

print('ingrese otro numero real')
nro2 = float(input())

Suma = nro1 + nro2
print('La suma entre', nro1, 'y', nro2, 'es', Suma)

Resta = nro1 - nro2
print('La resta entre', nro1, 'y', nro2, 'es', Resta)

Multip = nro1 * nro2
print('La multiplicación entre', nro1, 'y', nro2, 'es', Multip)

Divi = nro1 / nro2
print('La división entre', nro1, 'y', nro2, 'es', Divi)

Potencia = pow(nro1,nro2)
print('La potencia entre', nro1, 'y', nro2, 'es', Potencia)
