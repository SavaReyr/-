import shutil
from pathlib import Path
import os
dishes_name = {}
firt_list = []
def cook_book_def(fil):
    with open(fil, encoding = "UTF-8") as file1:
        for line in file1:
            if line.isspace() is True:
                LIST = file1.readline()
                dishes_name[LIST.rstrip()]= []
    with open(fil, encoding='utf-8') as f:
        for line in f:
            firt_list.append(line.rstrip('\n'))
    for num1, num2 in enumerate(firt_list):
        if num2.isdigit():
            for food in firt_list[num1+1:num1+int(num2)+1]:
                ingredient_name = food.split(' | ')[0]
                quantity = int(food.split(' | ')[1])
                measure = food.split(' | ')[2]
                dishes_name[firt_list[num1-1]].append({'ingredient_name':ingredient_name,'quantity':quantity,'measure':measure})

    return dishes_name
def get_shop_list_by_dishes(dishes, person_count, name_of_file):
    this_dict = {}
    if type(dishes) == type(["3", "4"]):
        for dish in dishes:
            for cook_book_key in cook_book_def(name_of_file).keys():
                if dish == cook_book_key:
                    for new_dict in  cook_book_def(name_of_file)[cook_book_key]:
                        #print(new_dict)
                        #print(new_dict["ingredient_name"], new_dict["quantity"], new_dict["measure"])
                        this_dict[new_dict["ingredient_name"]] = {"measure":new_dict["measure"], "quantity":new_dict["quantity"]*person_count}
        print(this_dict)
    if type(dishes) != type(["3", "4"]):
        for cook_book_key in cook_book_def(name_of_file).keys():
            if dishes == cook_book_key:
                for new_dict in dishes_name[cook_book_key]:
                    this_dict[new_dict["ingredient_name"]] = {"measure":new_dict["measure"], "quantity":new_dict["quantity"]*person_count}
        print(this_dict)
print(cook_book_def("pyy.txt"))
get_shop_list_by_dishes("Омлет", 5, "pyy.txt")
def unification(first_file, second_file, new_file):
    with open(first_file, encoding = "UTF-8") as file1:
        first = file1.read()
        count = 0
        file1.seek(0)
        for num in file1:
            count += 1

    with open(second_file, encoding="UTF-8") as file2:
        second = file2.read()
        count_2 = 0
        file2.seek(0)
        for num1 in file2:
            count_2 += 1

    with open(new_file, "w", encoding="UTF-8") as file3:
        if count < count_2:
            file3.write(first_file)
            file3.write(f'\n{str(count)}')
            file3.write(f'\n{first}')

            file3.write(f'\n{second_file}')
            file3.write(f'\n{str(count_2)}')
            file3.write(f'\n{second}')
        else:
            file3.write(second_file)
            file3.write(f'\n{str(count_2)}')
            file3.write(f'\n{second}')

            file3.write(f'\n{first_file}')
            file3.write(f'\n{str(count)}')
            file3.write(f'\n{first}')







unification("text_for_py1.txt", "text_for_py2.txt", "Empty_file_for_py.txt")
