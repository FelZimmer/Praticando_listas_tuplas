convidados = ['Ana', 'Pedro', 'Carlos']
while True:

    print(f"Lista atual de convidados: {", ".join(convidados)}")
    nome_novo_convidado = input("Digite o nome do novo convidado: ")
    nova_posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

    if nova_posicao >= 0:
        convidados.insert(nova_posicao,nome_novo_convidado)
    else:
        print("Digite um numero de entrada positiva")
    print(f"Lista atualizada de convidados: {", ".join(convidados)}")

    match int(input("""
    1 - Sim
    2 - Nao
    Quer Adicionar mais alguem? """)):
        case 1:
            print(f"Lista atualizada de convidados: {", ".join(convidados)}")
            continue

        case 2:

            print(f"Lista atualizada de convidados: {", ".join(convidados)}")
            break

