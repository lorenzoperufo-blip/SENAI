#trabalho do Lorenzo E. Perufo

#Menu inicial
nome = input("Digite seu nome: ")
print(f"Bem vindo, {nome}")

while True:

#Para Escolher seu Usuário
    usuario = float(input("Qual tipo de usuário você é? 'n1- Membro' ou 'n2- Visitante' "))

    if usuario == "1":
        print("Bem vindo Membro")
        break

#Aqui é para Digitar as horas que vc quer
    if usuario == "2":
       float(input("Digite quantas horas você deseja ficar logado (maximo 4): "))

#Seu Login
    if time <= 4:
        print(f"Olá, {nome}, seu login foi feito com sucesso")
        break

    if time >= 4:
        print("Acesso negado! quantidade de horas inválida.")

#Tentar novamente
        tentativa = input("Tente novamente\n1- Sim\n2- Não\n\nEscolha: ")
        if tentativa ==1:
            continue
        elif tentativa ==2:
            break

    if usuario ==1:
        print("Bem Vindo!, tempo de login: 9h da manha, até as 18h da tarde")
        break
    
    if usuario ==2:
         print("Até a proxima!")
        break

