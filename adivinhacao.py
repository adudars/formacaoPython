import random

from central_jogos.forca import imprime_mensagem_encerramento


def jogar():
    imprime_mensagem_abertura()
    entra_rodadas = imprime_mensagem_entrada()

    while(entra_rodadas < 1 or entra_rodadas > 3):
        imprime_mensagem_invalido()
        entra_rodadas = imprime_mensagem_entrada()

    total_tentativas = define_tentativas_nivel(entra_rodadas)

    numero_secreto = random.randint(1,101)
    pontos = 1000

    for rodada in range (0,total_tentativas):
        imprime_mensagem_rodada(rodada,total_tentativas)
        chute = entrada_chute()
        while (chute < 1 or chute > 100):
            imprime_mensagem_invalido()
            chute = entrada_chute()
        imprime_mensagem_escolha(chute)

        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute
        errou = numero_secreto != chute

        if(acertou):
            imprime_mensagem_vencedor(pontos)
            break
        else:
            if(maior):
                imprime_mensagem_erro_mais()
                pontos = pontos - abs(numero_secreto - chute)
            elif(menor):
                imprime_mensagem_erro_menos()
                pontos = pontos - abs(numero_secreto - chute)
        rodada += rodada
    if(errou):
        imprime_mensagem_perdedor(numero_secreto)
    imprime_mensagem_encerramento()


def imprime_mensagem_abertura():
    print("\n*** Bem vindo ao jogo de adivinhação! ***\n")
    print("Defina o nível de dificuldade")


def imprime_mensagem_entrada():
    return int(input("Fácil(1) Médio(2) Difícil(3): "))


def define_tentativas_nivel(entra):
    if (entra == 1):
        total_tentativas = 20
    elif (entra == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    return total_tentativas


def imprime_mensagem_rodada(rodada, total):
    print("\nRodada {} de {}".format(rodada + 1, total))


def entrada_chute():
    return int(input("Qual o número? Entre 1 e 100: "))


def imprime_mensagem_invalido():
    print("Opção inválida.")


def imprime_mensagem_vencedor(pontos):
    print("\nVOCÊ ACERTOU e fez {} pontos. Parabéns!".format(pontos))


def imprime_mensagem_erro_mais():
    print("Você errou para mais.")


def imprime_mensagem_erro_menos():
    print("Você errou para menos.")


def imprime_mensagem_escolha(chute):
    print("Número escolhido: ", chute)


def imprime_mensagem_perdedor(numero):
    print("\nVOCÊ PERDEU! O número secreto era ", numero)


if(__name__ == "__main__"):
    jogar()