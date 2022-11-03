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

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
al ingresara los dos nombres completos de sus padres.
En definitiva se solicita crear una variable nueva que reuna
los apellidos.

- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres (ver la nota al final)
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''

print('Jugando con texto')
# Empezar aquí la resolución del ejercicio

print('Separando nombre de apellido con coma,')
print('por favor ingrese el nombre completo de la madre:')
mom = str(input())
nombremom, apellidomom = mom.split(', ')
# agregue un espacio despues de la coma para que el comando capitalize
# se hiciera efectivo en la fila 64

print('Ahora ingrese el nombre completo del padre:')
dad = str(input())
nombredad, apellidodad = dad.split(', ')

print('Nombre completo de hija/o:' )
sd = str(input())
nombresd, apellidosd = sd.split(',')
# aqui no fue necesario ya que apellidosd no es tomado 
# en cuenta en el resultado final

nombre_compuesto = (nombresd.capitalize() + ' '+ apellidodad.capitalize()+ ' '+ apellidomom.capitalize())
print('El nombre compuesto sería:', nombre_compuesto)

''' en el caso d elos apellidos precedidos por 'de' o 'del' 
haria un 'if' para que ambas palabras al final se mostrasen con mayusculas, 
eventualmente lo agregaré. (poniendome al dia con tareas)'''