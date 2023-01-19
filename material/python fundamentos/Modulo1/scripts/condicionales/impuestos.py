

salario = float(input('Ingrese su salario anual: '))


# impuestos = salario * t
if salario < 10000:
    t = 0.05
elif salario >= 10000 and salario<20000:
    t = 0.15
elif salario >= 20000 and salario<35000:
    t = 0.20
elif salario >= 35000 and salario<60000:
    t = 0.30
else:
    t = 0.45
    pass
    
impuesto = t * salario
print(f'El puesto en base a su salario ${salario}  es ${impuesto}')

print('Programa finalizado! ')









