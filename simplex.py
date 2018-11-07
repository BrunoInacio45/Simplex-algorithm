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
    print("-------------")
    print("Tableau:")
    for item in tb:
        print(item)
    print("\nResultado final:\nO otimo eh: ", tb[0][len(tb[0]) - 1])


if __name__ == '__main__':
    main()

