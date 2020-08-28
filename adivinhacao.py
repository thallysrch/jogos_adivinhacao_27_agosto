import random

def jogar():
    print("************************")
    print ("bem-vindo a adivinhação")
    print ("adivinhe qual numero estou pensando!")
    #numero_objetivo = 99
    numero_objetivo = round (random.randrange(1,101))
    #print(f"o sorteado foi: {numero_objetivo}")
    numero_tentativas = 0
    tentativa = 1
    numero_pontos = 1000

    print("Dificuldade")
    print("(1) Easy, (2) Medium, (3) Hard")

    dificuldade = int(input("Selecione o nivel de dificuldade: "))

    if(dificuldade == 1):
        numero_tentativas = 15
    elif(dificuldade == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    while(tentativa <= numero_tentativas):
        print(f"Cara, você está na tentiva: {tentativa}, de um total de: {numero_tentativas}.")
        chute_string = input("qual é o seu palpite entre (1 - 100)")
        chute = int(chute_string)

        if(chute < 1 or chute > 100):
            print("número inválido bro, tente novamente")
            exit()

        acertou = chute == numero_objetivo
        maior = chute > numero_objetivo
        menor = chute < numero_objetivo

        print(f"Você chutou: {chute}")

        if(acertou):
            print(f"Você acertou! É nóis bruxo! Você fez {numero_pontos} pontos!")
            break
        else:
            if(maior):
                print ("Você errou, este numero é MAIOR!")
            elif(menor):
                print("Você errou, este numero é MENOR!")
            pontos_perdidos = 100
            numero_pontos -= pontos_perdidos
        tentativa += 1
    print(f"fim de jogo, o número era {numero_objetivo}")

if (__name__== '__main__'):
    jogar()