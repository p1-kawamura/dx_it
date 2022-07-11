from django.urls import path
from .views import index,top,left,right,upload,right1,delete,hyouji_all,hyouji_inoue,hyouji_furukawa,hyouji_mashimo


app_name="houjin2"
urlpatterns = [
    path('index/', index, name="index"),
    path('top/', top, name="top"),
    path('left/', left, name="left"),
    path('right/', right, name="right"),
    path('right/<int:pk>/', right1, name="right1"),
    path('delete/', delete, name="delete"),
    path('upload/', upload, name="upload"),
    path('hyouji_all/', hyouji_all, name="hyouji_all"),
    path('hyouji_inoue/', hyouji_inoue, name="hyouji_inoue"),
    path('hyouji_furukawa/', hyouji_furukawa, name="hyouji_furukawa"),
    path('hyouji_mashimo/', hyouji_mashimo, name="hyouji_mashimo"),
]