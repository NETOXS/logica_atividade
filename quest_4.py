#Questão 4

total_alunos = 18
portugues_e_ciencias = 6
portugues_e_matematica = 5
matematica_e_ciencias = 9
tres_materias = 2

apenas_matematica = total_alunos - (portugues_e_ciencias + portugues_e_matematica + matematica_e_ciencias - 2 * tres_materias)

print("O número de alunos que farão recuperação somente em Matemática é:", apenas_matematica)