from django.contrib import admin
from django.urls import path

from core.views import index
from core.views import contact
from core.views import privacy
from core.views import terms

urlpatterns = [
    # set homepage to index view
    path('', index, name='index'),
    # set contact page, privacy page, and terms page
    path('contact/', contact, name='contact'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),

    path('admin/', admin.site.urls),
]
