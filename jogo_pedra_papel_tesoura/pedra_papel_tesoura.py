#Jogar pedra papel e tesoura
import random
nome_jogador = input("Escolha seu nome: ")
nome_adversario = input("Escolha o nome do seu adversário: ")
jogador = input("Escolha pedra, papel ou tesoura (letras minúsculas):  ")
computador = random.choice(["pedra","papel","tesoura",])

#funçao que define o resultado
def verificar_resultado(jogador, computador): 
    
    if jogador == computador:
     print(nome_jogador," Empatou com ", nome_adversario)

 #pedra ganha tesoura e perde para papel
    if jogador == "pedra" and computador == "tesoura":
        print (nome_jogador," ganhou!")
    if jogador == "pedra" and computador == "papel":
        print (nome_jogador," perdeu!")
 #papel ganha pedra e perde para tesoura       
    if jogador == "papel" and computador == "pedra":
        print (nome_jogador," ganhou!")  
    if jogador == "papel" and computador == "tesoura":
        print (nome_jogador," perdeu!")     
 #tesoura ganha papel e perde para pedra
    if jogador == "tesoura" and computador == "papel":
        print (nome_jogador," ganhou!")
    if jogador == "tesoura" and computador == "pedra":
        print (nome_jogador," perdeu!")
 

if jogador != "pedra" and jogador != "tesoura" and jogador != "papel":
     print("A escolha ",jogador,"não é válida, por favor começe o jogo novamente!")
     
else:
    verificar_resultado(jogador,computador)
    print(nome_jogador," escolheu", jogador,"e ", nome_adversario ,"escolheu", computador)
  
input()
 
 
 