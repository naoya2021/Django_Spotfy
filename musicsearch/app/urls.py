from django.urls import path
from django.urls.resolvers import URLPattern
from app import views
from django.contrib.auth import views as auth_views

app_name='app'

urlpatterns=[
    path('home/',views.IndexView.as_view(),name='index'),
    path('detail/<str:id>',views.DetailView.as_view(),name='detail'),
    path('',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
]