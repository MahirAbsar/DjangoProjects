from django.conf.urls import url
from django.urls import path
from first_app import views


app_name = 'first_app'
urlpatterns = [

    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('add_musician/',views.musician_form,name='musician_form'),
    path('add_album/',views.album_form,name = 'album_form'),
    path('album_list/<int:id>/',views.list_of_albums,name='list_of_albums'),
    path('update_musician/<int:id>/',views.update_musician,name='update_musician'),
    path('edit_album/<int:id>/',views.update_album,name="update_album"),
    path('delete_album/<int:id>',views.delete_album,name='delete_album'),
    path('delete_musician/<int:id>',views.delete_musician,name='delete_musician'),
]
