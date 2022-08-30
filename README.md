# Сайт о достопримечательностях Москвы
Это учебный проект сайта с точками и описаниями достопримечательностей Москвы, сделанный для devman.org
Тестовую версию сайта можно посмотреть по ![ссылке](http://dimitryroukhadze.pythonanywhere.com/)

## Установка и подготовка к работе

Для работы необходимо установить необходимые библиотеки. Это делается с помощью команды в терминале:
```commandline
pip install -r requirements.txt
```

После установки всех библиотек, создайте файл `.env` и поместите в него следующие переменные:
```dotenv
DJANGO_SECURITY_KEY=Ваш ключ безопасности Django
STATIC_ROOT=путь/к/папке
ALLOWED_HOSTS=['Разрешенный хост 1', 'Разрешенный хост 2']
DEBUG_MODE=False
CSRF_COOKIE_SECURE=True или False
SESSION_COOKIE_SECURE=True или False
```

При первом запуске откройте терминал в папке `where_to_go` и запустите команду `python manage.py migrate` для создания
пустой базы данных.

Затем вам необходимо заполнить базу данных с достопримечательностями. Это можно сделать либо вручную через админку (см.ниже),
либо подготовить `.json` файлы с данными о достопримечательностях и загрузить их с помощью команды менеджера `load_place` Шаблон такого файла вы можете найти в этом репозитории.
Название файла `place_example.json`.

После того как подготовите файлы, запустите команду менеджера и передайте ей папку с файлами в качестве аргумента, как показано ниже:

```bash
python manage.py load_url https://ваш/url
```

## Работа сайта

### Сайт
При запуске сайта вы увидите карту Москвы с точками на ней:
![togo1](https://user-images.githubusercontent.com/77689849/185153044-667ee4eb-b191-4799-bccc-e023f9c41f7a.JPG)

Если нажать на точку, слева появится сайдбар с описанием и картинками места:
![togo2](https://user-images.githubusercontent.com/77689849/185153111-b9499960-ee01-4abc-8579-7cefc86bd559.JPG)

### Админка

У сайта по адресу `http://вашхост/admin` доступна админка:
![togo3](https://user-images.githubusercontent.com/77689849/185153189-00285387-d4bf-4f69-9281-2ec8e5c9e6cf.JPG)

В ней вы можете добавлять новые места (Places) и изображения к ним (Images). При добавлении нового места поле `title` является
обязательным, остальные поля вы можете заполнить по мере необходимости. Также, внизу описания места вы можете видеть изображения,
которые к нему относятся. Порядок изображений можно менять.
![togo4](https://user-images.githubusercontent.com/77689849/185153279-7b980732-4a32-425b-a378-17524360440e.JPG)
![togo5](https://user-images.githubusercontent.com/77689849/185153445-144589fb-1b2b-4f08-9501-e5028d31dab8.JPG)

При добавлении изображений обязательно указывайте место, к которому оно относится в поле `place`
![togo6](https://user-images.githubusercontent.com/77689849/185153504-7dfd4913-a5be-45c9-9bca-8896e1a17b73.JPG)

