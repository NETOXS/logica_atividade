#Questão 3

total_alunos = 36
alunos_erraram_todas = 4
apenas_segunda = 5
apenas_primeira = 0 
apenas_terceira = 7
primeira_e_segunda = 9
primeira_e_terceira = 10
segunda_e_terceira = 7

alunos_pelo_menos_uma = total_alunos - alunos_erraram_todas

acertam_todas = (primeira_e_segunda + primeira_e_terceira + segunda_e_terceira + apenas_segunda + apenas_terceira - alunos_pelo_menos_uma)

print(f"O número de alunos que acertaram todas as três questões é: {acertam_todas}")