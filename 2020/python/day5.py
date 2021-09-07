from time import time

start_time = time()
def getFile(name):
    f = open(name, "r")
    archivo = []
    for string in f:
        archivo.append(string)
    f.close();
    return archivo

def CalcularFila(fila, low, up):
    max=pow(2, len(fila))-1;min=0;
    for f in fila:
        #print("[",min,', ',max,']')
        if f==low:
            max = min+int((max-min)/2)
        if f==up:
            min = min+int((max-min)/2)+1;
    return min

myTicket = 0;
maxTicket = 0
listaTickets = []
for codigo in getFile("day5Input.txt"):
    codigo = codigo.replace('\n','')
    fila = codigo[:7]
    asiento = codigo[7:]
    #print('|',fila,'|',asiento,'|')
    numFila = CalcularFila(fila,'F','B')
    numAsiento = CalcularFila(asiento,'L','R')
    ticket = (numFila*8+numAsiento)
    listaTickets.append(ticket)
    if(ticket>maxTicket):
        maxTicket = ticket
    #print("Fila:",numFila,'',numAsiento,' = ', ticket)

print('Hay',len(listaTickets),'tickets.')
listaTickets.sort()

for x in range(1,len(listaTickets)):
    if (listaTickets[x] - listaTickets[x-1]) > 1:
        myTicket = listaTickets[x-1] + 1

print("Solución 1:",maxTicket)
print("Solución 2:",myTicket)
print("Elapsed time: %0.10f seconds." % (time() - start_time))