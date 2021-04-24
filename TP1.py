import random

print('-' * 79)
print('Bienvenidos al juego de dados')
print('-' * 79)

# Reglas del juego

print('Reglas del juego \n \n'
    'Se juegan dos rondas \n \n'
    'En la primera ambos jugadores tiran los dados, si salen 3 dados iguales suma 6 puntos,\n'
    'si salen 2 dados iguales, se vuelve a tirar el dado desigual, \n'
    'en caso de ser desigual suma solo 3 puntos, y si salen los 3 desiguales suma 0 puntos. \n \n'
    'En la segunda ronda se vuelve a tirar los dados apostando el puntaje actual \n'
    'a la paridad de la suma de los dados, si la suma de los dados resulta de la \n'
    'paridad elegida, suma el dado de mayor valor al puntaje final, y si además \n'
    'los 3 dados resultan iguales, se duplica el valor del puntaje \n'
    'En caso de no salir la paridad elegida, se resta el valor del dado de menor \n'
    'valor al puntaje del jugador.\n \n'
    'Suerte y a jugar!!!\n')

print('-' * 79)

# ENTRADA DE DATOS
nombre_1 = input('> Ingrese el nombre de el jugador 1: ')
nombre_2 = input('> Ingrese el nombre de el jugador 2: ')


# PRIMERA RONDA------------------------------------------
print('-' * 79)

input(f'{nombre_1} presione enter para tirar los dados')
print('-' * 79)

# PROCESO DE TIRADA DE DADOS 
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

puntaje_1 = 0
puntaje_2 = 0

# Comprobación de igualdad

# JUGADOR 1
if dado1 == dado2 == dado3:
    print(nombre_1, 'sacó 3 dados iguales, sumas 6 puntos')
    puntaje_1 += 6

elif dado1 == dado2 or dado1 == dado3 or dado2 == dado3:
    if dado1 == dado2:
        print(nombre_1, dado1, dado2, dado3, 'volver a tirar el dado 3')
        input('Vuelve a tirar presionando enter')
        dado3 = random.randint(1, 6)
        if dado1 == dado3:
            print(nombre_1, 'sacó todos iguales, sumás 6 puntos')
            puntaje_1 += 6
        else:
            print(nombre_1, 'sacó uno desigual, sumás 3 puntos')
            puntaje_1 += 3
    elif dado1 == dado3:
        print(nombre_1, 'sacó', dado1, dado2, dado3, 'volver a tirar el dado 2')
        input('Vuelve a tirar presionando enter')
        dado2 = random.randint(1, 6)
        if dado1 == dado2:
            print(nombre_1, 'sacó todos iguales, sumás 6 puntos')
            puntaje_1 += 6
        else:
            print(nombre_1, 'sacó uno desigual, sumás 3 puntos')
            puntaje_1 += 3
    else:
        print(nombre_1, 'sacó', dado1, dado2, dado3, 'volver a tirar el dado 1')
        input('> Vuelve a tirar presionando enter')
        dado1 = random.randint(1, 6)
        if dado1 == dado3:
            print(nombre_1, 'sacó todos iguales, sumás 6 puntos')
            puntaje_1 += 6
        else:
            print(nombre_1, 'sacó uno desigual, sumás 3 puntos')
            puntaje_1 += 3


print('Sacaste: ', dado1, dado2, dado3)
print('Puntaje: ', nombre_1, puntaje_1, 'puntos')



# JUGADOR 2
print('-' * 79)
input(f'> {nombre_2} presione enter para tirar los dados')
print('-' * 79)

# PROCESO DE TIRADA DE DADOS 
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

# PROCESO DE COMPARACIÓN DE DADOS PARA SUMA DE PUNTAJES
if dado1 == dado2 == dado3:
    print(nombre_2, 'sacó 3 dados iguales, sumas 6 puntos')
    puntaje_2 += 6

elif dado1 == dado2 or dado1 == dado3 or dado2 == dado3:
    if dado1 == dado2:
        print(nombre_2, dado1, dado2, dado3, 'volver a tirar el dado 3')
        input('> Vuelve a tirar presionando enter')
        dado3 = random.randint(1, 6)
        if dado1 == dado3:
            print(nombre_2, 'sacó todos iguales, sumás 6 puntos')
            puntaje_2 += 6
        else:
            print(nombre_2, 'sacó uno desigual, sumás 3 puntos')
            puntaje_2 += 3
    elif dado1 == dado3:
        print(nombre_2, ' sacó', dado1, dado2, dado3, 'volver a tirar el dado 2')
        input('> Vuelve a tirar presionando enter')
        dado2 = random.randint(1, 6)
        if dado1 == dado2:
            print(nombre_2, 'sacó todos iguales, sumás 6 puntos')
            puntaje_2 += 6
        else:
            print(nombre_2, 'sacó uno desigual, sumás 3 puntos')
            puntaje_2 += 3
    else:
        print(nombre_2,'sacó', dado1, dado2, dado3, 'volver a tirar el dado 1')
        input('> Vuelve a tirar presionando enter')
        dado1 = random.randint(1, 6)
        if dado1 == dado3:
            print(nombre_2, 'sacó todos iguales, sumás 6 puntos')
            puntaje_2 += 6
        else:
            print(nombre_2, 'sacó uno desigual, sumás 3 puntos')
            puntaje_2 += 3

print('Sacaste: ', dado1, dado2, dado3)
print('Puntaje: ', nombre_2, puntaje_2, 'puntos')


#SEGUNDA RONDA-------------------------------------------

print('-' * 79 )
print('Comienza la segunda ronda, momento de apostar!!')
input('Presiona enter para continuar')

print('-' * 79)
print('Puntos de ', nombre_1, ': ', puntaje_1)
print('Puntos de ', nombre_2, ': ', puntaje_2)

# ------------------ JUGADOR 1 ------------------

print('Elija la paridad a la que apostarle')
eleccion_paridad = int(input(f'> {nombre_1}, presione 1 para elegir PAR o 0 para elegir IMPAR: '))
print('-' * 79)

input(f'> {nombre_1} presiona enter para tirar los dados')
print('-' * 79)

# PROCESO DE TIRADA DE DADOS 
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print('Sacaste: ', dado1, dado2, dado3)

# PROCESO DE VERIFICACION DE PARIDAD ELEGIDA
if eleccion_paridad == 1:
    print('Elegiste par')
    if (dado1 + dado2 + dado3) % 2 == 0:
        print('La suma de los tres dados es par!')
        print('-' * 79)
        dado_mayor = max(dado1, dado2, dado3)
        print('Tu puntaje actual es: ', puntaje_1)
        puntaje_1 += dado_mayor
        print('El mayor fue: ', dado_mayor)
        print('Tu nuevo puntaje es: ', puntaje_1)
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            print('Como ADEMÁS todos los dados que tiraste también fueron par! Así que duplicas tus puntos!!!')
            puntaje_1 *= 2
            print('Puntaje duplicado: ', puntaje_1)
    else:
        dado_menor = min(dado1, dado2, dado3)
        puntaje_1 -= dado_menor
        print('No salio la paridad elegida, tus puntos quedan en: ', puntaje_1)
elif eleccion_paridad == 0:
    print('elegiste impar')
    if (dado1 + dado2 + dado3) % 2 == 1:
        print('La suma de los tres dados es impar!')
        dado_mayor = max(dado1, dado2, dado3)
        print('Tu puntaje actual es: ', puntaje_1)
        puntaje_1 += dado_mayor
        print('El dado mayor fue: ', dado_mayor)
        print('Tu nuevo puntaje es: ', puntaje_1)
        if dado1 % 2 == 1 and dado2 % 2 == 1 and dado3 % 2 == 1:
            print('Como ADEMÁS todos los dados que tiraste también fueron impar! Así que duplicas tus puntos!!!')
            puntaje_1 *= 2
            print('Puntaje duplicado: ', puntaje_1)
    else:
        dado_menor = min(dado1, dado2, dado3)
        puntaje_1 -= dado_menor
        print('No salio la paridad elegida se te restó el dado de menor valor,\n'
              ' tus puntos quedan en:', puntaje_1)
        input('Presiona enter para continuar')


# ------------------ JUGADOR 2 ------------------

# ELECCION DE PARIDAD
print('-' * 79)
print(f'{nombre_2} Elija la paridad')
eleccion_paridad = int(input(f'> {nombre_2}, presione 1 para elegir PAR o 0 para elegir IMPAR: '))
print('-' * 79)

input(f'> {nombre_2} presiona enter para tirar los dados')
print('-' * 79)

# PROCESO DE TIRADA DE DADOS 
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print('Sacaste: ', dado1, dado2, dado3)


# PROCESO DE VERIFICACION DE PARIDAD ELEGIDA
if eleccion_paridad == 1:
    print('Elegiste par')
    if (dado1 + dado2 + dado3) % 2 == 0:
        print('La suma de los tres dados es par!')
        print('-' * 79)
        dado_mayor = max(dado1, dado2, dado3)
        print('Tu puntaje actual es: ', puntaje_2)
        puntaje_2 += dado_mayor
        print('El dado mayor fue: ', dado_mayor)
        print('Tu nuevo puntaje es: ', puntaje_2)
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            print('Como ADEMÁS todos los dados que tiraste también fueron par! Así que duplicas tus puntos!!!')
            puntaje_2 *= 2
            print('Puntaje duplicado: ', puntaje_2)
    else:
        dado_menor = min(dado1, dado2, dado3)
        puntaje_2 -= dado_menor
        print('No salio la paridad elegida, tus puntos quedan en: ', puntaje_2)
        input('Presiona enter para continuar')
elif eleccion_paridad == 0:
    print('elegiste impar')
    if (dado1 + dado2 + dado3) % 2 == 1:
        print('La suma de los tres dados es impar!')
        print('-' * 79)
        dado_mayor = max(dado1, dado2, dado3)
        print('Tu puntaje actual es: ', puntaje_2)
        puntaje_2 += dado_mayor
        print('El mayor fue: ', dado_mayor)
        print('Tu nuevo puntaje es: ', puntaje_2)
        if dado1 % 2 == 1 and dado2 % 2 == 1 and dado3 % 2 == 1:
            print('Como ADEMÁS todos los dados que tiraste también fueron impar! Así que duplicas tus puntos!!!')
            puntaje_2 *= 2
            print('Puntaje duplicado: ', puntaje_2)

    else:
        dado_menor = min(dado1, dado2, dado3)
        puntaje_2 -= dado_menor
        print('No salio la paridad elegida se te restó el dado de menor valor,\n'
              ' tus puntos quedan en:', puntaje_2)
        input('Presiona enter para continuar')



print('-' * 79)

# MUESTRA DEL PUNTAJE FINAL
print(f'Resultado final:')
print(f'\t {nombre_1} sacaste: {puntaje_1}')
print(f'\t {nombre_2} sacaste: {puntaje_2}')

print('-' * 79)

# VERIFICACION DE JUGADOR GANADOR
if puntaje_1 > puntaje_2:
    print('Ganaste', nombre_1)
elif puntaje_2 > puntaje_1:
    print('Ganaste', nombre_2)
else:
    print('Hubo un empate, lo vas a dejar así?')


print('-' * 79)
print('Fin del juego')
print('/' * 79)
