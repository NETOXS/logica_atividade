#Questão 2

A = 210
B = 210
C = 250
A_and_B = 60
A_and_C = 70
B_and_C = 50
A_and_B_and_C = 20
none = 100

total_union = A + B + C - A_and_B - A_and_C - B_and_C + A_and_B_and_C

total_people = total_union + none

print(f"o total de pessoas é {total_people}")