from django.db import models
from api.models import User

# Create your models here.
class Library(models.Model):
  library_types = (
    ('OL', 'OfficeLibrary'),
    ('EL', 'Elibrary'),
    ('UL', 'UnknownLibrary'),
  )

  name = models.CharField(max_length=128)
  library_type = models.CharField(max_length=2, choices=library_types, default='UnknownLibrary')

  def __str__(self):
    return self.name

class BookInformation(models.Model):
  title = models.CharField(max_length=128)
  ISBN = models.CharField(max_length=13)
  author = models.CharField(max_length=128)
  publisher = models.CharField(max_length=128)
  published = models.DateTimeField()
  cover = models.CharField(max_length=128, null=True, blank=True)
  amazon_link = models.CharField(max_length=128, null=True, blank=True)

  def __str__(self):
    return self.title

class Item(models.Model):
  library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)
  info = models.ForeignKey(BookInformation, on_delete=models.PROTECT)

  def __str__(self):
    return "%s @ %s" % (self.info.title, self.library.name)

class Loan(models.Model):
  date_loaned = models.DateTimeField()
  info = models.ForeignKey(Item, on_delete=models.CASCADE)
  person = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return "%s loaned by %s" % (str(self.info), str(self.person))