conjunto = {1, 3, 4, 5, 6}
conj_1 = {4, 6, 7,8,9}
conj_2 = {26, 34, 5, 6,7}

conjunto.add("R")
conjunto.discard(4)


union_conj = conj_1.union(conj_2)
intersection_conj = conj_1.intersection(conj_2)
diferent_conjunto = conj_2.difference(conj_1)
simetric_diferenc_conj = conj_1.symmetric_difference(conj_2)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 3,4,5,2}

is_sub_set = conjunto_a.issubset(conjunto_b)
is_super_set = conjunto_a.issuperset(conjunto_b)

print("União entre o conjunto {} e o conjunto {} = {}".format(conj_1, conj_2, union_conj))
print("interseção entre o conjunto {a} e o conjunto {b} = {c}".format(a = conj_1, b = conj_2, c = intersection_conj))
print("Diferença entre o conjunto {a} e o conjunto {b} = {c}".format(a = conj_1, b = conj_2, c = diferent_conjunto))
print("Diferença simétrica entre os conjuntos {a} e {b} = {c}".format(a = conj_1, b = conj_2, c = simetric_diferenc_conj))

print(is_sub_set)
print(is_super_set)
print(simetric_diferenc_conj)
