# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento
# que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou,
# ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano,
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

ano_correto = False
while (ano_correto == False):
    try:
        nome = input("Qual seu  nome?\n")
        a = int(input("Entre com ano nascimento entre 1922 e 2021\n"))
        if (a >= 1922) and (a <= 2021):
            b = 2022-a
            print(nome)
            print(b)
            ano_correto = True
        else:
            print("Digite um numero entre 1922 e 2021\n")
    except:
        print("Caracter invalido\n")
