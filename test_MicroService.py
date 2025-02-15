from api import MicroService
from settings import *

ms = MicroService()

def test_create_item_1(item_data=valid_item):
    """Позитивный тест на добавление нового объявления"""
    status, result = ms.create_item(item_data)
    assert status == 200
    assert 'Сохранили объявление' in result['status']

def test_get_item_by_id_2(item_id=valid_item_id):
    """Позитивный тест на запрос объявления по идентификатору"""
    status, result = ms.get_item_by_id(item_id)
    assert status == 200
    assert len(result) == 1
    assert result[0]['id'] == valid_item_id

def test_get_item_by_sellerid_3(seller_id=valid_seller):
    """Позитивный тест на запрос объявлений по идентификатору продавца"""
    status,result = ms.get_items_by_sellerid(seller_id)
    assert status == 200
    for elem in result:
        assert elem['sellerId'] == valid_seller

def test_statistic_by_id_4(item_id=valid_item_id):
    """Позитивный тест на запрос статистики объявления по идентификатору"""
    status,result = ms.get_statistic_by_id(item_id)
    assert status == 200
    assert all([len(result) == 1, "contacts" in result[0], "likes" in result[0], "viewCount" in result[0]])

def test_create_item_5(item_data=valid_item):
    """Позитивный тест с корректными данными тела запроса и числом с точкой в 'price'"""
    item_data['price'] = num_dot
    status, result = ms.create_item(item_data)
    assert status == 200
    assert 'Сохранили объявление' in result['status']

def test_create_item_6(item_data=valid_item):
    """Позитивный тест с корректными данными тела запроса и нулём в "price"""
    item_data['price'] = zero
    status, result = ms.create_item(item_data)
    assert status == 200
    assert 'Сохранили объявление' in result['status']

def test_create_item_7(item_data=valid_item):
    """Позитивный тест с нулём в "contacts" тела запроса"""
    item_data["statistics"]['contacts'] = zero
    status, result = ms.create_item(item_data)
    assert status == 200
    assert 'Сохранили объявление' in result['status']

def test_create_item_8(item_data=valid_item):
    """Позитивный тест с нулём в "like" тела запроса"""
    item_data["statistics"]['like'] = zero
    status, result = ms.create_item(item_data)
    assert status == 200
    assert 'Сохранили объявление' in result['status']

def test_create_item_9(item_data=valid_item):
    """Позитивный тест с нулём в "viewCount" тела запроса"""
    item_data["statistics"]['viewCount'] = zero
    status, result = ms.create_item(item_data)
    assert status == 200
    assert 'Сохранили объявление' in result['status']

def test_create_item_10(item_data=empty_body_item):
    """Негативный тест с пустым объектом JSON в теле запроса"""
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_get_item_by_id_11(item_id=invalid_item_id):
    """Негативный тест на запрос объявления с некорректным ID"""
    status,result = ms.get_item_by_id(item_id)
    assert status == 400
    assert 'передан некорректный идентификатор объявления' in result['message']

def test_create_item_12(item_data=valid_item):
    """Негативный тест с некорректным форматом (число вместо строки) "name" в теле запроса"""
    item_data['name'] = num
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_13(item_data=valid_item):
    """Негативный тест с некорректным форматом (число с точкой вместо строки) "name" в теле запроса"""
    item_data['name'] = num_dot
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_14(item_data=valid_item):
    """Негативный тест со спецсмволами в "name" тела запроса"""
    item_data['name'] = str_spec
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'недопустмые символы в имени' in result['status']

def test_create_item_15(item_data=valid_item):
    """Негативный тест с некорректным форматом (строка вместо числа) "price" в теле запроса"""
    item_data['price'] = string
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_16(item_data=valid_item):
    """Негативный тест с отрицательным числом в "price" тела запроса"""
    item_data['price'] = num_negative
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_17(item_data=valid_item):
    """Негативный тест с некорректным форматом (строка вместо числа) "sellerId" в теле запроса"""
    item_data['sellerId'] = string
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_18(item_data=valid_item):
    """Негативный тест с некорректным форматом (число с точкой вместо числа) "sellerId" в теле запроса"""
    item_data['sellerId'] = num_dot
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_19(item_data=valid_item):
    """Негативный тест с нулём в "sellerId" тела запроса"""
    item_data['sellerId'] = zero
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_20(item_data=valid_item):
    """Негативный тест с отрицательным числом в "sellerId" тела запроса"""
    item_data['sellerId'] = num_negative
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_21(item_data=valid_item):
    """Негативный тест с некорректным форматом (строка вместо числа) "contacts" в теле запроса"""
    item_data["statistics"]['contacts'] = string
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_22(item_data=valid_item):
    """Негативный тест с некорректным форматом (число с точкой вместо числа) "contacts" в теле запроса"""
    item_data["statistics"]['contacts'] = num_dot
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_23(item_data=valid_item):
    """Негативный тест с отрицательным числом в  "contacts" тела запроса"""
    item_data["statistics"]['contacts'] = num_negative
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_24(item_data=valid_item):
    """Негативный тест с некорректным форматом (строка вместо числа) "like" в теле запроса"""
    item_data["statistics"]['like'] = string
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_25(item_data=valid_item):
    """Негативный тест с некорректным форматом (число с точкой вместо числа) "like" в теле запроса"""
    item_data["statistics"]['like'] = num_dot
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_26(item_data=valid_item):
    """Негативный тест с отрицательным числом в "like" тела запроса"""
    item_data["statistics"]['like'] = num_negative
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_27(item_data=valid_item):
    """Негативный тест с некорректным форматом (строка вместо числа) "viewCount"" в теле запроса"""
    item_data["statistics"]['viewCount'] = string
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_28(item_data=valid_item):
    """Негативный тест с некорректным форматом (число с точкой вместо числа) "viewCount" в теле запроса"""
    item_data["statistics"]['viewCount'] = num_dot
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']

def test_create_item_29(item_data=valid_item):
    """Негативный тест с отрицательным числом в "viewCount" тела запроса"""
    item_data["statistics"]['viewCount'] = num_negative
    status, result = ms.create_item(item_data)
    assert status == 400
    assert 'не передано тело объявления' in result['status']