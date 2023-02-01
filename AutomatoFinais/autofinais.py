with open('autfinito2.txt', 'r') as f:
    lines = [line.rstrip() for line in f]
print(f"estado inicial: {lines[0]}")
print(f"estados finais separados por vírgula: {lines[1]}")
print(f"transições: {lines[2]}")

transition = lines[2].split(',')
t = []
for x in transition:
    itemString = x.replace('(', '')
    itemString = itemString.replace(')', '')
    item = itemString.split("|")
    t.append(item)
symbol = []
for x in t:
    if x[1] not in symbol:
        symbol.append(x[1])
aceitacao = list(map(int, lines[1].split(',')))
with open('entrada2.txt', 'r') as f:
    entradas = [line.rstrip() for line in f]
c = 0
cadeias = []
for entrada in entradas:
    c+=1
    cad = list(entrada)
    cadeias.append(cad)
f.close()

def statusCadeia(cadeiaAtual, estadoAtual):

    if(cadeiaAtual == ['$']):
        if(estadoAtual in aceitacao):
            return True
        return False
    if(cadeiaAtual == []):
        if(estadoAtual in aceitacao):
            return True
        return False

    simboloAtual = cadeiaAtual[0]
    for i in range(len(t)):
        transicaoAtual = t[i]
        estadoInicialT = int(transicaoAtual[0])
        simboloT = transicaoAtual[1]
        if((estadoInicialT == estadoAtual) and (simboloT == simboloAtual)):
            estado = int(transicaoAtual[2])
            cadeiaNova = cadeiaAtual[1:]
            
            if(statusCadeia(cadeiaNova,estado)):
                return True
    return False

print("")
with open('resultado3.txt', 'w') as f:
    for j in range(int(c)):
        cadeiaAtual = cadeias[j]
        if(statusCadeia(cadeiaAtual,0)):
            print("aceita")
            f.writelines("aceita\n")
        else:
            print("rejeita")
            f.writelines("rejeita\n")

print("\nRegistrado com sucesso")
