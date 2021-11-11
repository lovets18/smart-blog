from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('addarticle/', views.addarticle, name='addarticle'),
    path('addarticle/added/<int:user_id>/', views.added, name='added'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
]

