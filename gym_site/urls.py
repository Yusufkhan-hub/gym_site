from django.contrib import admin
from django.urls import path,include
from gym_site import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name='index'),
    path('content', views.content,name='content'),
    path('gallery', views.gallery,name='gallery'),
    path('instructor', views.instructor,name='instructor'),
    path('signup', views.signup,name='signup'),
    path('about', views.about,name='about'),
    path('why_fit_hit', views.why_fit_hit,name='why_fit_hit'),
    path('create_user',views.create_user,name='create_user'),
    path('acconuts/',include('django.contrib.auth.urls')),    
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 