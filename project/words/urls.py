from django.urls import path
from .views import CreateWordView, WordDetailView, WordListView

urlpatterns = [
    path('word/create/', CreateWordView.as_view()),
    path('word/<int:pk>/', WordDetailView.as_view()),
    path('word/list/', WordListView.as_view()),
]


