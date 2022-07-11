from django.urls import path
from .views import index,upload,koshin,delete,hyouji_all,hyouji_inoue,hyouji_furukawa,hyouji_mashimo,csv_page, \
     v2_index,v2_top,v2_left,v2_right,v2_right1,v2_delete,v2_hyouji_all,v2_hyouji_inoue,v2_hyouji_furukawa,v2_hyouji_mashimo
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
    path('csv_page/', csv_page, name="csv_page"),
    path('v2_index/', v2_index, name="v2_index"),
    path('v2_top/', v2_top, name="v2_top"),
    path('v2_left/', v2_left, name="v2_left"),
    path('v2_right/', v2_right, name="v2_right"),
    path('v2_right/<int:pk>/', v2_right1, name="v2_right1"),
    path('v2_delete/', v2_delete, name="v2_delete"),
    path('v2_hyouji_all/', v2_hyouji_all, name="v2_hyouji_all"),
    path('v2_hyouji_inoue/', v2_hyouji_inoue, name="v2_hyouji_inoue"),
    path('v2_hyouji_furukawa/', v2_hyouji_furukawa, name="v2_hyouji_furukawa"),
    path('v2_hyouji_mashimo/', v2_hyouji_mashimo, name="v2_hyouji_mashimo"),
]