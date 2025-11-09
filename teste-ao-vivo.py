nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes", 
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes", 
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha", 
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5, 8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]

#gerar um dicionário cujas chaves são os nomes e os valores são as médias dos(as) estudantes selecionados(as)
#selecionar estudantes que tenham média final maior ou igual a 9.0

#bolsistas = {expressao_chave: expressao_valor for item in iteravel if condicao}

bolsistas = {nomes_estudante: medias_estudante 
             for nomes_estudante, medias_estudante 
             in zip(nomes_estudantes, medias_estudantes) 
             if medias_estudante>=9 }

print(bolsistas)