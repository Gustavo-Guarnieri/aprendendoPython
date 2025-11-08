notas = [
    [8.0, 9.0, 10.0],
    [9.0, 7.0, 8.0],
    [3.4, 7.0, 7.0],
    [5.5, 6.6, 8.0],
    [6.0, 10.0, 9.5]
]

# ['expressão' for 'item' in 'lista']

#Calculo média usando LIST COMPREHENSION
media = [sum(nota)/len(nota) for nota in notas]

#Calculo média usando LAMBDA
media = list(map(lambda nota: sum(nota)/len(nota), notas))

print(media)