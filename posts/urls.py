from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),

    path('users_info', views.users_info, name='users_info'),
    path('send_message/<int:post_id>', views.send_message),
    # path('list', views.list, name='list'),

    path('boxing', views.boxing, name='boxing'),
    path('create_boxing', views.create_boxing, name='create_boxing'),
    path('update_boxing/<int:post_id>', views.update_boxing),
    path('delete_boxing/<int:post_id>', views.delete_boxing),
    path('boxing/<slug:post_slug>', views.show_boxing, name='boxing_slug'),

    path('wrestling', views.wrestling, name='wrestling'),
    path('create_wrestling', views.create_wrestling, name='create_wrestling'),
    path('update_wrestling/<int:post_id>', views.update_wrestling),
    path('delete_wrestling/<int:post_id>', views.delete_wrestling),
    path('wrestling/<slug:post_slug>', views.show_wrestling, name='wrestling_slug'),

    path('athletics', views.athletics, name='athletics'),
    path('create_athletics', views.create_athletics, name='create_athletics'),
    path('update_athletics/<int:post_id>', views.update_athletics),
    path('delete_athletics/<int:post_id>', views.delete_athletics),
    path('athletics/<slug:post_slug>', views.show_athletics, name='athletics_slug'),

    path('weightlifting', views.weightlifting, name='weightlifting'),
    path('create_weightlifting', views.create_weightlifting, name='create_weightlifting'),
    path('update_weightlifting/<int:post_id>', views.update_weightlifting),
    path('delete_weightlifting/<int:post_id>', views.delete_weightlifting),
    path('weightlifting/<slug:post_slug>', views.show_weightlifting, name='weightlifting_slug'),

    path('cycling', views.cycling, name='cycling'),
    path('create_cycling', views.create_cycling, name='create_cycling'),
    path('update_cycling/<int:post_id>', views.update_cycling),
    path('delete_cycling/<int:post_id>', views.delete_cycling),
    path('cycling/<slug:post_slug>', views.show_cycling, name='cycling_slug'),

    path('team_sports', views.team_sports, name='team_sports'),
    path('create_team_sports', views.create_team_sports, name='create_team_sports'),
    path('update_team_sports/<int:post_id>', views.update_team_sports),
    path('delete_team_sports/<int:post_id>', views.delete_team_sports),
    path('team_sports/<slug:post_slug>', views.team_sports, name='team_sports_slug'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)