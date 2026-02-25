contador=0
soma=0
while contador > 4:
    contador+=1
    nota = float(input(f"insira o {contador} nota"))
    soma+=nota


media= soma/contador
print("A media foi ",media)

if media >=7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")

#aluno aprovado = +7
#aluno reprovado = -7

 