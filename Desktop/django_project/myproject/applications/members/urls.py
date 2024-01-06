from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),  we are commenting this line because we are not using function for views , instead for this we are writing a new line for memberclass view
    path('members/',views.MembersView.as_view()), # this is for class view
    # path('authorized/',views.authorized),
    path('authorized/',views.AuthorizedView.as_view()),
]