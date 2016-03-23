# -*- coding:utf-8 -*-
from django.conf.urls import url,include
from management import views

urlpatterns=[
    url(r'^$',views.index,name='homepage'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^set_password/$',views.set_password,name='set_password'),
    url(r'^add_book/$',views.add_book,name='add_book'),
    url(r'add_image/$',views.add_image,name='add_image'),
    url(r'^view_book_list/$',views.view_book_list,name='view_book_list'),
    url(r'^book/detail/$',views.detail,name='detail'),
    url(r'^register/$',views.user_register,name='register'),

    # url 已经完成，接下来就是对应模板的编写了

]