
from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_register_view, name='register'),

    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view()),

    path('home', views.home, name='home'),
    path('add_it_jobs', views.add_it_jobs, name='add_it_jobs'),
    path('view_it_jobs', views.view_it_jobs, name='view_it_jobs'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update_it_jobs/<int:id>/', views.update_it_jobs, name='update_it_jobs'),

    # path('image_view', views.image_view, name='image_view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
