def n_gram(sen_lst: list, n: int) -> list:
    return list(zip(*[sen_lst[i:] for i in range(n)]))

print(n_gram('I am an NLPer'.split(' '), 2))
print(n_gram(list('I am an NLPer'), 2))
