'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo;
- O nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos.
'''
soma_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0
if __name__ == "__main__":
    for i in range(4):
        print(f"----- {i + 1}ª Pessoa -----")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").strip().upper()

        soma_idade += idade

        if sexo == "M":
            if idade > idade_homem_mais_velho:
                idade_homem_mais_velho = idade
                homem_mais_velho = nome
        elif sexo == "F":
            if idade < 20:
                mulheres_menos_20 += 1

    media_idade = soma_idade / 4
    print("A média de idade do grupo é: {:.2f} anos.".format(media_idade))
    if homem_mais_velho:
        print("O homem mais velho é {} com {} anos.".format(homem_mais_velho, idade_homem_mais_velho))
    else:
        print("Não há homens no grupo.")
    print("Quantidade de mulheres com menos de 20 anos: {}".format(mulheres_menos_20))