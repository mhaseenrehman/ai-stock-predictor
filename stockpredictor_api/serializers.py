from rest_framework import serializers
from stockpredictor.models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            "title",
            "symbol",
            "price",
            "lastupdate",
        )

    