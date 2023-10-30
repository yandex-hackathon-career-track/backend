GOOD_PROFILE = {
    "name": "АО Компания",
    "about": "Мы лучшие",
    "website": "https://www.company.com",
    "phone": "+7 911 9876543",
    "email": "company@thecompany.com",
    "activity": "Делаем все в IT",
    "foundation_year": 2020,
}

EMPLOYER_CREATE_VALID_DATA = (
    (
        {
            "email": "test_client_01@unexistingmail.ru",
            "password": "neverinmylife-123",
        },
        "пользователь-работодатель без роли (по умолчанию)",
    ),
    (
        {
            "email": "test_client_02@unexistingmail.ru",
            "password": "neverinmylife-123",
        },
        "пользователь с роль Работодатель",
    ),
    (
        {
            "email": "test_client_03@unexistingmail.ru",
            "password": "neverinmylife-123",
            "role": "admin",
        },
        "пользователь с ролью Админ",
    ),
    (
        {
            "email": "test_client_04@unexistingmail.ru",
            "password": "neverinmylife-123",
            "role": "applicant",
        },
        "пользователь с ролью Соискатель",
    ),
)

EMPLOYER_CREATE_INVALID_DATA = (
    (
        {
            "password": "neverinmylife-123",
        },
        "нет email",
    ),
    (
        {
            "email": "test_client_05@unexistingmail.ru",
        },
        "нет пароля",
    ),
    (
        {
            "email": "test_client_05@unexistingmail.ru",
            "password": "1234567",
            "first_name": "Mr. Client",
        },
        "пароль не проходит валидацию",
    ),
    (
        {
            "email": "employer@unexisting_mail.ru",
            "password": "neverinmylife-123",
        },
        "существующий пользователь",
    ),
)


EMPLOYER_EDIT_VALID_DATA = (
    (
        {
            "name": "Название",
            "about": "Много слов о компании",
            "website": "https://www.test.com",
            "phone": "+79111234567",
            "email": "test@newmail.com",
            "activity": "Тест",
            # 'employees_number': 1,
            "foundation_year": 2000,
        },
        "all fields",
    ),
    (
        {
            "name": "Название",
            "about": "Много слов о компании",
        },
        "name & about",
    ),
    (
        {
            "website": "https://www.test.com",
            "phone": "+79111234567",
            "email": "test@newmail.com",
        },
        "site & phone & email",
    ),
    (
        {
            "activity": "Тест",
            "foundation_year": 2000,
        },
        "activity & foundation year",
    ),
)


EMPLOYER_EDIT_INVALID_DATA = (
    (
        {
            "name": "a" * 120,
        },
        "Слишком длинное имя",
    ),
    (
        {
            "website": "test.com",
        },
        "Ссылка на сайт без http",
    ),
    (
        {
            "phone": "9" * 30,
        },
        "Слишком длинный телефон",
    ),
    (
        {
            "email": "test",
        },
        "Неверный формат email",
    ),
    (
        {
            "foundation_year": "2000 год",
        },
        "Неверный формат года",
    ),
    (
        {
            "foundation_year": 2025,
        },
        "Год из будущего",
    ),
    (
        {
            "foundation_year": 1850,
        },
        "Год до 1900",
    ),
)
