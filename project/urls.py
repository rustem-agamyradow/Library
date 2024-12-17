from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [   
    
    path('',views.loginView,name='login'),
    path('home',login_required (views.index), name='index'),
    # path('login', views.loginView, name='login'),
    path('categors', views.categors, name='categors'),
    path('logout/',views.logoutView,name='logout'),
    path('register/',views.register,name='register'),

 

    path('books/<int:category_id>/', views.books, name='books'),

    path('users', views.users, name='users'),

    path('user_about/<int:user_id>/', views.user_about, name='user_about'),

    path('news', views.news, name='news'),

    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),  # Kategori silme
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Kitap silme
    path('delete_news/<int:new_id>/', views.delete_news, name='delete_news'),  # Haber silme


    path('delete_user/<int:user_id>/', views.delete_user, name = 'delete_user'),

    path('news_see/<int:new_id>/', views.news_see, name='news_see'), 



    path('settings', views.settings, name='settings'), 
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('add_categor', views.add_categor, name='add_categor'),


    path('add_book', views.add_book, name='add_book'),



    path('add_user', views.add_user, name='add_user'),



    path('add_new', views.add_new, name='add_new'),
 
    path('about', views.about, name='about'),
    
 
]