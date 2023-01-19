

# normalmente; sobre un bucle (for, while) se itera un conjunto de valores

# for i in [12, 45, 25]:
#     print(i)



# existen palabras clave, que permite romper un bucle o saltarse una iteración de un bucle

# Break -> da por finalizado un bucle

for i in range(7):
    print(i, sep=';', end='')
    if i == 3:
        break # finaliza el bucle
