from django.contrib import admin
from django.urls import path

from core.views import index

urlpatterns = [
    # set homepage to index view
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
