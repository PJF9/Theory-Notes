def factorial(number: int) -> int:
    n_fact = 1
    for num in range(1, number):
        n_fact *= num

    return (number * n_fact) if (number > 0) else n_fact


def get_total_combinations(length: int, positions: int) -> int:
    if (length > positions):
        n_fact = factorial(length)
        k_fact = factorial(positions)
        n_minus_k_fact = factorial(length - positions)

        return n_fact / (k_fact * n_minus_k_fact)
    return 0


def get_total_combinations_with_repacement(length: int, positions: int) -> int:
    if (length > positions):
        n_plus_k_minus_one_fact = factorial(length + positions - 1)
        k_fact = factorial(positions)
        n_minus_one_fact = factorial(length - 1)

        return n_plus_k_minus_one_fact / (k_fact * n_minus_one_fact)
    return 0


def get_total_permutations(length: int, positions: int) -> int:
    if (length > positions):
        n_fact = factorial(length)
        n_minus_k_fact = factorial(length - positions)

        return n_fact / n_minus_k_fact
    return 0


def get_total_products(length: int, positions: int) -> int:
    if (length > 0) and (positions > 0):
        return length ** positions
    return 0


def combinations_of_2(iterable: list) -> list:
    ret_list = []

    for i in range(len(iterable)):
        for j in range(i, len(iterable)):
            L = [iterable[i]]
            if len(L) <= 2 and iterable[i] != iterable[j]:
                L.append(iterable[j])

            if len(L) > 1:
                ret_list.append((L))

    return ret_list


def combinations_with_replacement_of_2(iterable: list) -> list:
    ret_list = []

    for i in range(len(iterable)):
        for j in range(i, len(iterable)):
            L = [iterable[i]]
            if len(L) <= 2:
                L.append(iterable[j])

            ret_list.append((L))

    return ret_list
