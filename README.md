# skychimp
Описание проекта

    Проект представляет из себя интерфейс для управления рассылками.
    В проекте используется библиотека  django-crontab, для работы с регулярными задачами. Поэтому важно:
        Работать с проектом либо используя Linux.
        Установить все зависимости проекта.
        Установить настройки, указанные в env.sample
        Убедиться, что механизм cron запущен - python manage.py crontab show, python manage.py crontab add, при необходимости.

Запуск проэкта из терминала:
        python manage.py runserver

Сущности системы

    Приложение sending
        Sending - все аттрибуты и настройки рассылки
        TrySending - попытки отправок рассылок (и разовые, и регулярные)

    Приложение customer
        Customers - клиенты компании (те, кому отпрвляются рассылки)
    Приложение blog
        Blog - блоги, продвигающие сервис
    Приложение user
        User - пользователи сервиса

Права доступа пользователей

    Обычный пользователь
        CRUD для своих рассылок и клиентов
        Отправка разовых рассылок (из своего списка рассылок) своим клиентам
        Запуск регулярной рассылки (из своего списка рассылок) своим клиентам
    Manager (группа "manager") 
        Включает все права обычных пользователей
        Удаление запущенных рассылоk
        Просмотр списка пользователей сервиса
        Блокировка пользователей сервиса 
        Просмотр всех рассылок и клиентов
    Superuser
        Включает все доступные права
        Дополнительно в Manager menu интерфейса реализован CRUD для модели User
        Дополнительно в Manager menu реализована возможность настраивать расписания рассылок (ONE_A_DAY, ONE_A_WEEK, ONE_A_MONTH)


Создание superuser:
  python manage.py create_user_command



