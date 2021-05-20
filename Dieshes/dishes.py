with open('recipies.txt', encoding='UTF-8') as f:
    book = {}
    book.setdefault(f.readline().strip('\n'))
    print(book)
    count = int(f.readline())
    dish_list = []

    for i in range(1, (count + 1)):
        a = (f.readline().strip('\n').split('|'))
        a[1] = int(a[1])
        b = ('ingredient_name', 'quantity', 'measure')
        dish_list.append(dict(zip(b, a)))
    print(dish_list)


    # c = 0
    # for line in f:
    #     if line == '\n':
    #         c += 1
    # dish_quantity = c + 1
    # print(dish_quantity)



