from django.urls import path
from . import views

urlpatterns = [
    path('', views.redir),
    path('shows/new', views.index),
    path('shows/create', views.create),
    path('shows', views.allshows),
    path('shows/<int:current_id>', views.displayshow),
    path('shows/<int:current_id>/edit', views.edit),
    path('shows/<int:current_id>/delete', views.delete),
    path('shows/<int:current_id>/update', views.update),

]
