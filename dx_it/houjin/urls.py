from django.urls import path
from .views import index,top,left,right,right1,upload,delete,hyouji,csv_page,page_next,page_last,page_first,page_prev,\
    dm_send,dm_down,sell,sell_delete,index2,index2_nen,index2_click,index2_save,rec_keisan,\
    download_customer,download_item,download_recieve,download_sell,test
from django.contrib.auth import views as auth_views


app_name="houjin"
urlpatterns = [
    path('', index, name="index"),  
    path('top/', top, name="top"),
    path('left/', left, name="left"),
    path('left/<int:num>/', left, name="left"),
    path('right/', right, name="right"),
    path('right/<int:pk>/', right1, name="right1"),
    path('delete/', delete, name="delete"),
    path('hyouji/', hyouji, name="hyouji"),
    path('upload/', upload, name="upload"),
    path('csv_page/', csv_page, name="csv_page"),
    path('rec_keisan', rec_keisan, name="rec_keisan"),
    path('login/', auth_views.LoginView.as_view(template_name='houjin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('page_first/', page_first, name="page_first"),
    path('page_prev/', page_prev, name="page_prev"),
    path('page_next/', page_next, name="page_next"),
    path('page_last/', page_last, name="page_last"),
    path('dm_send/', dm_send, name="dm_send"),
    path('dm_down/', dm_down, name="dm_down"),
    path('sell/', sell, name="sell"),
    path('sell_delete/<int:pk>', sell_delete, name="sell_delete"),
    path('index2/', index2, name="index2"),
    path('index2_nen/', index2_nen, name="index2_nen"),
    path('index2_click/', index2_click, name="index2_click"),
    path('index2_save/', index2_save, name="index2_save"),
    path('download_customer/', download_customer, name="download_customer"),
    path('download_item/', download_item, name="download_item"),
    path('download_recieve/', download_recieve, name="download_recieve"),
    path('download_sell/', download_sell, name="download_sell"),
    path('test/', test, name="test"),
]