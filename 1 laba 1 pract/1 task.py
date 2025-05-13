j = input("Введите символы, входящие в список драгоценностей: ")
S = input("Введите символы, входящие в список камней: ")

jewels = set(j)
stones = list(S)

count = 0
for i in stones:
    if i in jewels:
        count += 1

print("Количество драгоценностей в камнях: ", count)