# Se realiza una suma entre 12 y 6 y se guarda el resultado en la variable 'suma'
suma = 12 + 6   # resultado: 18

# Se realiza una resta entre 50 y (8*2). 
# Primero se multiplica 8*2 = 16, luego 50 - 16 = 34
resta = 50 - 8*2   # resultado: 34

# Se realiza una operación con multiplicación y división.
# Primero se multiplica 7*3 = 21, luego se divide 21 / 3 = 7
# Finalmente 50 - 7 = 43
multiplicacion = 50 - 7*3 / 3   # resultado: 43.0 (tipo float por la división)

# Esta línea hace una operación pero no se guarda en ninguna variable:
# 15 / 3 + 2 * 4 - 8
# Se calcula: 15 / 3 = 5, 2 * 4 = 8, entonces 5 + 8 - 8 = 5
15 / 3 + 2 * 4 - 8   # resultado: 5, pero no se muestra porque no se imprime ni guarda

# Se muestran los resultados de las tres operaciones anteriores en pantalla
print("el resultado de la suma es:", suma)
print("el resultado de la resta es:", resta)
print("el resultado de la multiplicacion es:", multiplicacion)
