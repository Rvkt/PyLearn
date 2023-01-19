list = ['abc', 'aba', '1919', 'ava']

[print(i) for i in list if len(i) > 1 and i[0] == i[-1]]