from django.db import models
from django.utils import timezone

# Category - Each stock has a category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Stock - Data for each stock of a category
class Stock(models.Model):

    # PERHAPS NOT REQUIRED
    class StockObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status="on")
    

    # Stock Manager - JUST TO KEEP WITH TUTORIAL
    options = (
        ('on', 'On'),
        ('off', 'Off'),
    )

    # Identification of the stock
    title = models.CharField(max_length=250)

    # Important for Stock Data
    symbol = models.TextField(null=True)
    data = models.TextField(null=True)

    # Category of Stock - ETF, Forex, Crypto
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    
    # Price and last update
    price = models.DecimalField(decimal_places=100, max_digits=1000)
    lastupdate = models.DateTimeField(default=timezone.now)

    # URL related if there exists multiple options to view
    slug = models.SlugField(max_length=250, unique_for_date="on")
    status = models.CharField(max_length=10, choices=options, default="on")

    # Model Managers
    objects = models.Manager()
    stockobjects = StockObjects()

    # Order data
    class Meta:
        ordering = ('-lastupdate',)

    # To String - returns title
    def __str__(self):
        return self.title
    
# For Alpaca Stock market Data
class StockData(models.Model):
    symbol = models.TextField(null=True)
    data = models.TextField(null=True)