with open('recipies.txt', encoding='UTF-8') as file_work:
    cook_dict = {}
    for line in file_work:
        dish_name = line.strip('\n')
        counter = int(file_work.readline())
        list_of_ingridient = []
        for i in range(1, (counter + 1)):
            temp_dict = {}
            ingridient = file_work.readline().strip('\n').split('|')
            ingridient[1] = int(ingridient[1])
            keys = ('ingredient_name', 'quantity', 'measure')
            temp_dict.update(dict(zip(keys, ingridient)))
            list_of_ingridient.append(temp_dict)
        cook_dict[dish_name] = list_of_ingridient
        file_work.readline()


def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        for dish_name, recipe in cook_dict.items():
            if dish in dish_name:
                order_temp = {}
                for ingr in recipe:
                    order_temp.update({(ingr['ingredient_name']): {ingr['quantity']*person_count, ingr['measure']}})
                order.update(order_temp)
    print(order)

get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)

