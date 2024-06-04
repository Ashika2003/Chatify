
from . import views
from django.urls import path
 
urlpatterns = [
   path('',views.rooms, name="rooms"),
   path("<str:slug>",views.room, name="room")
]
