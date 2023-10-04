###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Um Lanche Antes da Aula
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################
                 
                    #Um Lanche Antes da Aula
#Você está no centro de Barão Geraldo e acabou perdendo a noção do tempo. Agora você tem apenas 45 minutos para chegar na Unicamp para a sua primeira aula! Entretanto, você quer comer alguma coisa antes e precisa considerar suas opções. O seu objetivo e chegar a tempo e gastar o mínimo possível.
#Você conseguiu reduzir suas escolhas a duas opções:
#Você pode pegar um ônibus até sua lanchonete preferida para comprar um lanche por L1 reais e pegar outro ônibus direto para a Unicamp. Nesse caso, você demora P1 minutos no primeiro percurso de ônibus, T minutos para comer o lanche (antes de embarcar no segundo ônibus) e P2 minutos no segundo percurso de ônibus.
#Você pode comprar um lanche em uma lanchonete próxima de onde você está por L2 reais e pegar um ônibus direto para a Unicamp. Nesse caso, você demora T minutos para comer o lanche (antes de embarcar no ônibus) e P3 minutos no percurso de ônibus.
#Como você começou a cursar a disciplina de MC102, você decidiu escrever um programa para determinar qual a melhor opção. Você pode considerar apenas o tempo para comer o lanche e o tempo dos percursos dos ônibus. Você ainda não tem um bilhete único para o ônibus, portanto ira pagar 6 reais (valor arredondado para este laboratório) por cada passagem de ônibus.
#Como entrada seu programa receberá 6 linhas com os valores inteiros correspondentes a T, L1, L2, P1, P2 e P3. Como saída, seu programa devera imprimir um valor booleano True, caso seja melhor pegar um ônibus para sua lanchonete preferida antes de ir para a Unicamp (opção 1) ou False, caso contrario (opção 2). A melhor opção é aquela com o menor gasto dentre as que te permitam chegar a tempo para a aula. Ou seja, se uma das opções não te permita chegar a tempo da aula você deve escolher a outra. Se ambas as opções te permitirem chegar a tempo e o custo for o mesmo escolha a opção 1. Se ambas as opções não te permitirem chegar a tempo escolha a que leva menos tempo e, se o tempo for o mesmo, escolha a opção 1.

#Resolução:

# Leitura da entrada
T = int(input())
L1 = int(input())
L2 = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())
O1 = True
O2 = False
T1 = P1 + T + P2 
T2 = T + P3 
C1 = L1 + 12
C2 = L2 + 6

# Comparação entre as opções e impressão da saída

if (T1 <= 45) and (T2 <= 45) and (C1 < C2):
    print(O1)
elif (T1 <= 45) and (T2 <= 45) and (C2 < C1):
    print(O2)
if (T1 > 45) and (T2 <= 45):
    print(O2)
elif (T1 <= 45) and (T2 > 45):
    print(O1)
if (T1 <= 45) and (T2 <= 45) and (C1 == C2):
    print(O1)
if (T1 > 45) and (T2 > 45) and (T1 < T2):
    print(O1)
elif (T1 > 45) and (T2 > 45) and (T2 < T1):
    print(O2)
if (T1 > 45) and (T2 > 45) and (T1 == T2):
    print(O1)
