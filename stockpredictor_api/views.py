from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import generics

from stockpredictor.models import StockData
from .serializers import StockSerializer

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

import datetime

from .functionality import initiate_prediction

"""
class StockList(generics.ListCreateAPIView):
    queryset = Stock.stockobjects.all()
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
"""


# Class Based View - Stock API Request
class StockAPIView(APIView):
    # API_KEY = "PKDCC68WUIENQGI2PVXS"
    # SECRET_KEY = "HprE8OKNDtvw4X21KEDgDhtsAIF4j8FylmZm5g0U"

    def get(self, request):
        response = self.obtain_stock_data(request)

        # Required for AI functionality
        # response2 = self.obtain_stock_prediction()

        return response

    @csrf_exempt
    def obtain_stock_data(self, request):
        # Stock to obtain - can obtain these values from request later
        stock = "BTC/USD"
        end = "2024-09-01"

        # Processed start values
        endDate = datetime.date(int(end[0:4]), int(end[5:7]), int(end[8:10]))
        startDate = endDate - datetime.timedelta(days=300)

        start = startDate.strftime("%Y-%m-%d")
        end = endDate.strftime("%Y-%m-%d")

        # Check that historical data is not already in the database
        # if StockData.objects.filter(symbol=stock).exists():
        #     pass

        # Obtain historical stock Data
        crypto_client = CryptoHistoricalDataClient()
        request_params = CryptoBarsRequest(
            symbol_or_symbols=[stock],
            timeframe=TimeFrame.Day,
            start=start,
            end=end
        )
        btc_bars = crypto_client.get_crypto_bars(request_params).df

        # Add data to Database
        # size = btc_bars.size
        # for i in range(0, size-1):
        #     btc_bars.iloc[i].to_numpy()

        # Send btc_bars directly for AI prediction processing
        stock_prediction = self.obtain_stock_prediction(btc_bars, "lin_reg").tolist()

        # Create JSON Response dictionary
        response_data = {}
        stock_dictionary = btc_bars.to_dict("records")
        index = 0
        for single_date in self.daterange(startDate, endDate):
            response_data[index] = stock_dictionary[index]
            response_data[index]["date"] = single_date
            index += 1

        # Add stock prediction to response_data
        predicted_index = 0
        for predicted_close_price in stock_prediction:
            response_data[index] = {}
            response_data[index]["close"] = stock_prediction[predicted_index]
            response_data[index]["close2"] = stock_prediction[predicted_index]
            predicted_index += 1
            index += 1
        
        # Process JSON String from Dict
        response = JsonResponse(response_data)

        # Return result
        return response
    
    def obtain_stock_prediction(self, raw_data, algorithm):
        result = initiate_prediction(raw_data, algorithm)
        return result

    def daterange(self, start_date: datetime.date, end_date: datetime.date):
        days = int((end_date - start_date).days)
        for n in range(days):
            yield start_date + datetime.timedelta(n)
