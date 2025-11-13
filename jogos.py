import forca
import adivinhacao

print("*****************************")
print("Escolha o seu jogo!")
print("*****************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    print("Jogando forca")
    forca.jogar()

else:
    print("Jogando advinhação")
    adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
