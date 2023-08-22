from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('sign_in', views.sign_in, name = 'sign_in'),
    path('sign_out',views.sign_out, name = 'sign_out'),
    path('logout', views.logout_user,name = 'logout'),
    path('update/<id>/',views.update,name = 'update'),
    path('delete/<id>',views.delete, name = 'delete'),
    path('viewBlog/<id>', views.viewBlog, name = 'viewBlog'),
    path('blog', views.blogInfo, name = 'blog'),
    path('addContent', views.addContent, name = 'addContent')
]