from django.urls import path

from . import views

app_name = 'webprint'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list/', views.PrintListView.as_view(), name='print_list'),
    path('<int:pk>/', views.PrintView.as_view(), name='print'),
    path('add/', views.PrintFormView.as_view(), name='print_add'),
]
