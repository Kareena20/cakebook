from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from recipes import views as recipe_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('register/', recipe_views.register, name='register'),
    path('login/',recipe_views.login_view , name='login'),
    path('logout/', recipe_views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
