from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import WordSerializer
from .models import Word


class CreateWordView(CreateAPIView):
    serializer_class = WordSerializer


class WordDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordListView(ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer