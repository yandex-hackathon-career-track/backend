# YANDEX HACKATHON: Внутренний сервис для найма в Карьерном трекере
http://130.193.38.88/

##  Описание BACKEND. 
### Инструменты:
![image](https://img.shields.io/badge/Python%203.11-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django%204.2-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest%203.14-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![image](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![image](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)

### Доступ в админ-панель:
http://130.193.38.88/admin 
```
login: admin@admin.ru
password: password-123
```

### API-документация:
http://130.193.38.88/api/schema/swagger/#/

### Описание возможностей
| Метод  | Endpoint                                     | Назначение                                                               |
|:-------|----------------------------------------------|--------------------------------------------------------------------------|
| GET    |/api/v1/applicants/                           | Список соискателей с возможностью фильтрации по атрибутам |
| GET    |/api/v1/applicants/{id}/                      | Подробная карточка соискателя  |
| POST   |/api/v1/applicants/{id}/selected/             | Добавление соискателя в избранное  |
| DELETE |/api/v1/applicants/{id}/selected/             | Удаление соискателя из избранного  |
| GET    |/api/v1/applicants/download_report/           | Скачивание отчета в excel  |
| GET    |/api/v1/attributes/                           | Полный список словарей моделей-атрибутов  |
| POST   |/api/v1/auth/jwt/create/                      | Получение нового JWT-токена |
| POST   |/api/v1/auth/jwt/refresh/                     | Обновление JWT-токена |
| POST   |/api/v1/auth/jwt/verify/                      | Верификация JWT-токена |
| GET    |/api/v1/employers/me/                         | Чтение профиля работодателя (личный кабинет)  |
| PATCH  |/api/v1/employers/me/                         | Изменение профиля работодателя (личный кабинет) |
| GET    |/api/v1/employers/vacancies/                  | Получение списка вакансий работодателя (текущего пользователя). Доступна фильтрация (опубликованные/архив) |
| POST   |/api/v1/employers/vacancies/                  | Создание новой вакансии |
| GET    |/api/v1/employers/vacancies/{id}/             | Карточка вакансии для работодателя |
| PATCH  |/api/v1/employers/vacancies/{id}/             | Редактирование вакансии |
| GET    |/api/v1/employers/vacancies/{id}/responds/    | Просмотр списка откликов на вакансию со статистикой |
| PATCH  |/api/v1/employers/vacancies/{id}/responds/    | Изменение статуса отклика |
| POST   |/api/v1/users/                                | Создание пользователя (+ создается профиль) |
| GET    |/api/v1/users/me/                             | Просмотр данных о пользователе (id/email/роль) |
| POST   |/api/v1/users/reset_password/                 | Сброс пароля |
| POST   |/api/v1/users/reset_password_confirm/         | Установка нового пароля после сброса |
| POST   |/api/v1/users/set_password/                   | Установка нового пароля в личном кабинете |
| GET    |/api/v1/vacancies/                            | Просмотр списка вакансий (для Соискателей) |
| GET    |/api/v1/vacancies/{id}/                       | Карточка вакансии (для Соискателей)  |
| POST   |/api/v1/vacancies/{id}/respond/               | Откликнуться на вакансию (для Соискателей) |


### Запуск проекта
## Переменные окружения
Файл .env хранится в корневой папке проекта; пример заполнения в .env.example.

## Запуск с установленным Docker
Копировать проект в папку целиком (для запуска контейнеров достаточно .env в корне проекта и папки /infra)
```
git clone git@github.com:yandex-hackathon-career-track/backend.git
```
Перейти в папку infra и запустить сборку контейнеров
```
cd backend/infra
docker compose up -d
```
Добавить миграции и собрать статику
```
docker exec -it career_back python manage.py migrate
docker exec -it career_back python manage.py collectstatic --noinput
```
Сайт доступен по адресу http://127.0.0.1/

## Наполнение проекта фикстурами
Добавить модели атрибутов (статичные модели для фильтров и атрибутов соискателей)
```
docker exec -it career_back python manage.py add_attributes
```

### Разработчики:
[Руслан Атаров](https://github.com/ratarov) <br>
[Филипп Пыхонин](https://github.com/caveinfix)