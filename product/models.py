import decimal
import datetime

from django.db import models

class Category(models.Model):
    """
    Top level category model
    """
    title = models.CharField(max_length=64, unique=True)
    
    def __unicode__(self):
        return self.title

class SubCategory(models.Model):
    """
    Sub category model
    """
    category = models.ForeignKey(Category)
    title    = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.title

class Brand(models.Model):
    """
    Brand/Manufacturer model
    """
    name    = models.CharField(max_length=64, unique=True)
    website = models.CharField(max_length=128)
        
    def __unicode__(self):
        return self.name

class Currency(models.Model):
    """
    Currency model for USD, EUR, YEN, INR etc
    """
    name = models.CharField(max_length=3, unique=True)
        
    def __unicode__(self):
        return self.name

class Unit(models.Model):
    """
    Measurement unit model for length, weight, speed, zoom etc
    """
    name = models.CharField(max_length=16, unique=True)
        
    def __unicode__(self):
        return self.name

class Product(models.Model):
    """
    Product model with common properties for all products
    """
    name         = models.CharField(max_length=64)
    brand        = models.ForeignKey(Brand)
    sub_category = models.ForeignKey(SubCategory)
    description  = models.TextField()
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    currency     = models.ForeignKey(Currency)
    url          = models.CharField(max_length=1024)
        
    def __unicode__(self):
        return self.name

    def get_review_count(self):
        """
        get count of all reviews for this product
        """
        return len(Review.objects.filter(product=self))

    def get_rating(self):
        """
        get average rating from all reviews of this product
        """
        rating = 0
        reviews = Review.objects.filter(product=self)
        if len(reviews) == 0: 
            return 0
        for review in reviews:
            rating += review.rating
        return float(rating)/float(len(reviews))

    def get_properties(self):
        """
        get custom properties for a product
        """
        return Property.objects.filter(Product=self)

    def get_offers_count(self):
        """
        convenience function for templates
        """
        return len(Offer.objects.filter(product=self))

    def get_offers(self):
        """
        get all offers given on this a product
        i.e. discount coupons, gifts etc
        """
        return Offer.objects.filter(product=self)

class Offer(models.Model):
    """
    Offer model for some seasonal discount, gift, coupon etc
    (at the moment, only considering coupon code)
    """
    product  = models.ForeignKey(Product)
    name     = models.CharField(max_length=256)
    # coupon code should be unique
    coupon   = models.CharField(max_length=128, unique=True)
    validity = models.DateField()
    used     = models.BooleanField(default=False)
        
    def __unicode__(self):
        return self.name

class Property(models.Model):
    """
    A specific property for a product
    i.e. screen size, processor speed, battery life etc
    """
    product = models.ForeignKey(Product)
    name    = models.CharField(max_length=128)
    value   = models.CharField(max_length=128)

    # data type for property, int, string, decimal, etc
    # we will need to convert data to appropriate type
    # for making decisions, eg. string -> integer/decimal
    data_type = models.CharField(max_length=128)

    # unit for property, inches, kg, hz, volts, watt
    unit = models.ForeignKey(Unit)

    def __unicode__(self):
        return self.name

class Review(models.Model):
    """
    Review for a product,

    A product will have serveral review, average of all
    these reviews will be the total rating of product
    """
    product   = models.ForeignKey(Product)
    rating    = models.IntegerField()
    post_date = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return "%s with Rating: %d" % (self.product, self.rating)
