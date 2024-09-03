#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
# que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
with open('03_mes09.json', 'r') as file:
    dados = json.load(file)

valoresList = [dicionario['faturamento'] for dicionario in dados]
valoresList.sort()
print(valoresList)

for values in valoresList[:]:
    if values == 0 or values < 1000:
        valoresList.remove(0)

print(valoresList)

minimo = valoresList[0]
maximo = valoresList[-1:]

total = 0
for i in valoresList:
    total = i + total

mediaMensal = round(total/len(valoresList), 2)

diasAcima = 0
for j in valoresList:
    if j > mediaMensal:
        diasAcima += 1

print('Menor valor do mes: {}'.format(minimo))
print('Maior valor do mes: {}'.format(maximo))
print('Dias do mes acima da média: {}'.format(diasAcima))