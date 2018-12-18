from django.contrib import admin

from libraryAppProxy.models import Library, BookInformation, Item, Loan

# Register your models here.
admin.site.register(Library)
admin.site.register(BookInformation)
admin.site.register(Item)
admin.site.register(Loan)