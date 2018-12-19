from datetime import datetime

from django.http import HttpResponse
import django_filters.rest_framework
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from .serializers import LibrarySerializer, BookInformationSerializer, \
  ItemSerializer, LoanSerializer

from .models import Library, BookInformation, Item, Loan
from api.models import User

'''
API routes from futurice/haskell-mega-repo/library-app
booksGet  DONE
:: route :- "book" :> Get '[JSON] [BookInformationResponse]

bookGet DONE
:: route :- "book" :> Capture "id" BookInformationId :> Get '[JSON] BookInformationResponse

bookByISBNGet DONE
:: route :- "book" :> "isbn" :> Capture "isbn" Text :> Get '[JSON] BookInformationByISBNResponse

bookCoverGet TODO
:: route :- BookCoverEndpoint

borrowPost DONE
:: route :- SSOUser :> "book" :> "borrow" :> ReqBody '[JSON] BorrowRequest :> Post '[JSON] Loan

itemDelete DONE
:: route :- "item"  :> Capture "id" ItemId :> Delete '[JSON] Text

snatchPost IGNORE
:: route :- SSOUser :> "book" :> "snatch" :> Capture "id" ItemId :> Post '[JSON] Loan

loansGet DONE
:: route :- "loan" :> Get '[JSON] [Loan]

loanGet DONE
:: route :- "loan" :> Capture "id" LoanId :> Get '[JSON] Loan

returnPost DONE
:: route :- "return" :> Capture "id" LoanId :> Post '[JSON] Bool

personalLoansGet DONE
:: route :- SSOUser :> "user" :> "loan" :> Get '[JSON] [Loan]

sendReminderEmailsPost IGNORE
:: route :- SSOUser :> "reminder" :> Get '[JSON] Bool
'''

class LibraryViewset(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  queryset = Library.objects.all()
  serializer_class = LibrarySerializer

class BookInformationViewset(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  queryset = BookInformation.objects.all()
  serializer_class = BookInformationSerializer
  filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
  filter_fields = ('ISBN',)

class ItemViewset(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class LoanViewset(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  queryset = Loan.objects.all().filter(returned=False)
  serializer_class = LoanSerializer

  @action(detail=True, methods=['post'])
  def returnLoan(self, request, pk=None):
    try:
      loan = Loan.objects.get(pk=pk)
      loan.returned = True
      loan.save()
      return HttpResponse('Loan returned', 200)
    except ObjectDoesNotExist:
      return HttpResponse('Loan not found', 404)

class LoanUserViewset(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = LoanSerializer

  def get_queryset(self):
    userpk = self.kwargs['userpk']
    print('userpk', userpk, self.kwargs)
    try:
      user = User.objects.get(pk=userpk)
    except ObjectDoesNotExist:
      user = None

    return Loan.objects.filter(person=user, returned=False)

  @action(detail=False, methods=['post'])
  def borrow(self, request, pk=None, userpk=None):
    item = Item.objects.get(pk=request.data['id'])
    if not item.reserved():
      person = User.objects.get(pk=userpk)
      newLoan = Loan.objects.create(date_loaned=datetime.now(), item=item, person=person)
      return HttpResponse('Item loaned', 200)
    else:
      return HttpResponse('Item already loaned', 412)

  