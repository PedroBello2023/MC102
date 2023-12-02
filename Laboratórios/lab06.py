###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Nota de MC102
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Nesta tarefa você deverá calcular a nota final de MC102 de um aluno, assim como a sua situação final ("Aprovado por nota", "Reprovado por nota", "Aprovado no exame" ou "Reprovado no exame"). Para o cálculo, utilizaremos as regras previstas no Plano de Desenvolvimento da Disciplina, conforme publicado no site da disciplina.

#Você receberá as notas dos laboratórios de um aluno e os pesos de cada laboratório.

#Caso a média ponderada dos laboratórios seja maior ou igual a 5,0 ou a média ponderada seja menor que 2,5:
#nota final = média ponderada dos laboratórios
#Caso a média ponderada dos laboratórios seja maior ou igual a 2,5 e menor que 5,0, você receberá a lista dos laboratórios que irão compor o exame e a nota do aluno nesses laboratórios. A nota final neste caso será dada por:
#nota final = mínimo{5, (média ponderada dos laboratórios + média ponderada do exame) / 2}
#Caso a nota final seja maior ou igual a 5,0, o aluno estará aprovado. Caso contrário, o aluno estará reprovado.

#O seu programa irá receber um inteiro N, seguido por N linhas representando as notas obtidas nos laboratórios e por N linhas representando os pesos de cada atividade. Caso o aluno tenha ficado de exame, o programa deverá receber um inteiro M, seguido por M linhas representando quais laboratórios serão utilizados no exame e por M linhas indicando a nota de cada laboratório selecionado durante o exame.

#A saída deve informar a média ponderada dos laboratórios, a situação do aluno ("Aprovado por nota", "Reprovado por nota", "Aprovado no exame" ou "Reprovado no exame") e a nota final, apresentadas da seguinte forma:

#Media laboratorios: <Média ponderada dos laboratórios>
#Situacao: <Situação do aluno>
#Nota final: <Nota final>
#Tanto a média ponderada dos laboratórios quanto a nota final deverão ser formatadas com uma casa decimal. Para fins deste laboratório, considere que os pesos dos laboratórios selecionados para o exame serão os mesmos usados antes do exame.'''

#Resolução: 

n = int(input())
soma_pesos_ex = 0
numerador_ex = 0
numerador = 0
nota_final = 0
notas = []
pesos = []
for cont  in range(n):
    notas.append(float(input()))
for con in range(n):
    pesos.append(float(input()))
soma_pesos = sum(pesos)
for c in range(n):
    soma = notas[c] * pesos[c]
    numerador += soma
    media = numerador / soma_pesos
if media >= 5:
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    print('Situacao: Aprovado por nota')
    print(f'Nota final:', format(media, ".1f").replace(".", ","))
elif media < 2.5:
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    print('Situacao: Reprovado por nota')
    print(f'Nota final:', format(media, ".1f").replace(".", ","))
else:
    e = int(input())
    nota_final = 0
    notas_ex = []
    pesos_ex = []
    for c in range(e):
        n = int(input())
        pesos_ex.append(pesos[n - 1])
    for c in range(e):
        notas_ex.append(float(input()))
        soma_pesos_ex = sum(pesos_ex)
        soma_ex = notas_ex[c] * pesos_ex[c]
        numerador_ex += soma_ex
        media_ex = numerador_ex / soma_pesos_ex
        nota_final = min(5, (media + media_ex)/2)
    if nota_final >= 5:
        print(f'Media laboratorios:', format(media, ".1f").replace(".", ","))
        print('Situacao: Aprovado no exame')
        print("Nota final:", format(nota_final, ".1f").replace(".", ","))
    else:
        print(f'Media laboratorios:', format(media, ".1f").replace(".", ","))
        print('Situacao: Reprovado no exame')
        print("Nota final:", format(nota_final, ".1f").replace(".", ","))
print(soma_ex)
print(numerador_ex)
print(soma_pesos_ex)
print(media_ex)
print(nota_final)
        

