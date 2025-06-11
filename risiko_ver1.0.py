#versione 1.0
import random
giocatori={'attaccante':[],'difensore':[]}
dado=0
attacco=0
difesa=0
valido=False
while valido==False:
    attacco=int(input('Attaccante con quante armate vuoi attaccare?? '))
    if attacco <=3 and attacco > 0:
        valido=True
    else:
        print('ATTENZIONE PUOI ATTACCARE CON UN MINIMO DI UN''ARMATA ED UN MASSIMO DI 3')
valido=False #IMPORTANTE QUESTA RIGA PER RIPORTARE VALIDO A FALSE, RIFACENDO IL PROGRAMMA CON LE FUNZIONI QUESTO NON SERVIRA'
while valido==False:
    difesa=int(input('Difensore con quante armate vuoi difendere?? '))
    if difesa <=3 and difesa > 0:
        valido=True
    else:
        print('ATTENZIONE PUOI DIFENDERE CON UN MINIMO DI UN''ARMATA ED UN MASSIMO DI 3')


#lancio dei dadi
for i in range(attacco):
    dado=random.randint(1,6)
    giocatori['attaccante'].append(dado)
    giocatori['attaccante'].sort()
    giocatori['attaccante'].reverse()
for i in range(difesa):
    dado=random.randint(1,6) #con random genero numeri casuali per simulare il dodo
    giocatori['difensore'].append(dado)
    giocatori['difensore'].sort()
    giocatori['difensore'].reverse() #metto in ordine decrescente le liste per il confronto

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
