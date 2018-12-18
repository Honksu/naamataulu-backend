from django.conf.urls import url, include
from rest_framework import routers

from .views import LibraryViewset, BookInformationViewset, ItemViewset, \
  LoanViewset

router = routers.DefaultRouter()
router.register(r'libraries', LibraryViewset)
router.register(r'books', BookInformationViewset)
router.register(r'items', ItemViewset)
router.register(r'loans', LoanViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]