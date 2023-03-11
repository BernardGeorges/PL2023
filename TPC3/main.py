import re
import json

def getSeculo(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

def porAno(dicios):
    ret = {}
    for dicionario in dicios:
        ano = dicionario['date'].split("-")[0]
        if ano not in ret.keys():
            ret[ano] = 0
        ret[ano] += 1
    return ret

def porNomes(dicios):
    ret = {}
    retOrd = {}
    for dicionario in dicios:
        nomes = dicionario['name1'].split(" ")
        sec = getSeculo(int(dicionario['date'].split("-")[0]))
        if sec not in ret.keys():
            ret[sec] = ({},{})
        if nomes[0] not in ret[sec][0].keys():
            ret[sec][0][nomes[0]] = 0
        if nomes[len(nomes)-1] not in ret[sec][1].keys(): 
            ret[sec][1][nomes[len(nomes)-1]] = 0
        ret[sec][1][nomes[len(nomes)-1]] += 1
        ret[sec][0][nomes[0]] += 1
    for seculos in ret:
        if seculos not in retOrd.keys():
            prim = sorted(ret[seculos][0].items(), key=lambda x:x[1], reverse=True)
            apel = sorted(ret[seculos][1].items(), key=lambda x:x[1], reverse=True)
            retOrd[seculos] = (prim[:5], apel[:5])
    return retOrd

def parente(dicts):
    ret = {}
    par = re.compile(r',([\w+|\s+]+)\.\s*Proc')
    for dicionario in dicts:
        resN3 = par.findall(dicionario['name3'])
        resN2 = par.findall(dicionario['name2'])
        resOPT = par.findall(dicionario['nameOpt'])
        for (paren) in resN3: 
            if paren not in ret.keys():
                ret[paren] = 0
            ret[paren] += 1
        for (paren2) in resN2: 
            if paren2 not in ret.keys():
                ret[paren2] = 0
            ret[paren2] += 1
        for (parenOpt) in resOPT: 
            if parenOpt not in ret.keys():
                ret[parenOpt] = 0
            ret[parenOpt] += 1
    return ret
        
def toJson(dict):
    fileJson = open("processos.json", "w")
    for line in dict[:10]:
        json.dump(line,fileJson)    
    
    

file = open("processos.txt")

comp = re.compile(r'(?P<id>\d+)::(?P<date>(\d|-)+)::(?P<name1>[^_]+)::(?P<name2>[^_]+)::(?P<name3>[^_]+)::(?P<nameOpt>[^_]*)::$')
dicts = []

for linha in file.readlines():
    res = comp.search(linha)
    if res: 
        dicts.append(res.groupdict())
        

#print("end")
#print(porAno(dicts))
#print(porNomes(dicts))
print(parente(dicts))
#print(dicts[0])
toJson(dicts)

