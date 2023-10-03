###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Batalha Pokémon
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Pokémon é uma franquia de mídia, incluindo jogos de vídeo-game, criada na década de 90. Os jogos são bastante famosos e fazem sucesso até os dias atuais. Em todos os jogos, os personagens treinam e cuidam das criaturas que dão nome ao jogo, os pokémon (o nome Pokémon vem da junção de palavras do título original japonês: "Pocket Monsters" – o que explica também por que o termo "pokémon" não tem plural). Existem várias espécies de pokémon e cada uma aprende vários ataques distintos.

#Apesar de existirem vários mecanismos de batalhas nos diferentes jogos de Pokémon, o mais famoso é o sistema de turnos. Nesse mecanismo de batalha, um pokémon A enfrenta um pokémon B, e cada pokémon tem um valor de pontos de vida (hp, do inglês Health Points). A cada turno cada pokémon lança um ataque, sendo que o primeiro ataque é realizado pelo pokémon mais rápido, e cada ataque diminui os pontos de vida do pokémon sendo atacado. A batalha continua até que um dos pokémon não tenha mais pontos de vida.

#Cada ataque tem um valor x, que indica a força do ataque, e um multiplicador y, que indica se o ataque foi efetivo (y=2), normal (y=1), ou não efetivo (y=0.5). Um ataque diminui em x*y unidades o hp do pokémon adversário. Os valores de ataque são sempre pares, o que garante que x*y é um número inteiro.

#Você foi chamado para criar um programa que simula uma batalha em turnos do jogo Pokémon. Nessa batalha, o pokémon Ivysaur enfrenta o pokémon Pikachu. Inicialmente, seu programa deve ler dois valores inteiros que indicam a quantidade inicial de hp dos pokémon Ivysaur e Pikachu, respectivamente. Após isso, seu programa deve ler dois valores inteiros que indicam a velocidade dos pokémon Ivysaur e Pikachu, respectivamente. Em seguida, o seu programa deve ler os ataques de cada turno, sendo que cada ataque é indicado por dois valores, sendo o primeiro a força do ataque e o segundo o multiplicador de efetividade. Os valores correspondentes ao primeiro ataque são do pokémon mais rápido, enquanto os valores correspondentes ao segundo ataque são do pokémon mais lento. Ao final de cada turno, você deverá imprimir o hp de cada pokémon.

#HP Ivysaur = <HP Ivysaur>
#HP Pikachu = <HP Pikachu>
#Lembre-se que o ataque do pokémon com maior velocidade é considerado primeiro ao diminuir o hp do oponente. O hp de cada pokémon nunca será negativo, sendo que seu valor mínimo é zero. No momento que o hp de um dos pokémon chega em zero o mesmo é considerado como derrotado e a batalha é considerada encerrada, mesmo que isso ocorra no meio de um turno. Ao final da batalha, após imprimir o hp de cada pokémon, seu programa deve imprimir o nome e o hp do pokémon que venceu a batalha:

#Pokémon Vencedor: <nome pokémon vencedor>
#HP do Vencedor: <HP do pokémon vencedor>

#Resoluçaõ:

# Leitura do hp e velocidade dos pokémons


hpi = int(input())
hpp = int(input())
vi = int(input())
vp = int(input())

# Leitura dos ataques dos turnos

soma1 = 0
soma2 = 0
if vi > vp:
    while hpi > 0 and hpp > 0:
        x1 = int(input())
        y1 = float(input())
        x2 = int(input())
        y2 = float(input())
        soma1 = soma1 + (x2 * y2)
        soma2 = soma2 + (x1 * y1)
        if hpi > soma1 and hpp > soma2:
            print('HP Ivysaur = {}'.format(int(hpi - soma1)))
            print('HP Pikachu = {}'.format(int(hpp - soma2)))
        else:
            if hpi - soma1 <= 0 and hpp - soma2 > 0:
                print('HP Ivysaur = {}'.format('0'))
                print('HP Pikachu = {}'.format(int(hpp - soma2)))
                print('Pokémon Vencedor: Pikachu')
                print('HP do Vencedor: {}'.format(int(hpp - soma2)))
                hpi = 0
            elif hpi - soma1 <= 0 and hpp - soma2 <= 0:
                print('HP Ivysaur = {}'.format(int(hpi - soma1 + (x2 * y2))))
                print('HP Pikachu = 0')
                print('Pokémon Vencedor: Ivysaur')
                print('HP do Vencedor: {}'.format(int(hpi - soma1 + (x2 * y2))))
                hpp = 0 
            else:
                print('HP Ivysaur = {}'.format(int(hpi - soma1 + (x2 * y2))))
                print('HP Pikachu = 0')
                print('Pokémon Vencedor: Ivysaur')
                print('HP do Vencedor: {}'.format(int(hpi - soma1 + (x2 * y2))))
                hpp = 0
else:
    while hpi > 0 and hpp > 0:
        x1 = int(input())
        y1 = float(input())
        x2 = int(input())
        y2 = float(input())
        soma1 = soma1 + (x1 * y1)
        soma2 = soma2 + (x2 * y2)
        if hpi > soma1 and hpp > soma2:
            print('HP Ivysaur = {}'.format(int(hpi - soma1)))
            print('HP Pikachu = {}'.format(int(hpp - soma2)))
        else:
            if hpi - soma1 <= 0 and hpp - soma2 > 0:
                print('HP Ivysaur = {}'.format('0'))
                print('HP Pikachu = {}'.format(int(hpp - soma2 + (x2 * y2))))
                print('Pokémon Vencedor: Pikachu')
                print('HP do Vencedor: {}'.format(int(hpp - soma2 + (x2 * y2))))
                hpi = 0
            elif hpi - soma1 <= 0 and hpp - soma2 <= 0:
                print('HP Ivysaur = {}'.format('0'))
                print('HP Pikachu = {}'.format(int(hpp - soma2 + (x2 * y2))))
                print('Pokémon Vencedor: Pikachu')
                print('HP do Vencedor: {}'.format(int(hpp - soma2 + (x2 * y2))))
                hpp = 0 
            else:
                print('HP Ivysaur = {}'.format(int(hpi - soma1)))
                print('HP Pikachu = {}'.format('0'))
                print('Pokémon Vencedor: Ivysaur')
                print('HP do Vencedor: {}'.format(int(hpi - soma1)))
                hpp = 0
