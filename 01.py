#1) Observe o trecho de código abaixo: 
# int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
k = 0 
soma = 0

while k < indice:
    k += 1
    soma = soma + k

print(soma)

# Soma = 91