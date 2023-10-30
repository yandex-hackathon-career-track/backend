# ID статуса "Не выбран" для откликов и отборов резюме.
UNCHOSEN_STATUS_ID = 1
# ID статуса "На рассмотрении" для откликов и отборов резюме.
UNDER_REVIEW_STATUS_ID = 2
# ID статуса "Отправлено тестовое" для откликов и отборов резюме.
SENT_TEST_STATUS_ID = 3
# ID статуса "Собеседование" для откликов и отборов резюме.
INTERVIEW_STATUS_ID = 4
# ID статуса "Не выбран" для откликов и отборов резюме.
REFUSAL_STATUS_ID = 5
# Список ID "Отобранных" резюме
CHOSEN_STATUS_IDS = [
    UNDER_REVIEW_STATUS_ID,
    SENT_TEST_STATUS_ID,
    INTERVIEW_STATUS_ID,
]
# Минимальный год основания компании
MIN_FOUNDATION_YEAR = 1900
# Допустимые типы файлов
ACCEPTABLE_FILES = [
    "png",
    "pdf",
    "jpeg",
    "jpg",
    "msword",
    "docx",
    "vnd.openxmlformats-officedocument.wordprocessingml.document",
]
# Макс.размер файла - 10 мегабайт
FILE_SIZE_LIMIT = 10485760
