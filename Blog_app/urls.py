from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view, contact_success_view,login_view, register_view

urlpatterns = [
    path('', views.AllPostsView.as_view(), name='home'),
    path('django/', views.DjangoList.as_view(), name='django'),
    path('development/', views.DevelopmentList.as_view(), name='development'),
    path('networking/', views.NetworkingList.as_view(), name='networking'),
    path('privacy/', views.Privacy.as_view(), name='privacy'),
    path('about/', views.About.as_view(), name='about'),
    path('support/', views.Support.as_view(), name='support'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path('create_post/', views.create_post, name='create_post'),
    path('login/', login_view, name='login'),
    path('register/',register_view, name='register'),
    path('<slug:slug>/', views.DjangoDetail.as_view(), name='django_detail'),
    path('development/<slug:slug>/', views.DevelopmentDetail.as_view(), name='development_detail'),
    path('networking/<slug:slug>/', views.NetworkingDetail.as_view(), name='networking_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)