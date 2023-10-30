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


CLIENT_UPDATE_VALID_DATA = (
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientov",
            "birthday": "12.09.1970",
        },
        "добавлен аватар",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientov",
            "birthday": "12.09.1970",
        },
        "добавлена фамилия",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientovich",
            "birthday": "12.09.1970",
            "phone_number": "+79119876543",
        },
        "добавлена фамилия и телефон",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientovich",
            "birthday": "12.09.1970",
            "phone_number": "+79119876543",
        },
        "добавлена фамилия, телефон и пол",
    ),
)


CLIENT_UPDATE_INVALID_DATA = (
    (
        {
            "first_name": "Mr. Client" * 20,
            "last_name": "Clientov",
            "birthday": "12.09.1970",
        },
        "слишком длинное имя",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientov" * 20,
            "birthday": "12.09.1970",
        },
        "слишком длинная фамилия",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientov",
            "birthday": "1970-09-12",
        },
        "неверный формат даты рождения",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientovich",
            "birthday": "12.09.1970",
            "phone_number": "+791198765432131515864864",
        },
        "слишком длинный номер телефона",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientov",
            "birthday": "12.09.1970",
            "avatar": "R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
        },
        "неверный формат картинки 1",
    ),
    (
        {
            "first_name": "Mr. Client",
            "last_name": "Clientov",
            "birthday": "12.09.1970",
            "avatar": "http://fakesite.com/fakesite",
        },
        "неверный формат картинки 2",
    ),
)
