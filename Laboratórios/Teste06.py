
# Leitura de dados
notas = []
pesos = []
notasxpesos = []
n = int(input())
for i in range(0, n):
    nota = float(input())
    notas.append(nota)
for i in range(0, n):
    peso = float(input())
    pesos.append(peso)
for i in range(0, len(notas)):
    notasxpesos.append(notas[i]*pesos[i])
# Cálculo da média ponderada dos laboratórios
somaNotas = 0
somaPesos = 0
for i in range(0, len(notasxpesos)):
     somaNotas += notasxpesos[i]
     somaPesos += pesos[i]
     media = somaNotas/somaPesos
# Verificação da situação do aluno
if media >= 5:
# Caso o aluno tenha sido aprovado por nota
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    print("Situacao: Aprovado por nota")
    print(f'Nota final:', format(media, ".1f").replace(".", ","))
elif media < 2.5:
# Caso o aluno tenha sido reprovado por nota
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    print("Situacao: Reprovado por nota")
    print(f'Nota final:', format(media, ".1f").replace(".", ","))
else:
# Cálculo da nota do exame, caso o aluno tenha ido para o exame
    N = int(input())
    notasDoExame = []
    pesosDoExame = []
    notasxpesosExame = []
    for i in range(0, N):
        pesosEx = int(input())
        pesosDoExame.append(pesos[pesosEx - 1])
    for i in range(0, N):
        notasEx = float(input())
        notasDoExame.append(notasEx)
    for i in range(0, len(notasDoExame)):
        notasxpesosExame.append(notasDoExame[i]*pesosDoExame[i])
    somaNotasDoExame = 0
    somaPesosDoExame = 0
    for i in range(0, len(notasxpesosExame)):
        somaNotasDoExame += notasxpesosExame[i]
        somaPesosDoExame += pesosDoExame[i]
        mediaEx = somaNotasDoExame/somaPesosDoExame
        notaFinal = min(5, (mediaEx + media)/2)
    if notaFinal >= 5:
# Caso o aluno tenha sido aprovado no exame
        print("Media laboratorios:", format(media, ".1f").replace(".", ","))
        print("Situacao: Aprovado no exame")
    else:
# Caso o aluno tenha sido repravado no exame
        print("Media laboratorios:", format(media, ".1f").replace(".", ","))
        print("Situacao: Reprovado no exame")
    print("Nota final:", format(notaFinal, ".1f").replace(".", ","))







