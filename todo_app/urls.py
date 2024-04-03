from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('add_form/', views.add_form, name="add_form"),
    path('edit_click/<int:pk>', views.edit_click, name="edit_click"),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete_todo'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('post_details/<int:pk>', views.post_details, name='post_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
