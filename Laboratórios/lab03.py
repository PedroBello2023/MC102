###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Investimento em Renda Fixa
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

                       #Investimento em Renda Fixa
#Seu amigo João vendeu um imóvel e não sabe como investir o dinheiro que recebeu com o negócio. João é uma pessoa que nunca investiu e possui alguns receios quando se trata do assunto.
#Sendo assim, João pediu o seu conselho sobre investimentos. Dentre as opções mais seguras para investimento, você sugeriu a poupança, o CDB (Certificado de Depósito Bancário), e os títulos do Tesouro Nacional (Tesouro Direto). Existem vários tipos de títulos do Tesouro Nacional, mas aqui iremos considerar apenas os títulos com juros pré-fixados.
#João se interessou pela poupança, por ser um investimento com alta liquidez (ou seja, ele pode resgatar o dinheiro a qualquer momento), e pelo Tesouro Nacional, por ter um bom rendimento e ter fortes garantias.
#A remuneração da poupança é isenta de imposto de renda. A remuneração do Tesouro Direto é sujeita a tributação de imposto de renda sobre o rendimento. A tributação sobre o rendimento tem as seguintes regras:
#22,5%, se o valor ficou aplicado até 180 dias;
#20%, se o valor ficou aplicado de 181 a 360 dias;
#17,5%, se o valor ficou aplicado de 361 a 720 dias;
#15%, se o valor ficou aplicado mais de 720 dias.
#João foi conservador na sua escolha e escolheu a poupança. Depois de alguns anos, João voltou a conversar com você sobre o assunto e pediu para que você fizesse um programa que calcule o rendimento das duas opções e informe qual teria sido a melhor opção, se ele soubesse de antemão qual seria a evolução dos juros da poupança no momento em que ele fez o investimento.
#Como entrada, você receberá: o montante inicial em reais; o número de dias d que o valor ficou aplicado; o valor percentual acumulado dos juros da poupança para o período; o valor percentual pré-fixado dos juros do Tesouro Direto no dia que ele aplicou o dinheiro na poupança.
#Lembre-se: o rendimento da poupança é calculado como o montante inicial vezes o valor dos juros no período. Já o rendimento do tesouro é calculado como o montante inicial vezes o valor pré-fixado dos juros para o período menos o imposto de renda. Note que os valores de entrada para os juros estão em porcentagem.
#Como saída, você deve imprimir o rendimento da poupança e o rendimento do tesouro direto. Por fim, você deve indicar qual das duas opções teve maior rendimento.

#Resolução:

# leitura de dados

# M = Montante inicial em Reais 
# D = Número de dias que o valor ficou aplicado
# P = Percentual dos juros acumulados da poupança
# T = Percentual do tesouro direto 

#Entrada 

M = float(input())
D = int(input())
P = float(input())
T = float(input())


# cálculo dos rendimentos

if (D <= 180):
    i = 22.50/100
elif (180 < D <= 360):
    i = 20/100
elif (360 < D <= 720):
    i = 17.50/100
elif ( D > 720):
    i = 15/100

tesouro = ((M*(T/100)) - i*(M*(T/100)))
poupanca = (M*(P/100))


# Impressão da saída

print("Rendimento poupança: {:.2f}".format(poupanca))
print("Rendimento tesouro: {:.2f}".format(tesouro))

if poupanca > tesouro:
	print("Maior rendimento: poupança")
else:
	print("Maior rendimento: tesouro")