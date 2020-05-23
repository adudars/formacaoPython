from central_jogos import forca, adivinhacao


def escolhe_jogos():
    print("\n*** ESCOLHA O SEU JOGO ***\n")

    print("Forca(1) Adivinhação(2)")
    jogo = int(input("Escolha a sua opção: "))

    while(jogo < 1 or jogo > 2):
        jogo = int(input("Escolha uma opção válida: "))
    if(jogo == 1):
        forca.jogar()
    else:
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogos()