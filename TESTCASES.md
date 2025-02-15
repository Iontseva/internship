# Вызов API
### Позитивные тесты
#### 1. Базовый позитивный тест с корректными данными тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с корректными данными объявления
```
{
            "name": "Телефон",
            "price": 85566,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с уникальным номером объявления: строка
```
{
    "status": "Сохранили объявление - 3078426e-7bfd-45dc-a6c8-7d8a5fe19320"
}
```

#### 2. Базовый позитивный тест на запрос объявления с корректным ID
- тип запроса: GET
- url:https://qa-internship.avito.com/api/1/item/:id
- :id: валидный номер объявления
```
 6f146a23-41b6-414b-836a-a7c1b1968682          
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с данными объявления и id из запроса
```
[
    {
        "createdAt": "2025-02-13 21:22:38.596412 +0300 +0300",
        "id": "3078426e-7bfd-45dc-a6c8-7d8a5fe19320",
        "name": "dsdsd",
        "price": 0,
        "sellerId": 258369,
        "statistics": {
            "contacts": 32,
            "likes": 0,
            "viewCount": 14
        }
    }
]
```

#### 3. Базовый позитивный тест на запрос объявлений с валидным ID продавца
- тип запроса: GET
- url: https://qa-internship.avito.com/api/1/:sellerID/item
- :sellerID: валидный номер продавца
```
 3452          
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с данными объявлений. А каждом объявлении sellerId совпадает с запросом
```
[
    {
        "createdAt": "2025-02-13 21:22:38.596412 +0300 +0300",
        "id": "3078426e-7bfd-45dc-a6c8-7d8a5fe19320",
        "name": "dsdsd",
        "price": 0,
        "sellerId": 3452,
        "statistics": {
            "contacts": 32,
            "likes": 0,
            "viewCount": 14
        }
    }
]
```

#### 4. Базовый тест на запрос объявления стасистики объявлений с корректным ID
- тип запроса: GET
- url:https://qa-internship.avito.com/api/1/statistic/:id
- :id: валидный номер объявления
```
 6f146a23-41b6-414b-836a-a7c1b1968682          
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с данными статистики объявления 
```
[
    {
        "contacts": 32,
        "likes": 0,
        "viewCount": 14
    }
]
```

#### 5. Позитивный тест с корректными данными тела запроса и числом с точкой в "price"
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с корректными данными объявления b числом с точкой "price"
```
{
            "name": "Телефон",
            "price": 85566.5,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с уникальным номером объявления: строка
```
{
    "status": "Сохранили объявление - 3078426e-7bfd-45dc-a6c8-7d8a5fe19320"
}
```

#### 6. Позитивный тест с корректными данными тела запроса и нулём в "price"
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с корректными данными объявления и нулём в "price"
```
{
            "name": "Телефон",
            "price": 0,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с уникальным номером объявления: строка
```
{
    "status": "Сохранили объявление - 3078426e-7bfd-45dc-a6c8-7d8a5fe19320"
}
```
#### 7. Позитивный тест с нулём в "contacts" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с нулём в "contacts"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 0,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с уникальным номером объявления: строка
```
{
    "status": "Сохранили объявление - 3078426e-7bfd-45dc-a6c8-7d8a5fe19320"
}
```
#### 8. Позитивный тест с нулём в "like" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с нулём в "like"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 35,
                "like": 0,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с уникальным номером объявления: строка
```
{
    "status": "Сохранили объявление - 3078426e-7bfd-45dc-a6c8-7d8a5fe19320"
}
```
#### 9. Позитивный тест с нулём в "viewCount" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с нулём в "viewCount"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 35,
                "like": 14,
                "viewCount": 0
            }
        }
```
Результаты выполнения запроса:
- Status: 200(OK)
- Body: JSON с уникальным номером объявления: строка
```
{
    "status": "Сохранили объявление - 3078426e-7bfd-45dc-a6c8-7d8a5fe19320"
}
```

### Негативные тесты
#### 10. Негативный тест с пустым объектом JSON в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с пустым объектом
```
{ }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```
#### 11.Негативный тест на запрос объявления с некорректным ID
- тип запроса: GET
- url:https://qa-internship.avito.com/api/1/item/:id
- headers = {'Content-Type': 'application/json'}
- :id: некорректный номер объявления
```
 6f146a23          
```
Результаты выполнения запроса:
- Status:  400 (Bad Request)
- Body: JSON с сообщением "передан некорректный идентификатор объявления"
```
{
    "result": {
        "message": "передан некорректный идентификатор объявления",
        "messages": {}
    },
    "status": "400"
}
```

#### 12. Негативный тест с некорректным форматом (число вместо строки) "name" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом в "name"
```
{
            "name": 9999999999,
            "price": 3365,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 13. Негативный тест с некорректным форматом (чило с точкой вместо строки) "name" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с точкой в "name"
```
{
            "name": 36.5,
            "price": 3365,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```
#### 14. Негативный тест со спецсмволами в "name" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json со спецсмволами в "name" тела запроса
```
{
            "name": "№%&#@",
            "price": 3365,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "недопустмые символы в имени"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "недопустмые символы в имени"
}
```

#### 15. Негативный тест с некорректным форматом (строка вместо числа) "price" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json со строкой в "price"
```
{
            "name": "Имя,
            "price": "Цена",
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```
#### 16. Негативный тест с отрицательным числом в "price" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с отрицательным числом в "price"
```
{
            "name": "Имя,
            "price": -95,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```
#### 17. Негативный тест с некорректным форматом (строка вместо числа) "sellerId" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json со строкой в "sellerId"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": "258369",
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 18. Негативный тест с некорректным форматом (число с точкой вместо числа) "sellerId" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с точкой в "sellerId"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369.5,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 19. Негативный тест с нулём в "sellerId" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с нулём в "sellerId"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 0,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 20. Негативный тест с отрицательным числом в "sellerId" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с отрицательным числом в "sellerId"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": -953655,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```
#### 21. Негативный тест с некорректным форматом (строка вместо числа) "contacts" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json со строкой в "contacts"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": "32",
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 22. Негативный тест с некорректным форматом (число с точкой вместо числа) "contacts" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с точкой в "contacts"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32.5,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 23. Негативный тест с отрицательным числом в  "contacts" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с отрицательным числом в  "contacts" тела "contacts"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": -32,
                "like": 35,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 24. Негативный тест с некорректным форматом (строка вместо числа) "like" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json со строкой в "like"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": "35",
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 25. Негативный тест с некорректным форматом (число с точкой вместо числа) "like" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с точкой в "like"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35.4,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 26. Негативный тест с отрицательным числом в "like" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с отрицательным числом в "like"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": -535,
                "viewCount": 14
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```


#### 27. Негативный тест с некорректным форматом (строка вместо числа) "viewCount"" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json со строкой в "viewCount"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": "14"
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 28. Негативный тест с некорректным форматом (число с точкой вместо числа) "viewCount" в теле запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с точкой в "like"
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": 14.6
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```

#### 29. Негативный тест с отрицательным числом в "viewCount" тела запроса
- тип запроса: POST
- url: https://qa-internship.avito.com/api/1/item
- headers = {'Content-Type': 'application/json'}
- body: json с числом с отрицательным числом в "viewCount" 
```
{
            "name": "Имя,
            "price": 3600,
            "sellerId": 258369,
            "statistics": {
                "contacts": 32,
                "like": 35,
                "viewCount": -146
            }
        }
```
Результаты выполнения запроса:
- Status: 400 (Bad Request)
- Body: JSON с сообщением "не передано тело объявления"
```
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"
}
```
