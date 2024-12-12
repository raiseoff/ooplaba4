# Current Exchanger

## Описание
Это веб-приложение на Django для обмена валют, которое включает:
- Форму для конвертации валют.
- Таблицу с текущими курсами валют.
- REST API с JWT-аутентификацией для доступа к конвертации валют и получения списка валют.
- Модульные тесты для проверки функционала приложения.
- Использование [внешнего API](https://www.cbr-xml-daily.ru/daily_json.js) для получения списка валют. Загрузка моделей (currency/models.py) при запуске
- Использование конфигурации `.env` <br>
  Пример:
    ```env
    SECRET_KEY='django-insecure-_)_d&++qny!s$hd@q%#%ae)l=*4gjl+md6#kvob#y%isv5*rl6'
    ACCESS_TOKEN_LIFETIME=5000
    REFRESH_TOKEN_LIFETIME=10000
    ROTATE_REFRESH_TOKENS=0
    BLACKLIST_AFTER_ROTATION=0
    UPDATE_LAST_LOGIN=1
    ALGORITHM=HS256
    SIGNING_KEY=secret
    VERIFYING_KEY=None
    AUDIENCE=None
    ISSUER=None
    JWK_URL=None
    LEEWAY=0
    AUTH_HEADER_TYPES=Bearer
    AUTH_HEADER_NAME=HTTP_AUTHORIZATION
    USER_ID_FIELD=id
    USER_ID_CLAIM=user_id
    USER_AUTHENTICATION_RULE=rest_framework_simplejwt.authentication.default_user_authentication_rule
    AUTH_TOKEN_CLASSES=rest_framework_simplejwt.tokens.AccessToken
    TOKEN_TYPE_CLAIM=token_type
    JTI_CLAIM=jti
    SLIDING_TOKEN_REFRESH_EXP_CLAIM=refresh_exp
    SLIDING_TOKEN_LIFETIME=300
    SLIDING_TOKEN_REFRESH_LIFETIME=600
    EXTERNAL_API_METHOD=GET
    EXTERNAL_API_URL=https://www.cbr-xml-daily.ru/daily_json.js
    ```
---

## Основные возможности
1. **Авторизация и регистрация**:
   - Размещены по адресу `/auth/login/` и `/auth/register/`
     
     ![image](https://github.com/user-attachments/assets/3616a896-7e1f-4891-a065-ab0963c15230) ![image](https://github.com/user-attachments/assets/4be97e49-c2e8-4a88-80b9-ca19e8ee52e1)


3. **Форма конвертации валют**:

   ![image](https://github.com/user-attachments/assets/51322515-04e8-4454-a287-eb3d7369175c)

   - Размещена по адресу `/currency/exchange`.
   - Поля для заполнения:
     - **from**: валюта, из которой будет осуществляться конвертация ([CharCode](https://www.iban.com/currency-codes)).
     - **to**: валюта, в которую будет осуществляться конвертация ([CharCode](https://www.iban.com/currency-codes)).
     - **amount**: количество конвертируемой валюты.
   - Результат конвертации отображается после заполнения формы.

4. **Таблица с курсами валют**:
   - Размещена на странице `/currency/exchange`.
   - Отображает текущие курсы валют относительно рубля.

 ![image](https://github.com/user-attachments/assets/f2d040a4-d3bd-4751-a061-b65c894c1d43)

---

### API
1. **Аутентификация через [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)**:
   - Используется библиотека `rest_framework_simple_jwt`.
   - Эндпоинты для работы с токенами:
     - `/api/token/` — получение пары `access` и `refresh` токенов.
     - Пример запроса:
       
       ![image](https://github.com/user-attachments/assets/5138b67a-4fd9-4fc8-ba30-a03c71548578)

     - `/api/token/refresh/` — обновление `access` токена с помощью `refresh` токена.
     - Пример запроса:
       
       ![image](https://github.com/user-attachments/assets/a8853d77-4bff-4e72-b966-948380098eef)

     - `/api/token/verify/` — проверка валидности токена. Возращает ```{}```, если токен валидный.
     - Пример запроса:
       
       ![image](https://github.com/user-attachments/assets/b5933d02-2650-448a-971c-e3b78b61e42e)
       
2. **Эндпоинт `/api/currency/exchange`** (Требуется указание ```access``` токена в Headers:
   
   ![image](https://github.com/user-attachments/assets/2ea5ed17-6e90-4eb7-81c9-e7880d38a191)
   
   - Метод `GET`: возвращает список доступных валют.
     - Пример запроса:
       
      ![image](https://github.com/user-attachments/assets/f40573b1-cc4e-4b8a-9da9-a9ba5e8ac823)

       
   - Метод `POST`: выполняет конвертацию валют.
     - Требуемые поля в запросе:
       - `currencyFrom` (строка) — валюта-источник ([CharCode](https://www.iban.com/currency-codes)).
       - `currencyTo` (строка) — валюта-получатель ([CharCode](https://www.iban.com/currency-codes)).
       - `amount` (число) — сумма для конвертации.
     - Пример запроса:
       
        ![image](https://github.com/user-attachments/assets/e12aece0-4b78-45bd-b48e-8f9f1cf056b5)



---

## Установка

1. Установка зависимостей:

```bash
pip install -r requirements.txt
```
  - Использованные библиотеки:

    ```bash
    asgiref==3.8.1
    certifi==2024.8.30
    charset-normalizer==3.4.0
    Django==5.1.3
    django-cors-headers==4.6.0
    djangorestframework==3.15.2
    djangorestframework-simplejwt==5.3.1
    idna==3.10
    PyJWT==2.10.0
    python-dotenv==1.0.1
    requests==2.32.3
    sqlparse==0.5.2
    tzdata==2024.2
    urllib3==2.2.3
    ```

2. Применение миграций:

```bash
python manage.py migrate
```

3. Запуск сервера:

```bash
python manage.py runserver
```

---

## Тестирование
1. Приложение ***currency***:
   - Запуск:
      ```bash
     python .\manage.py test currency
      ```
   - Проверка создания модели валют.
   - Проверка Регистрации, входа и выхода пользователя.

2. Приложение ***api***:
   - Запуск:
     ```bash
     python .\manage.py test api
     ```
   - Проверка получения и обновления JWT токенов, проверка валидности токена
   - Проверка конвертации валют
