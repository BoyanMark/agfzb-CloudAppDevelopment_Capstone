from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model:
class CarMake(models.Model):
    # - Name
    name = models.CharField(max_length=35)
    # - Description
    description = models.CharField(max_length=300)
    # - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model:
class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # - Name
    name = models.CharField(max_length=30)
    # - Dealer id, used to refer a dealer created in cloudant database
    dealer_id = models.IntegerField()
    # - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    type_c = models.CharField(max_length=10, choices=(("SEDAN", "SEDAN",), ("SUV", "SUV"), ("HATCHBACK", "HATCHBACK"),("WAGON", "WAGON")))
    # - Year (DateField)
    year = models.DateField()
    # - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id
