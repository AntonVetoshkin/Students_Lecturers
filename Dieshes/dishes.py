with open('recipies.txt', encoding='UTF-8') as file_work:
    cook_book = {}
    for line in file_work:
        dish_name = line.strip('\n')
        counter = int(file_work.readline())
        list_of_ingridient = []
        for i in range(1, (counter + 1)):
            temp_dict = {}
            ingridient = file_work.readline().strip('\n').split('|')
            ingridient[1] = int(ingridient[1])
            keys = ('ingridient_name', 'quantity', 'measure')
            temp_dict.update(dict(zip(keys, ingridient)))
            list_of_ingridient.append(temp_dict)
        cook_book[dish_name] = list_of_ingridient
        file_work.readline()
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                new_shop_list_item = dict(ingridient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingridient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    for k, v in shop_list.items():
        del v['ingridient_name']

    print(shop_list)



# def get_shop_list_by_dishes(dishes, person_count):
#     order = {}
#     for dish in dishes:
#         for dish_name, recipe in cook_book.items():
#             if dish in dish_name:
#                 order_temp = {}
#                 for ingr in recipe:
#                     order_temp.update({(ingr['ingredient_name']): {ingr['quantity']*person_count, ingr['measure']}})
#                 order.update(order_temp)
#     print(order)    это был мой код

get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)
