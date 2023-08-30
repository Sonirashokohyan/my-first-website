from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('sale/', views.sale, name='sale'),
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('property/<detid>', views.property, name='property'),
    # path('contact/', views.contact, name='contact'),
    # path('savecontact/', views.savecontact, name='savecontact'),
    # path('', views.index, name='index'),
    # path('members/index/shop', views.shop, name='shop'),
    
    path('', views.home, name='members'),
    path('home/about/', views.about, name='about'),
    path('home/contact/', views.contact, name='contact'),
    path('home/men/', views.men, name='men'),
    path('home/women/', views.women, name='women'),
    path('details/<detid>/', views.property, name='property'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
