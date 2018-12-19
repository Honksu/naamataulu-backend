from rest_framework import serializers

from .models import Library, BookInformation, Item, Loan

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class BookInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInformation
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'library', 'info', 'reserved')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'