import random

naipes = ['ouro' , 'copas' , 'espadas', 'paus'] 
numeros = ['Ás', '1', '2', '3' , '4' , '5' , '6' , '7' , '8' , '9', '10', 'Q' , 'K'] 

cartas = []

#for para naipes
for i in range(4):
 #for para numeros 
  for u in range(13):
    cartas.append(str(numeros[u])+" de "+naipes[i])

quantidades  = int(input(" Digite a quantidade de cartas"))
           
random.shuffle(cartas) 
for i in range(quantidades):
  print(cartas[i] ) 

                           