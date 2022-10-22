"""dj_secret_santa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web_santa.views import PageNotFound

# здесь маршруты страниц
# функция path связывает маршрут и функцию представления
# у функции path 2 обяз аргумента и третий необязательный (имя для маршрута):
# - сам подадрес (маршрут, префикс, тип строка), добавляемый
# к главному адресу (домену), например http://127.0.0.1:8000/secret_santa/
# - и функция или класс возвращающие объект представления
# здесь напрмер функция index возвращает объект HttpResponse
# функцию или класс возвращающие объект представления нужно импортировать сюда
# из приложения из файла views.py
# в файле views.py приложения прописаны функции и классы возвращающие объект представления

# функция include импортированная из django.urls содержит список url адресов приложения
# и связанные с ними функции представлений, ей (include) нужно передать
# путь (в виде строки) к файлу urls.py в приложении, содержащему маршруты данного приложения
# здесь это 'web_santa.urls'
# функцию include нужно передать в path вторым аргументом,
# при этом первый аргумент - это префикс, с которого будут начинаться
# все маршруты приложения
# если используем только include, то импортировать сюда функции и классы
# из файла views.py приложений (например web_santa) не нужно
# импорты функций и классов делаем в файле urls.py приложения

urlpatterns = [
    path('admin/', admin.site.urls),          # http://127.0.0.1:8000/admin/
    path('web/', include('web_santa.urls'))   # http://127.0.0.1:8000/web/
]

# переменная handler404 (должна называться именно так)
# создаётся для кастомного отображения ошибки 404 (страница не найдена)
# функция, которая присваивается этой переменной, определяется в файле views.py приложения
# и импортируется сюда
handler404 = PageNotFound

# также есть ещё множество обработчиков исключений при запросах к серверу
# например:
# 500 - ошибка сервера
# 403 - доступ запрещён
# 400 - невозможно обработать запрос
handler500 = None
handler403 = None
handler400 = None
