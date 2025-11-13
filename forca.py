import random

def imprime_mensagem_abertura():
    print("*****************************")
    print("Bem vindo ao jogo de forca!")
    print("*****************************")

def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    print(palavras)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    '''
    for letra in palavra_secreta:
        letras_acertadas.append("_")
    '''

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # enquanto não enforcou e não acertou:
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                # print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        if acertou:
            print("Você ganhou!")
            print(r"""
                       ___________
                      '._==_==_=_.'
                      .-\:      /-.
                     | (|:.     |) |
                      '-|:.     |-'
                        \::.    /
                         '::. .'
                           ) (
                         _.' '._
                        `"""""""`

                      PARABÉNS!
                    VOCÊ GANHOU! 
                """)

        elif enforcou:
            print("Você perdeu!")

            print(r"""
                      _____
                     /     \
                    | () () |
                     \  ^  /
                      |||||
                      |||||
                   ___|||||___
                  /   |||||   \
                 /_____________\
                    VOCÊ PERDEU!
                """)

    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
