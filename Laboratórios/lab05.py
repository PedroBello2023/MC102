###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - A Última Rodada
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Seu amigo está planejando uma viagem há muito tempo, mas ainda não conseguiu juntar todo o dinheiro necessário. Felizmente, ele teve a oportunidade de participar de um programa de TV onde ele tem a chance de ganhar o suficiente para pagar pela viagem. Nesse programa, ele roda uma roleta e ganha ou perde parte do prêmio de acordo com a posição que a roleta para.

#Seu amigo chegou até a última rodada e você gostaria de saber qual a chance dele conseguir o suficiente para realizar a viagem. Para isso, você pode escrever um programa em Python.

#A entrada do programa começará com uma linha contendo três inteiros N, V e P separados por um espaço, sendo que N é o numero de partes da roleta, V é o valor que seu amigo precisa para a viagem e P é o valor do prêmio que ele acumulou até essa rodada. Em seguida, a entrada contém N linhas representando cada uma das N partes da roleta. Cada parte tem o mesmo tamanho e portanto a mesma chance de ser selecionada quando seu amigo rodar a roleta. Cada linha representando uma parte da roleta estará em um dos seguintes formatos:

#+ X Reais: nesse caso, seu amigo ganha X reais.
#- X Reais: nesse caso, seu amigo perde X reais. Se o prêmio atual (P) for menor do que X ele fica com O reais.
#+ X %: nesse caso, seu amigo ganha X% do valor do prêmio atual, ou seja, o prêmio final será P mais X% de P. O valor ganho não precisa ser inteiro.
#- X %: nesse caso, seu amigo perde X% do valor do prêmio atual, ou seja, o prêmio final será P menos X% de P. O valor perdido não precisa ser inteiro. Se o prêmio atual (P) for menor do que o valor perdido ele fica com O reais.
#A saída do seu programa deve ser a probabilidade (em porcentagem) do seu amigo conseguir o suficiente para a viagem e o valor médio do prêmio a ser recebido, considerando todas as possibilidades de valores a serem recebidos. Esses valores devem ser exibidos com duas casas decimais.

#Resolução:

# Leitura da primeira linha
N, V, P = input().split()
N = int(N)
V = int(V)
P = int(P)

# Leitura da roleta

cont = 0
soma = 0
pont = 0
font = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0

if V > 0:    
    for n in range (N, 0, -1):
        a, b, c = input().split()
        a = str(a)
        b = float(b)
        c = str(c).upper()
        if a == '+' and c == 'REAIS' and b >= V - P:
            soma = soma + 1
        elif a == '+' and c == '%' and P + (b/100) * P >=  V:
            cont = cont + 1
        elif a == '-' and c == '%' and P - (b/100) * P >= V:
            pont = pont + 1
        if a == '+'  and c == 'REAIS':
            s1 = s1 + P + b
        elif a == '-' and c == 'REAIS' and b < P:
            s2 = s2 + P - b
        elif a == '-' and c == '%':
            s3 = s3 + P - (b/100) * P
        elif a == '+'  and c == '%':
            s4 = s4 + P + (b/100) * P
    
    premio_medio = (s1 + s4 + s2 + s3)/N
    prob_viagem = ((soma + cont + pont) * 100)/N

    # Imprime a probabilidade do premio final ser suficiente para a viagem
    print("{:.2f}%".format(prob_viagem))
    # Imprime o valor médio do premio final a ser recebido
    print("R$ {:.2f}".format(premio_medio))

elif V == 0:
    for n in range (N, 0, -1):
        a, b, c = input().split()
        a = str(a)
        b = float(b)
        c = str(c).upper()
        if a == '+' and c == 'REAIS' and b >= V - P:
            soma = soma + 1
        elif a == '-' and c == 'REAIS' and b >= V - P:
            font = font + 1
        elif a == '+' and c == '%' and P + (b/100) * P >=  V:
            cont = cont + 1
        elif a == '-' and c == '%' and P - (b/100) * P >= V:
            pont = pont + 1
        if a == '+'  and c == 'REAIS':
            s1 = s1 + P + b
        elif a == '-' and c == 'REAIS' and b < P:
            s2 = s2 + P - b
        elif a == '-' and c == '%':
            s3 = s3 + P - (b/100) * P
        elif a == '+'  and c == '%':
            s4 = s4 + P + (b/100) * P
    
    premio_medio = (s1 + s4 + s2 + s3)/N
    prob_viagem = ((soma + cont + pont + font) * 100)/N

    # Imprime a probabilidade do premio final ser suficiente para a viagem
    print("{:.2f}%".format(prob_viagem))
    # Imprime o valor médio do premio final a ser recebido
    print("R$ {:.2f}".format(premio_medio))