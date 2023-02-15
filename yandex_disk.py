import requests
from unittest import TestCase 
import pytest

class Manager_Yandex():
    def __init__(self, name_path):    
        self.token = 'y0_AgAAAABjrMcYAAkkSwAAAADcSrglPMZCEarAQlWoi5JCZEdPqU8Uhws'
        self.headers = {
            'Content-Type': 'Application/json',
            'Authorization': f'OAuth {self.token}'}
        self.name_path = name_path

    def create_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url=url, params={'path': '{}'.format(self.name_path)}, headers=self.headers)
        return response.status_code
    
    def get_name(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.get(url=url, params={'path': '{}'.format(self.name_path)}, headers=self.headers)
        return response.json()['name']

ya = Manager_Yandex(name_path='WRITE FOLDER"S NAME HERE') # Тест создание папки 
def test_folder():
    assert ya.create_folder() == 201

@pytest.mark.parametrize( # Тесты с ошибкой. Случайные название папок, которых нет на диске. Можно поменять на свои имена
        'name', [('jwfjwfwk'),
                 ('Something yet'),
                 ('DB'),
                 ('LFWLFWLll')] 
) 
def test_availability(name): # Тест на наличие папки с заданным именем на диске
    assert ya.get_name() == name