from django.conf.urls import url, include
from rest_framework import routers

from .views import LibraryViewset, BookInformationViewset, ItemViewset, \
  LoanViewset, LoanUserViewset

router = routers.DefaultRouter()
router.register(r'libraries', LibraryViewset)
router.register(r'books', BookInformationViewset)
router.register(r'items', ItemViewset)
router.register(r'loans', LoanViewset)
router.register(r'users/(?P<userpk>\d+)/loans', LoanUserViewset, base_name='userloans')

urlpatterns = [
    url(r'^', include(router.urls)),
]