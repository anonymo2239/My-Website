from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('projects/', views.projects, name='projects'),
    path('photos/', views.photos, name='photos'),
    path('blog/', views.blog, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)