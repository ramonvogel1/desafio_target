# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#  (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(num):
    x = 0
    y = 1

    fibonacciList = [0]
    
    for i in range(0, num):
        z = x + y
        fibonacciList.append(z)
        x = y
        y = z

    for j in fibonacciList:
        if j == num:
            return('Número pertence a sequencia fibonnaci!')
    
    return('Número não pertence a sequencia fibonnaci!')

variable = int(input('Entre com o número: '))
x = fibonacci(variable)
print(x)