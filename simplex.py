import numpy as np
import sys

nameFile = sys.argv[1]

# Determina se o tableau eh otimo(nao existe negativos na linha Z)
def great(tb):                  
    for number in tb[0]:
        if number < 0:
            print("\nO tableau nao eh considerado otimo: ")
            return False
    return True

# Escolhe a coluna pivo e retorna sua posição
def chooseColumn(tb):
    pivotColumn = 0
    for pos in range(0, len(tb[0]) - 1):
        if tb[0][pos] < tb[0][pivotColumn]:
            pivotColumn = pos
    print("Coluna pivo: ", pivotColumn + 1)
    return pivotColumn

# Escolhe a linha pivo e retorna sua posição
def chooseLine(tb, column):
    listPivot = []
    for pos in range(1, len(tb)):
        number = tb[pos][column]
        colSolution = tb[pos][len(tb[0]) - 1]
        if number != 0:
            listPivot.append(colSolution / number)
        else:
            listPivot.append(-1)
    print("Linha pivo: ", np.argmin(listPivot) + 2)    
    return np.argmin(listPivot) + 1                                 #Retorna a posição do menor número nao negativo

# Faz o cálculo da nova linha pivo e retorna o tableau atualizado
def changePivotLine(tb, pc, pl):
    pivot = tb[pl][pc]
    for pos in range(0,len(tb[pl])):
        tb[pl][pos] = tb[pl][pos] / pivot
    return tb

# Atualiza as demais linhas
def changeTb(tb, cp, cl):
    newLine = tb[cl]
    cp = cp
    for lin in range(0, len(tb)):                                           #Percorre cada linha
        if lin != cl:       
            oposto = (-(tb[lin][cp]))                                       #Pega o oposto do pivo de cada linha
            for col in range(0, len(tb[0])):                                #Percorre cada número de cada linha
                tb[lin][col] = newLine[col] * oposto + tb[lin][col]         #Realiza os cálculos
    return tb

#Lê os coeficientes e insere em um vetor
def treatInput(inputString):
    return list(map(lambda x: int(x), inputString))
    
# def getInput():
    tb = []
    print("Digite todos os valores de cada restricao, separados por virgula, incluindo os coeficientes de todas as variaveis",
    "\ncaso alguma variavel nao apareca, insira 0 como coeficiente")
    print("Exemplo -> 20x1 + 60x2 + S1 = 60000. Na formula nao apresenta as variaveis Z,S2 e S3, portanto colocar 0")
    #Adiciona um elemento em um vetor, onde cada elemento é um vetor de valores
    print("Digitar -> 0,20,60,1,0,0,60000")
    tb.append(treatInput(input("Digite os coeficientes de Z, separados por virgulas: ")))               
    restritions = input("Digite o numero de restricoes: ")
    for restrition in range(0, int(restritions)):
        print("Restricao ", restrition + 1, ":")
        tb.append(treatInput(input()))
    return tb

#Faz o tratamento do conteúdo do arquivo para construir uma matriz
def getFile():
    fileContent = open(nameFile, 'r').readlines()    
    tb = []
    for line in fileContent:
        tb.append(treatInput(line.replace('\n','').split(',')))
    return tb

def main():
    tb = getFile()
    while(great(tb) != True):
        print("----------------------------------------")
        cp = chooseColumn(tb)
        cl = chooseLine(tb,cp)
        tb = changePivotLine(tb,cp,cl)
        tb = changeTb(tb, cp, cl)
    print("-------------\nResultado final:\nO otimo eh: ", tb[0][len(tb[0]) - 1])
    print("Tableau:")
    for item in tb:
        print(item)   


if __name__ == '__main__':
    main()

