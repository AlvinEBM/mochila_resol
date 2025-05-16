
capacidad = 20
peso_objeto = [10, 4, 7, 5, 3, 3, 2, 3]
valor_objeto = [4, 3, 3, 2, 1, 2, 1.8, 3]


valor_peso = []
n = len(peso_objeto)
for i in range(n):
    vp = valor_objeto[i] / peso_objeto[i]
    valor_peso.append(vp)


for i in range(n - 1):
    for j in range(n - i - 1):
        if valor_peso[j] < valor_peso[j + 1]:
            
            temp = valor_peso[j]
            valor_peso[j] = valor_peso[j + 1]
            valor_peso[j + 1] = temp

           
            temp = peso_objeto[j]
            peso_objeto[j] = peso_objeto[j + 1]
            peso_objeto[j + 1] = temp

           
            temp = valor_objeto[j]
            valor_objeto[j] = valor_objeto[j + 1]
            valor_objeto[j + 1] = temp


peso_total = 0
valor_total = 0

print("Objetos agregados a la mochila:\n")
for i in range(n):
    if capacidad == 0:
        break
    if peso_objeto[i] <= capacidad:
        print(f"- Objeto completo: peso {peso_objeto[i]}, valor {valor_objeto[i]}")
        peso_total += peso_objeto[i]
        valor_total += valor_objeto[i]
        capacidad -= peso_objeto[i]
    else:
        fraccion = capacidad / peso_objeto[i]
        valor_fraccion = valor_objeto[i] * fraccion
        print(f"- Objeto fraccionado: {fraccion*100:.2f}% de peso {peso_objeto[i]}, valor ganado {valor_fraccion:.2f}")
        peso_total += capacidad
        valor_total += valor_fraccion
        capacidad = 0

print("\nResumen:")
print(f"Peso total en la mochila: {peso_total} kg")
print(f"Valor total ganado: S/.{valor_total:.2f}")
