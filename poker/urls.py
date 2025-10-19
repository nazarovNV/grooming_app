from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create-room/', views.create_room, name='create_room'),
    path('room/<uuid:room_id>/', views.room_detail, name='room_detail'),
    path('task/<int:task_id>/vote/', views.vote, name='vote'),
    path('task/<int:task_id>/complete/', views.complete_voting, name='complete_voting'),
    path('task/<int:task_id>/results/', views.vote_results, name='vote_results'),
]