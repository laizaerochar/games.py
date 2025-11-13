import random
def jogar():


    print("*****************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*****************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000


    print("Qual nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel ==1:
        total_de_tentativas = 20
    elif nivel ==2:
        total_de_tentativas = 10
    elif nivel ==3:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #string interpolation
        chute = int(input("Digite o número secreto entre 1 e 100: "))
        print("Você digitou ", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue #volta e continua com a próxima iteração


        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))

            break #sair do laço

        else:
            if maior:
                print("Você errou, seu chute foi maior do que o número secreto")

            elif menor:
                print("Você errou, seu chute foi menor do que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")
    print("O número secreto era", numero_secreto)

if(__name__ == "__main__"):
    jogar()