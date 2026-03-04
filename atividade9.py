maior = float()
menor = float()
soma = 0
acima_100 = 0
for cont in range(10):
    temperatura = float(input(f"Digite a {cont + 1} temperatura: "))
    soma += temperatura

    if cont == 0:
        maior = temperatura
        menor = temperatura

    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

    soma += temperatura

    if temperatura > 100:
        acima_100 += 1

media = soma / 10

print("resultado")
print(f"maior temperatura é {maior}")
print(f"menor temperatura é {menor}")
print(f"a media das temperaturas é{media}")
print(f"a temperatura ultrapassou 100{acima_100} vezes")