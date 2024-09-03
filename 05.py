# 5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverte_string(string):
    stringList = []
    invertedList = []
    
    for letter in string:
        stringList.append(letter)

    for i in range(0, len(stringList)):
        invertedList.append(stringList[-1:])
        stringList.pop()

    breakNestedList = [item for sublist in invertedList for item in sublist]
    result_string = ''.join(breakNestedList)
    return result_string
    

string = input('Escreva a string que deseja inverter: ')
inverted_string = inverte_string(string)
print(inverted_string)