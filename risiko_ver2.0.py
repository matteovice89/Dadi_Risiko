import random
def schiera_le_truppe(): 
    valido=False
    while valido==False:
        truppe=int(input('Quante truppe vuoi schierare?? '))
        if truppe <=3 and truppe > 0:
            valido=True
        else:
            print('ATTENZIONE PUOI SCHIERARE UN MINIMO DI UN''ARMATA ED UN MASSIMO DI 3')
    return truppe
    
def lancio_dadi(tiri):
    lista=[]
    for i in range(tiri):
        dado=random.randint(1,6)
        lista.append(dado)
    lista.sort()
    lista.reverse()
    return lista
    
giocatori={'attaccante':[],'difensore':[]}#giocatori sono all'interno di un diz che contiene giocatori e dadi
print('ATTACCANTE SCHIERA LE TUE TRUPPE')
attacco=schiera_le_truppe()
print('DIFENSORE SCHIERA LE TUE TRUPPE')
difesa=schiera_le_truppe()

lista=lancio_dadi(attacco)
giocatori['attaccante']=lista
lista=lancio_dadi(difesa)
giocatori['difensore']=lista
print('Il risultato del lancio dei dadi è ',giocatori)
#confronto devo confrontare il lancio dei dadi, i tiri possono essere uguali o diversi fra i giocatori
#il massimo dei confronti è il len della lista piu piccola
pa=0
pd=0#pa e pd stanno per perdita attaccante e perdita difes
confronti=0
if (len(giocatori['attaccante'])) > (len(giocatori['difensore'])):
    confronti=(len(giocatori['difensore']))
else:
    confronti=(len(giocatori['attaccante']))
(len(giocatori['attaccante']))
for i in range(confronti):
    if (giocatori['attaccante'][i])> (giocatori['difensore'][i]):
        pd+=1
    else:
        pa+=1
print('L\'attaccante perde',pa,'truppe')
print('Il difensore perde',pd,'truppe')
