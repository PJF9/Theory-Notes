import itertools

iterable = [1, 2, 3, 4, 5]

combs = itertools.combinations(iterable, 3)
combs_with_rep = itertools.combinations_with_replacement(iterable, 3)
perms = itertools.permutations(iterable, 3)
prods = itertools.product(iterable, repeat=3)

print("Combinations", end='                 : ')
for comb in combs:
    print(comb, end=" ")

print()

print("Combination With Replacement : ", end='')
for comb_with_rep in combs_with_rep:
    print(comb_with_rep, end=" ")

print()

print("Permutations", end='                 : ')
for perm in perms:
    print(perm, end=" ")

print()

print("Products", end='                     : ')
for prod in prods:
    print(prod, end=" ")

print()
