from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemsView.as_view()),
    path('item/<int:pk>/', views.ItemView.as_view()),
    path('add/', views.AddItem.as_view()),
    path('employee/', views.EmployeeView.as_view()),
    path('company/', views.CompanyView.as_view()),
]
