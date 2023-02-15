from unittest import TestCase 
from main import filteration, unique_list, max_elem


# Task 1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
    ]

class test_filteration(TestCase):
    def test_correct(self):
        res = filteration(geo_logs)
        self.assertEqual(res, [{'visit1': ['Москва', 'Россия']}, 
                               {'visit3': ['Владимир', 'Россия']}, 
                               {'visit7': ['Тула', 'Россия']}, 
                               {'visit8': ['Тула', 'Россия']}, 
                               {'visit9': ['Курск', 'Россия']}, 
                               {'visit10': ['Архангельск', 'Россия']}])
        
    def test_list(self):
        res = filteration(geo_logs)
        self.assertIsInstance(res, list)

# Task 2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

class test_unique(TestCase):
    def test_unique(self):
        check = set(sum(ids.values(), []))
        res = unique_list(ids)
        self.assertEqual(res, check)

    def test_list(self):
        res = unique_list(ids)
        self.assertNotIsInstance(res, dict)

# Task 4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

class test_max(TestCase):
    def test_max_company(self):
        check = max(stats, key=stats.get)
        res = max_elem(stats)
        self.assertEqual(res, check)
    
    def test_str(self):
        res = max_elem(stats)
        self.assertIsInstance(res, str)

