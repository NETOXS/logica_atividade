#Questão 1

#Um conjunto  pode ser uma coleção de elementos que são únicos.
#Isso significa que um conjunto não pode conter elementos duplicados.
#A ordem dos elementos não importa e são  muito úteis para realizar operações de intersecção, união e diferença.

#Exemplo:

conjunto_vazio = set()
print(conjunto_vazio)  
conjunto_numeros = {1, 2, 3, 4, 5}
print(f"O conjunto é: {conjunto_numeros}\n")  

#Operações:
print("Agora veremos operações:\n")
conjunto_a = {8, 4, 5}
conjunto_b = {2, 9, 5}
print(f"Conjunto A:{conjunto_a}")
print(f"Conjunto B:{conjunto_b}")

# União
uniao = conjunto_a.union(conjunto_b)
print(f"União dos conjuntos é: {uniao}")  

# Interseção
intersecao = conjunto_a.intersection(conjunto_b)
print(f"A intersecção é: {intersecao}")  