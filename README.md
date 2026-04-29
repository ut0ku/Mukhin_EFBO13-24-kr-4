<img width="711" height="432" alt="image_2026-04-28_17-36-12" src="https://github.com/user-attachments/assets/7e08ba54-370a-46cb-8ffe-b3c765c45284" />Задание 9.1
Была применена первоначальная миграция к базе данных, таблица Product вместе с полями "id", "title", "price" и "count" успешно создалась
<img width="413" height="65" alt="image_2026-04-28_17-04-21" src="https://github.com/user-attachments/assets/a0f559be-c43d-4874-94aa-7620f81ff9ef" />

Добавлены две записи в таблицу
<img width="423" height="95" alt="image_2026-04-28_17-06-12" src="https://github.com/user-attachments/assets/7b5bdc3a-f127-4f72-b9d1-8160779a2282" />

Добавлено новое поле "description" (not null) к сущности "Product", сгенерирован новый сценарий миграции через Alembic, применена новая миграция к базе данных
<img width="486" height="93" alt="image_2026-04-28_17-11-45" src="https://github.com/user-attachments/assets/3977ded0-8574-40b7-b6b1-9720d33d45e3" />

Задание 10.1
Создано приложение FastAPI, настроены пользовательские классы исключений (CustomExceptionA, CustomExceptionB), Зарегистрированы пользовательские обработчики исключений, определены модели реагирования на ошибки (Pydantic), созданы две конечные точки API

Тест (GET) /trigger-a (status 400)
<img width="712" height="437" alt="image_2026-04-28_17-36-11" src="https://github.com/user-attachments/assets/c02abc1d-72e5-49d6-894f-e908718244ad" />

Тест успешного (GET) /trigger-a (status 200)
<img width="710" height="431" alt="image_2026-04-28_17-36-11 (2)" src="https://github.com/user-attachments/assets/227eecc5-c144-46c9-a95a-60c4976d5817" />

Тест (GET) /trigger-b/{item_id} (status 404)
<img width="709" height="441" alt="image_2026-04-28_17-36-11 (3)" src="https://github.com/user-attachments/assets/541c01c5-04e8-4cb8-bb82-c62b3fa6415c" />

Тест успешного (GET) /trigger-b/{item_id} (status 200)
<img width="711" height="432" alt="image_2026-04-28_17-36-12" src="https://github.com/user-attachments/assets/102b2c6b-b9af-43f3-a1dc-a79e088add34" />

Задание 10.2
Создано FastAPI-приложение с моделью Pydantic User, обеспечивающей строгую валидацию входящих данных (возраст, email, пароль).

Тест (POST) /users с корректными данными (status 200)
<img width="712" height="356" alt="image_2026-04-29_09-56-58" src="https://github.com/user-attachments/assets/fb2c9f8f-da82-464b-80d0-f37a7caad242" />
<img width="710" height="403" alt="image_2026-04-29_09-56-58 (2)" src="https://github.com/user-attachments/assets/e413c09e-cc2e-4194-90ba-50a07b4bdc47" />

Тест (POST) /users с вводом неверного age (<19) (status 422)
<img width="711" height="350" alt="image_2026-04-29_09-59-17" src="https://github.com/user-attachments/assets/66fc48cb-1bbc-4dbc-8603-19674c03df64" />
<img width="710" height="343" alt="image_2026-04-29_09-59-17 (2)" src="https://github.com/user-attachments/assets/3e172081-da1f-4b9b-b35e-6b1266011eeb" />

Тест (POST) /users с вводом неверного email (status 422)
<img width="709" height="349" alt="image_2026-04-29_10-00-51" src="https://github.com/user-attachments/assets/7d8d6399-5df9-4d08-b4e6-feccf2e4b003" />
<img width="711" height="383" alt="image_2026-04-29_10-00-51 (2)" src="https://github.com/user-attachments/assets/7b9d9901-ca26-4f6a-b0ea-1902080da7cf" />

Тест (POST) /users с вводом короткого пароля (status 422)
<img width="710" height="350" alt="image_2026-04-29_10-03-38" src="https://github.com/user-attachments/assets/b3d985e2-51c0-4fe6-82fc-e7d1e0ca2d4c" />
<img width="709" height="348" alt="image_2026-04-29_10-03-38 (2)" src="https://github.com/user-attachments/assets/36e79d5e-bb91-410e-9784-88be05364a9b" />

Тест (POST) /users с вводом слишком длинного пароля (status 422)
<img width="709" height="350" alt="image_2026-04-29_10-05-19" src="https://github.com/user-attachments/assets/88f5bc6f-7899-4478-a73b-b67691ab1314" />
<img width="710" height="347" alt="image_2026-04-29_10-05-19 (2)" src="https://github.com/user-attachments/assets/7ff1c857-4dc9-4866-ac71-d29d49952618" />

Тест (POST) /users с отсутствием обязательного поля возраста (status 422)
<img width="711" height="350" alt="image_2026-04-29_10-08-15" src="https://github.com/user-attachments/assets/b9cad763-97e4-4624-8e60-67cafaf2b488" />
<img width="709" height="340" alt="image_2026-04-29_10-08-15 (2)" src="https://github.com/user-attachments/assets/891e8259-c82b-468a-8d39-cccad162ffe6" />

Задание 11.1
Настроено приложение FastAPI с тремя конечными точками API
<img width="718" height="83" alt="image_2026-04-29_10-21-42" src="https://github.com/user-attachments/assets/7cad749d-bcec-42fb-9b48-d5136f161cd8" />

Написано 9 модульных тестов:
POST /users
1. test_create_user_success (успешное создание с валидными данными).
2. test_create_user_age_too_low (ошибка валидации: age <= 18).
3. test_create_user_invalid_email (ошибка валидации: некорректный email).
4. test_create_user_password_too_short (ошибка валидации: пароль < 8 символов).
5. test_create_user_password_too_long (ошибка валидации: пароль > 16 символов).
Get /users/{user_id}
6. test_get_user_success (успешное получение существующего пользователя).
7. test_get_user_not_found (ошибка 404: пользователь не найден).
DELETE /users/{user_id}
8. test_delete_user_success (успешное удаление и проверка, что он исчез).
9. test_delete_user_not_found (ошибка 404: пользователь не найден).
<img width="520" height="253" alt="image_2026-04-29_10-46-02" src="https://github.com/user-attachments/assets/7364bfaf-4e4a-4ad3-bff5-243408a6692d" />

Задание 11.2
Подготовлено окружение, установлены все необходимы зависимости, написаны асинхронные тесты для всех 3х эндпоинтов, сгенерированы данные через Faker, обеспечено чистое состояние между тестами.

Написано 9 асинхронных тестов:
POST /users
1. test_create_user (Тест успешного создания пользователя)
2. test_create_user_age_too_low (Тест валидации возраста)
3. test_create_user_invalid_email (Тест валидации email)
4. test_create_user_password_too_short (Тест ошибки валидации: пароль < 8 символов).
5. test_create_user_password_too_long (Тест валидации: пароль > 16 символов).
Get /users/{user_id}
6. test_get_user_success (Тест успешного получения существующего пользователя)
7. test_get_user_not_found (Тест получения несуществующего пользователя)
DELETE /users/{user_id}
8. test_delete_user_success (Тест успешного удаления пользователя)
9. test_delete_user_not_found (Тест удаления несуществующего пользователя)
<img width="510" height="202" alt="image_2026-04-29_11-30-34" src="https://github.com/user-attachments/assets/3ec23ad6-fe08-413f-b837-9a1db3024bf2" />

Установка зависимостей:
pip install fastapi uvicorn[standard] pydantic httpx pytest pytest-asyncio faker

Запуск приложения:
uvicorn main:app --reload

Команды для тестирования ключевых сценариев:

Синхронные тесты (test_main.py):
pytest test_main.py -v

Асинхронные тесты (test_main_async.py):
pytest test_main_async.py -v --asyncio-mode=auto
