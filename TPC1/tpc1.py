import math

def main():
    with open("myheart.csv") as file:
        content = file.readlines()
        
    matrix = []
    
    for line in content: 
        matrix.append(list(line.strip().split(',')))

    matrix.pop(0)
    dados = {'1' : [],
            '0' : []} 
    #[idade, sexo, tensao, colesterol, batimento, hasDoenca]
    for mens in matrix:
        dados[mens[5]].append(mens[:4])
    pessoasSexo = porSexo(dados)
    print(printTable(pessoasSexo))
   # print("Porcentagem de homens com a doenca: " + str(pessoasSexo['M']/pessoasSexo['T']*100) + "% \nPecentagem de mulheres com a doenca:" + str(pessoasSexo['F']/pessoasSexo['T']*100) + "%")
    toPrint = porIdade(dados)
    print(printTable(toPrint))
    pessoasCol = porColesterol(dados)
    print(printTable(pessoasCol))
            # print("Porcentagem de pessoas com colesterol entre os " + str(resultCom) + " e " + str(resultCom + 10) +" com a doenca: " + str(pessoasCol[resultCom]*100/pessoasCol['T']) + "%")

    
def porSexo(dados):
    
    result = {'M' : 0,
              'F' : 0,
              'T' : 0}
    for mens in dados['1']:
        result[mens[1]] += 1
        result['T'] += 1
    toPrint = [["Sexo","Porcentagem"],[],[]]
    for key in result:
        toPrint[1].append(key)
        toPrint[2].append(str(result[key]*100/result['T'])+ "%")
    return toPrint
    

def porIdade(dados):
    #[30-34], [35-39], [40-44]
    result = [0,0,0]
    total = 0
    for mens in dados['1']:
        idade = (int(mens[0])-30)//5
        diff = idade - (len(result) - 1)
        while(diff > 0):
            result.append(0)
            diff -= 1
        result[idade] += 1
        total += 1
    toPrint = [["Idade","Porcentagem"],[],[]]
    i = 30
    for value in result:
        i += 5
        toPrint[1].append("["+str(i) + "," + str((i + 5))+"]")
        toPrint[2].append(str(value*100/total)+ "%")
    return toPrint

def porColesterol(dados):
    result = {'T' : 0,
               0 : 0}
    for mens in dados['1']:
        col = math.floor(int(mens[3])/10) * 10
        if col not in result:
            result[col] = 0
        result[col] += 1
        result['T'] += 1
    total = 0
    toPrint = [["Colesterol","Porcentagem"],[],[]]
    for resultCom in result:
        if(resultCom != 'T'):
            toPrint[1].append("["+ str(resultCom) + "," + str(resultCom + 10) +"]")
            toPrint[2].append(str(result[resultCom]*100/result['T'])+ "%")
    return toPrint


#dados tem que estar em lista de listas (a primeira indica oq sao as listas seguintes e os parametros e o segundo os valores)
def printTable(dados):
    i = len(dados[2])
    result = ""
    for j in dados[0]:
        result += j + " | "
    result += "\n"
    f = 0
    while(i > f):
        result += dados[1][f] + " | " + dados[2][f] + " |\n"
        f += 1
    return result
           

main()