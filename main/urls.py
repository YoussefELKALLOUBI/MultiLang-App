from django.urls import path
from .views import article_list
from .views import chatbot_view
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('', article_list, name='article_list'),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('i18n/setlang/', set_language, name='set_language'),
]