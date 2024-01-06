from . import views
from django.urls import path


urlpatterns=[
    # path('notes',views.list),
    # this url will be diff because here we are passing a value on run time
    # http://127.0.0.1:8000/smart/notes/1 
    #  int is integer number
    # path('notes/<int:pk>',views.detail),
    path('notes',views.NotesListView.as_view(),name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
]