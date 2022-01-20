# smart-blog
Многопользовательский блог, осуществляющий орфографический контроль введенного пользователем текста

### myfirst/apps/articles/autocorrection.py - функции для коррекции текста

myfirst/apps/articles - директория с файлами приложения articles

<hr/>

myfirst/apps/articles/static/ - статические файлы приложение articles

myfirst/apps/articles/static/css - стили

myfirst/apps/articles/static/images - изображение

myfirst/apps/articles/tests - директория с тестами, запускаются командой python manage.py test articles из корня проекта

myfirst/apps/articles/tests/tests.py - тесты TestCase, проверяют модели, формы, представления, а также функцию коррекции текста

myfirst/apps/articles/tests/tests_selenium.py - тесты Selenium, иммитируют поведение реального пользователя

myfirst/apps/articles/forms.py - формы ввода

myfirst/apps/articles/models.py - модели сущностей БД

myfirst/apps/articles/urls.py - пути в приложении articles

myfirst/apps/articles/views.py - представления

myfirst/static - статические файлы проекта

myfirst/static/grapelli - кастомизация панели администратора

myfirst/static/admin - панель администратора

myfirst/templates/base.html - базовый шаблон для рендеринга

myfirst/templates/articles - частные шаблоны для рендеринга

myfirst/settings.py - файл настроек
myfirst/urls.py - файл путей проекта

manage.py - файл для управления проектом

для первоначальной настройки:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
