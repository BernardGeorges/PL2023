import csv
import re
import json
from statistics import mean

def main():
    ficheiro = input("Introduza o ficheiro que deseja ler:")
    file = open(ficheiro)
    delims = re.compile(r'((\w+| +)+)|({\w,?\w?})')
    if not file:
        print("Ficheiro Invalido")
        return -1
    header = file.readline()
    headline = delims.findall(header)
    headlines = []
    start = len(headline)
    func = re.findall(r'::(\w+)',header)
    print(headline)
    getNums = None
    if func: 
        start -= len(func)
    for grupo in headline:
        if grupo[2] != '':
            start -= 2
            getNums = True
        else:
            headlines.append(grupo[0])
    nome = re.match(r'(.+)\.csv',ficheiro)
    retFile = open(nome.group(1) + ".json", "w", encoding='utf8')
    retFile.write("{\n\""+nome.group(1) + "\":\n")
    ret = []
    for line in file:
        aux = {}
        i = 0
        values = delims.findall(line)
        while i < start:
            aux[headlines[i]] = values[i][0]
            i += 1
        if getNums:
            j = start
            lista = []
            while j < len(values):
                lista.append(int(values[j][0]))
                j += 1
        print(lista)
        if func:
            for funcao in func:
                aux[headlines[i]+"_"+funcao] = eval(funcao+"("+str(lista)+")")
        else: 
            aux[headlines[-1]] = lista
        #print(aux)
        ret.append(aux)
    json.dump(ret,retFile, ensure_ascii=False)
    retFile.write("\n}")
    
    

main()