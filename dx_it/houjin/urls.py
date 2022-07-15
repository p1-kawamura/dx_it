from django.urls import path
from .views import index,top,left,right,right1,upload,delete,hyouji_all,hyouji_inoue,hyouji_furukawa,hyouji_mashimo,csv_page
from django.contrib.auth import views as auth_views


app_name="houjin"
urlpatterns = [
    path('', index, name="index"),  
    path('top/', top, name="top"),
    path('left/', left, name="left"),
    path('right/', right, name="right"),
    path('right/<int:pk>/', right1, name="right1"),
    path('delete/', delete, name="delete"),
    path('hyouji_all/', hyouji_all, name="hyouji_all"),
    path('hyouji_inoue/', hyouji_inoue, name="hyouji_inoue"),
    path('hyouji_furukawa/', hyouji_furukawa, name="hyouji_furukawa"),
    path('hyouji_mashimo/', hyouji_mashimo, name="hyouji_mashimo"),   
    path('upload/', upload, name="upload"),
    path('csv_page/', csv_page, name="csv_page"),
    path('login/', auth_views.LoginView.as_view(template_name='houjin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]