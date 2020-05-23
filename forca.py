import random

def jogar():
    enforcou = False
    acertou = False
    erros = 0
    letras_escolhidas = []

    #########
    imprime_mensagem_abertura()
    palavra_secreta = define_palavra_secreta()
    letras_acertadas = inicializa_forca(palavra_secreta)
    imprime_forca(letras_acertadas,erros)
    #########

    while(not enforcou and not acertou):
        chute = entrada_chute()
        if(chute in letras_escolhidas):
            imprime_mensagem_chute_repetido()
        else:
            if(chute in palavra_secreta):
                verifica_posicioes_chute(palavra_secreta,chute,letras_acertadas)

                acertou = "_" not in letras_acertadas

                imprime_forca(letras_acertadas,erros)
                if (acertou):
                    imprime_mensagem_vencedor()
                else:
                    imprime_mensagem_acerto(letras_acertadas)
            else:
                erros = verifica_quantidade_erros(erros)
                imprime_forca(letras_acertadas,erros)
                enforcou = erros == 7
                if(enforcou):
                    imprime_mensagem_perdedor(palavra_secreta)
            letras_escolhidas.append(chute)
    imprime_mensagem_encerramento()


def imprime_mensagem_abertura():
    print("\n*** Bem vindo ao jogo de forca! ***")


def define_palavra_secreta():
    with open("central_jogos/palavras.txt") as arquivo:
        palavras = [linha.strip().upper() for linha in arquivo]

    palavra_secreta = random.choice(palavras)
    #palavra_secreta = palavras[random.randrange(0,len(palavras))]
    return palavra_secreta


def imprime_forca(letras,erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("Forca: {}".format(letras))


def inicializa_forca(palavra):
    return ["_" for letra in palavra]


def entrada_chute():
    return input("\nQual a letra? ").strip().upper()


def verifica_posicioes_chute(palavra,chute,letras):
    index = 0
    for letra in palavra:
        if (letra == chute):
            letras[index] = letra
        # if
        index += 1
    # for


def verifica_quantidade_erros(erros):
    erros += 1
    print("Você errou! {} de 6 chances.".format(erros))
    return erros


def imprime_mensagem_encerramento():
    print("\nFim do jogo!")


def imprime_mensagem_vencedor():
    print("\nVOCÊ VENCEU!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra):
    print("\nVOCÊ FOI ENFORCADO! A palavra era: {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_acerto(letras):
    print("Você acertou! Faltam {} letra(s)".format(letras.count("_")))


def imprime_mensagem_chute_repetido():
    print("Essa letra já foi escolhida!")


if(__name__ == "__main__"):
    jogar()