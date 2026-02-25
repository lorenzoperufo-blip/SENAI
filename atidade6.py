nome = input("Insira o nome: ")
idade = int(input("Insira a idade (anos completos): "))
while idade > 120 and idade < 0:
    idade = int(input("idade(anos completos - ate 120): "))
    diasdevida = idade * 365
    print(f"{nome}, você ja viveu aproximadamente {diasdevida} dias. ")

