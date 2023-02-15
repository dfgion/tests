from pprint import pprint
# Task 1

def filteration(list_of_dict: list):
    filter_list = []
    for element in list_of_dict:
        for v in element.values():
            if v[1] == 'Россия':
                filter_list.append(element)
    return filter_list

def unique_list(dict_of_ids: dict):
    result = set()
    for element in dict_of_ids.values():
        result.update(element)
    return result

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
def max_elem(dict_of_company: dict):
    max = {'start': 0}
    for element in dict_of_company.items():
        if element[1] > list(max.values())[0]:
            max = {element[0]: element[1]}
    return list(max.keys())[0]
