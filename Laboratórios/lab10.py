#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caçadores de Tesouros
# Nome: Pedro Henrique Martins Belo
# RA: 267809
#####################################################

#Você está desenvolvendo um jogo sobre caçadores de tesouros. Em uma das fases do jogo, cada jogador controla um personagem e deve coletar os tesouros que encontrar pelo mapa. Porém, como os tesouros são pesados, cada personagem consegue carregar apenas um tesouro por vez.

#Durante a caça aos tesouros, um personagem por vez caminhará pelo mapa. Ao encontrar um tesouro pela primeira vez, o personagem irá carregá-lo junto com ele, removendo o tesouro daquele local. Caso encontre um segundo tesouro enquanto já estiver carregando um tesouro, se este tesouro encontrado possuir um valor maior do que o está sendo carregado, ele substituirá os dois tesouros, ou seja, jogará o seu tesouro de menor valor naquela posição do mapa e carregará o tesouro de maior valor consigo. Após o primeiro personagem terminar seu caminho no mapa, o segundo personagem irá percorrê-lo, e assim por diante.

#Como você gosta de antever os resultados da partida, você resolveu criar um programa para indicar o valor que cada personagem irá coletar.

#Como entrada o seu programa, você deverá ler dois inteiros, n e m, que indicam a quantidade de linhas e colunas do mapa, respectivamente. Nas próximas n linhas, o seu código receberá as linhas do mapa, com valores inteiros entre 0 e 9, sendo que 0 indica uma posição sem tesouro e valores maiores que 0 representam o valor do tesouro naquela posição. Na sequência, você deverá ler o inteiro q, indicando a quantidade de personagens. Para cada personagem, você deverá ler duas linhas, sendo a primeira linha com dois valores inteiros, representando a linha e a coluna inicial do personagem (por exemplo, a posição no canto superior esquerdo do mapa é denotada por 0 0), e a segunda linha representando os movimentos realizados pelo personagem. Os seguintes caracteres são utilizados para representar os movimentos:

#N: representa uma movimentação para o norte, ou seja para a linha acima da posição atual.
#S: representa uma movimentação para o sul, ou seja para a linha abaixo da posição atual.
#O: representa uma movimentação para o oeste, ou seja para a coluna à esquerda da posição atual.
#L: representa uma movimentação para o leste, ou seja para a coluna à direita da posição atual.
#Você pode considerar que todos os movimentos são válidos, sempre mantendo o personagem dentro do mapa.

#Como saída o seu programa deve imprimir o valor do tesouro encontrado para cada um dos personagens. Caso o personagem não encontre nenhum tesouro, o valor deverá ser igual a 0. A seguinte mensagem deve ser impressa para cada caçador, sendo C o número do caçador e T o valor do tesouro:

#Caçador C: T

#Resolução:

def seguinte(l,c,letra, mapa):
    if letra == 'N':
        l -= 1
    if letra == 'S':
        l += 1
    if letra == 'L':
        c += 1
    if letra == 'O':
        c -= 1
    return mapa[l][c], l, c

def faztroca(l,c,mapa, valor_atual, valor_seguinte, indice):
    aux = valor_atual
    valor_atual = valor_seguinte
    mapa[l][c] = aux
    return valor_atual, mapa
   
# Leitura do mapa
n, m = [int(i) for i in input().split()]
list = []
mapa = []
for _ in range(n):
  linha = [int(i) for i in input().split()]
  mapa.append(linha)
q = int(input())
for i in range(q):
    l, c = [int(i) for i in input().split()]
    caminho = str(input()).upper()
    valor_atual = mapa[l][c]
    for indice in range(len(caminho)):
        letra = caminho[indice]
        valor_seguinte, x, y = seguinte(l,c,letra, mapa)
        

        if valor_atual < valor_seguinte:
            valor_atual, mapa = faztroca(x,y, mapa, valor_atual, valor_seguinte, indice)
        if indice == 0:
            mapa[l][c] = 0
        l=x
        c=y
        if indice == len(caminho) - 1:
            print(f"Caçador {i+1}: {valor_atual}")
            
            
                
       



