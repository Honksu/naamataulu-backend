from rest_framework import viewsets

from .serializers import LibrarySerializer, BookInformationSerializer, \
  ItemSerializer, LoanSerializer

from .models import Library, BookInformation, Item, Loan

class LibraryViewset(viewsets.ModelViewSet):
  queryset = Library.objects.all()
  serializer_class = LibrarySerializer

class BookInformationViewset(viewsets.ModelViewSet):
  queryset = BookInformation.objects.all()
  serializer_class = BookInformationSerializer

class ItemViewset(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class LoanViewset(viewsets.ModelViewSet):
  queryset = Loan.objects.all()
  serializer_class = LoanSerializer      