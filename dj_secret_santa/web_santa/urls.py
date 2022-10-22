from django.urls import path
from .views import *

# путь к странице с представлением index с префиксом web/, потому что
# в конфигурационном пакете в файле urls.py в path для приложения web_santa
# мы прописали префикс - 'web/', так что к домену добавился префикс web/
# вот что в конфигурационном urls.py: path('web/', include('web_santa.urls'))
# у path есть параметр name, он задаёт ИМЯ для маршрута
# это имя используется в джанге например для редиректов и т.д.
urlpatterns = [
    path('', index, name='main_web'),        # http://127.0.0.1:8000/web/
    path('users/', users),                   # http://127.0.0.1:8000/web/users/
]
