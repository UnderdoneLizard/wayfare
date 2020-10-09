from django.urls import path
from . import views
from django.conf.urls.static import static
from wayfare import settings 

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('accounts/profile/edit', views.profile_edit, name='profile_edit'),
] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)