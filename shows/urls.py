from django.urls import path
from .views import view_shows, ShowCreateView, ShowUpdateView, ShowDeleteView, show_details, index

urlpatterns = [
    path('', index, name='home'),
    path('shows/', view_shows, name='show-list'),
    path('shows/create', ShowCreateView.as_view(), name='show-create'),
    path('shows/<int:pk>/update', ShowUpdateView.as_view(), name='show-update'),
    path('shows/<int:pk>/delete', ShowDeleteView.as_view(), name='show-delete'),
    path('shows/<int:pk>/details', show_details, name='show-details'),

    
]