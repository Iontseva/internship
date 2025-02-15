import requests
import json
class MicroService:
    def __init__(self):
        self.base_url = "https://qa-internship.avito.com"
    def create_item(self, item_data):
        """Метод делает запрос к API сервера, добавляет на сервер информацию о новом объявлении и возвращает статус
        запроса и результат в формате JSON с сообщением о сохранении объявления и уникальным идентификатором"""
        headers = {'Content-Type': 'application/json'}
        res = requests.post(f'{self.base_url}/api/1/item', headers=headers, data=json.dumps(item_data))
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def get_item_by_id(self, item_id):
        """Метод делает запрос к API сервера с идертификатором объявления и возвращает статус запроса и результат
        в формате JSON с списком данных объявления"""
        res = requests.get(f'{self.base_url}/api/1/item/{item_id}')
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def get_items_by_sellerid(self, seller_id):
        """Метод делает запрос к API сервера с идертификатором продавца и возвращает статус запроса и результат
        в формате JSON с списком данных всех объявлений продавца"""
        res = requests.get(f'{self.base_url}/api/1/{seller_id}/item')
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def get_statistic_by_id(self, item_id):
        """Метод делает запрос к API сервера с идертификатором объявления и возвращает статус запроса и результат
        в формате JSON со статистикой объявления"""
        res = requests.get(f'{self.base_url}/api/1/statistic/{item_id}')
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    
