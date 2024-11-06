#Faça um programa de implementação de um jogo de Craps. O jogador lançou um par de dados, obteve um valor entre 2 e 12. Se, na primeira partida, você tirou 7 ou 11, você um "natural" e ganhou.
#Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
#Seu objetivo agora é continuar jogando os dados até tirar esse número novamente.
#Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random

def lancar_dados():
    return random.randint(1, 6) + random.randint(1, 6)

def jogo_de_craps():
    print("Bem-vindo ao Jogo de Craps!")
    
    primeira_jogada = True
    ponto = 0
    
    while True:
        input("Pressione Enter para lançar os dados...")
        resultado = lancar_dados()
        print(f"Você tirou: {resultado}")
        
        if primeira_jogada:
            if resultado in [7, 11]:
                print("Natural! Você ganhou!")
                return
            elif resultado in [2, 3, 12]:
                print("Craps! Você perdeu!")
                return
            else:
                ponto = resultado
                print(f"Seu Ponto é: {ponto}")
                primeira_jogada = False
        else:
            if resultado == ponto:
                print("Você tirou o Ponto novamente! Você ganhou!")
                return
            elif resultado == 7:
                print("Você tirou 7 antes do Ponto! Você perdeu!")
                return

def main():
    while True:
        jogo_de_craps()
        resposta = input("Deseja jogar novamente? (s/n): ")
        if resposta.lower() != "s":
            break

if __name__ == "__main__":
    main()

