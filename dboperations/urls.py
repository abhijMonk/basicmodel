from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_author', views.get_author),
    path('<str:author_first_name>', views.get_author),

]
'''   
    path('blog/', views.get_blog),
    path('category', views.get_category),
    path('addauthor/', views.add_author),
    path('addblog/', views.add_blog),
    path('addcategory/', views.add_category),
    path('article/', views.get_article),
    path('addarticle/', views.add_article),
'''