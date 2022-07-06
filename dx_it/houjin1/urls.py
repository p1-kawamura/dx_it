from django.urls import path
from .views import index,upload,koshin,delete,hyouji_all,hyouji_inoue,hyouji_furukawa,hyouji_mashimo
from django.contrib.auth import views as auth_views


app_name="houjin1"
urlpatterns = [
    path('', index, name="index"),
    path('upload/', upload, name="upload"),
    path('koshin/<int:pk>/', koshin, name="koshin"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('hyouji_all/', hyouji_all, name="hyouji_all"),
    path('hyouji_inoue/', hyouji_inoue, name="hyouji_inoue"),
    path('hyouji_furukawa/', hyouji_furukawa, name="hyouji_furukawa"),
    path('hyouji_mashimo/', hyouji_mashimo, name="hyouji_mashimo"),
    path('login/', auth_views.LoginView.as_view(template_name='houjin1/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]