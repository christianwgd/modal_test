from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='index'),
    path('detail/<int:pk>/', views.BlogPostDetailView.as_view(), name='detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BlogPostUpdateView.as_view(), name='update'),
]
