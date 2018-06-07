from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
   #path('', include('languages.urls'))
   path('', include(router.urls)) # you can't see url. but its generated internally access to urls
   #it creates HTml and you can see from postman. runserver
]

# what i want to get through API
#start with a model you need some kind of a model
