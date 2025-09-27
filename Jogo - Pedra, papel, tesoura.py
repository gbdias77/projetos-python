#Jogar pedra papel e tesoura
jogador = input(" Escolha entre pedra, papel ou tesoura?  ")
import random
computador = random.choice(["pedra","papel","tesoura"])



#pedra > tesoura; papel > pedra; tesoura > pedra;
def verificar_resultado(jogador, computador): 
    if jogador == computador:
     print( "Empate!")

 #pedra ganha tesoura e perde para papel
    if jogador == "pedra" and computador == "tesoura":
        print ("você ganhou!")
    if jogador == "pedra" and computador == "papel":
        print ("você perdeu!")
 #papel ganha pedra e perde para tesoura       
    if jogador == "papel" and computador == "pedra":
        print ("você ganhou!")  
    if jogador == "papel" and computador == "tesoura":
        print ("você perdeu!")     
 #tesoura ganha papel e perde para pedra
    if jogador == "tesoura" and computador == "papel":
        print ("você ganhou!")
    if jogador == "tesoura" and computador == "pedra":
        print ("você perdeu!")
 

if jogador != "pedra" and jogador != "tesoura" and jogador != "papel":
     print("A escolha ",jogador,"não é válida, por favor começe o jogo novamente!")
     
else:
    verificar_resultado(jogador,computador)
    print("Você escolheu", jogador,"e a CPU escolheu", computador)
  

 
 
 
 