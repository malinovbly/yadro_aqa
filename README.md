# Автотесты для сервиса Push-console


## Содержание
- [Описание](#1-описание)
- [Структура проекта](#2-структура-проекта)
- [Установка и запуск тестов](#3-установка-и-запуск-тестов)
- [Отчет allure](#4-отчет-allure)


### 1. Описание

AQA проект по автоматизации тестирования сервиса ```Push-console```

Веб-клиенты:
- Адрес сервиса - http://193.169.128.91/login
- Документация API (Swagger) - http://193.169.128.91:3080/
- Логи (VictoriaMetrics) - http://193.169.128.91:9428/select/vmui/
- PostgreSQL (DBeaver) - http://193.169.128.91:11001/
- Redis (Redis Insight) - http://193.169.128.91:11002/
- RabbitMQ (RabbitMQ Management) - http://193.169.128.91:15672


### 2. Структура проекта

```
yadro_aqa/
├── fixtures/               # Фикстуры pytest
├── general/
    ├── checkers/           # Проверочные функции
    ├── clients/            # Клиенты БД
    ├── helpers/            # Вспомогательные функции
    ├── paths/              # Константы путей к REST эндпоинтам / UI урлам
    ├── request_wrappers/   # Обертки для gRPC и REST запросов
    └── utils.py            # Утилиты для генерации данных и др.
├── models/pydantic/
    ├── grpc/               # Pydantic-модели для валидации gRPC ответов
    └── rest/               # Pydantic-модели для валидации REST API ответов
├── pages/playwright/       # Реализация паттерна Page Object для UI-тестирования
├── proto_files/            # Прото-файл, сгенерированные python-клиенты на основе файла
├── routes/
    ├── grpc/               # Описание методов и маршрутов gRPC
    └── rest/               # Описание методов и эндпоинтов REST API
├── test_data/              # Тестовые данные
├── tests/
    ├── grpc/               # Тесты gRPC
    ├── rest/               # Тест REST API
    └── ui/playwright/      # Тесты UI (playwright)
├── .env.example            # Шаблон для переменных окружения (секреты, токены, URL)
├── config.json             # Статические параметры окружения и настройки клиентов
├── config.py               # Логика загрузки и парсинга config.json
└── TEST_CASES.md           # Документация тест-кейсов 
```


### 3. Установка и запуск тестов

Склонируйте репозиторий
```
git clone https://github.com/malinovbly/yadro_aqa.git
```

Перейдите в директорию проекта
```
cd yadro_aqa
```

Скопируйте файл .env.example под именем .env:
```
cp .env.example .env
```

Откройте файл .env и впишите в него данные своего пользователя
```
nano .env
```

Создайте Docker-образ
```
docker build -t aqa-final-project . 
```

Создайте и запустите контейнер
```
docker run --name tests --env-file .env aqa-final-project:latest
```


### 4. Отчет allure

Скопируйте директорию с результатами тестирования из контейнера
```
docker cp tests:/yadro_aqa/allure-results ./allure-results
```

Сгенерируйте временный HTML-отчет и откройте в браузере
```
allure serve allure-results
```
