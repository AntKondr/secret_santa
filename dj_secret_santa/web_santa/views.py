from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
# в этом файле прописываются все представления приложения
# представления можно оформлять как функцию возвращающую объекты Response (ответ), или как классы
# имя функции или класса может быть любым (задаём говорящее имя)
# для функции первым аргументом обязательно указываем request (запрос)
# в аргумент request будет ссылаться класс HttpRequest, он содержит информацию о запросе,
# о сессии, о куках, заголовки, параметры запроса и т.д.
# т.е. через переменную request внутри функции нам доступна
# вся информация в рамках текущего запроса
# на выходе функция должна возвращать объект Response (ответ) или redirect
# и нужно импортировать эти объекты для данного файла
# далее связываем эту функцию или класс с URL адресом (маршрутом)
# в главном пакете конфигурации в файле urls.py
# или в файле urls.py приложения, если юзаем include в главном urls.py
# пакет конфигурации это главная папка (здесь dj_secret_santa)
# в файле urls.py прописываем объект path со ссылкой на функции или классы представлений
# (имя функции, в данном случае index, users и т.д.)


def index(request):
    return HttpResponse('<h1>main page of secret santa</h1>')


def users(request):
    return HttpResponse('<h1>this page of users</h1>')


# эта функция для handler404, обяз должна принимать 2 аргумента
# request и exception
# возвращает объект HttpResponseNotFound (не забываем импортить его сюда)
def PageNotFound(request, exception):
    if request.path == '/':
        # redirect выполняет перенаправление
        # не забываем импортить его из django.shortcuts
        # у redirect два кода, 301 и 302 (по умолчанию 302 (permanent=False))
        # чтобы был 301 redirect, добавляем второй аргумент permanent=True
        # 301 - страница перемещена на другой постоянный URL-адрес
        # 302 - страница перемещена временно на другой URL-адрес
        # первый параметр - это адрес, куда происходит перенаправление
        # в данном случае мы использовали имя адреса ('main_web'), имя адресу даётся в urls.py
        # но можно и явно прописать адрес
        return redirect('main_web', permanent=True)
    else:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')
