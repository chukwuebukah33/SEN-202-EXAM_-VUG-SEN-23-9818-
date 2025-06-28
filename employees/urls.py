from django.urls import path
from .views import (
    StaffRoleView,
    ManagerListCreateView,
    ManagerRetrieveUpdateDestroyView,
    InternListCreateView,
    InternRetrieveUpdateDestroyView,
)

urlpatterns = [
    
    path('roles/', StaffRoleView.as_view(), name='staff-roles'),

  
    path('managers/', ManagerListCreateView.as_view(), name='manager-list-create'),
    path('managers/<int:pk>/', ManagerRetrieveUpdateDestroyView.as_view(), name='manager-detail'),

    
    path('interns/', InternListCreateView.as_view(), name='intern-list-create'),
    path('interns/<int:pk>/', InternRetrieveUpdateDestroyView.as_view(), name='intern-detail'),
]
