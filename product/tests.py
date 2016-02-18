import datetime
from django.test import TestCase
from django.contrib.auth.models import User

from product.models import *

class ProductTestCase(TestCase):
    """
    test cases for product model
    """

    category     = None
    sub_category = None
    brand        = None
    currency     = None

    def setUp(self):
        """
        create a test category, sub-category and a brand for a test product
        """
        # creating test category
        self.category = Category(title='Tablets and Phones')
        self.category.save()

        # creating test sub category
        self.sub_category = SubCategory(title='Smartphones', category=self.category)
        self.sub_category.save()

        # creating test brand
        self.brand = Brand(name='Sony', website='http://www.sony.com/prod123/')
        self.brand.save()

        # creating currency
        self.currency = Currency(name='EUR')
        self.currency.save()

    def test_required_fields(self):
        """
        sanity tests to check that required fields are really required
        required fields are name, brand, description, sub category, price, currency
        """
        # empty product
        product = Product()
        self.assertRaises(Exception, product.save)

        # adding name
        product.name = 'Xperia'
        self.assertRaises(Exception, product.save)

        # adding brand
        product.brand = self.brand
        self.assertRaises(Exception, product.save)

        # adding sub category
        product.sub_category = self.sub_category
        self.assertRaises(Exception, product.save)

        # adding description
        product.description = "This is a very cool phone with 12px zoom and large battery life"
        self.assertRaises(Exception, product.save)

        # adding price
        product.price = 400
        self.assertRaises(Exception, product.save)

        # adding currency
        product.currency = self.currency
        self.assertRaises(Exception, product.save)

    def tearDown(self):
        """
        cleanup test data
        """
        pass

class CategoryTestCase(TestCase):
    """
    test cases for category model
    """

    def setUp(self):
        """
        create a test category
        """
        pass

    def test_required_fields(self):
        """
        sanity tests to check that required fields are really required
        """
        # empty category
        category = Category()
        self.assertRaises(category.save)

        category.title='Tablets and Phones'
        self.assertRaises(category.save)

    def test_title_unique(self):
        """
        in models we have declared that category title is unique

        lets, test that category title are unqiue
        """

        # creating category 1
        category1 = Category(title="ABC Category")
        category1.save()

        # creating category 2 with same title
        category2 = Category(title="ABC Category")
        self.assertRaises(Exception, category2.save)

    def test_category_create(self):
        """
        test creating a category
        """
        category = Category(title='Domestic')
        category.save()
        self.assertEqual(category, Category.objects.get(title='Domestic'))

    def tearDown(self):
        """
        cleanup test data
        """
        pass

class SubCategoryTestCase(TestCase):
    """
    test cases for sub category model
    """

    category = None

    def setUp(self):
        """
        create a test category
        """
        # creating test category
        self.category = Category(title='Tablets and Phones')
        self.category.save()

    def test_required_fields(self):
        """
        sanity tests to check that required fields are really required
        """

        # empty sub category
        sub_category = SubCategory()
        self.assertRaises(Exception, sub_category.save)

        # adding title
        sub_category.title = 'Smartphones'
        self.assertRaises(Exception, sub_category.save)

        # adding category
        sub_category.category = self.category
        self.assertRaises(Exception, sub_category.save)

    def test_title_unique(self):
        """
        in models we have declared that sub-category title is unique

        lets, test that sub-category title are unqiue
        """

        # creating sub category 1
        sub_category1 = SubCategory(title="Some Sub Category", category=self.category)
        sub_category1.save()

        # creating sub category 2 with same title
        sub_category2 = SubCategory(title="Some Sub Category", category=self.category)
        self.assertRaises(sub_category2.save)

    def tearDown(self):
        """
        cleanup test data
        """
        pass

class CurrencyTestCase(TestCase):
    """
    test cases for product's currency model
    """

    def test_create_currency(self):
        """
        test creating a currency
        """
        currency = Currency(name='INR')
        currency.save()
        self.assertEqual(currency, Currency.objects.get(name='INR'))

    def test_create_unique_currency(self):
        """
        test creating a unique currency
        """
        currency1 = Currency(name='USD')
        currency1.save()

        currency2 = Currency(name='USD')
        self.assertRaises(Exception, currency2.save)

class UnitTestCase(TestCase):
    """
    test cases for product's unit model
    """

    def test_create_unit(self):
        """
        test creating a unit
        """
        unit = Unit(name='inches')
        unit.save()
        self.assertEqual(unit, Unit.objects.get(name='inches'))

    def test_create_unique_unit(self):
        """
        test creating a unique unit
        """
        unit1 = Unit(name='kg')
        unit1.save()

        unit2 = Unit(name='kg')
        self.assertRaises(Exception, unit2.save)

class BrandTestCase(TestCase):
    """
    test cases for brand model
    """

    def test_create_brand(self):
        """
        test creating a brand
        """
        brand = Brand(name='samsung', website='http://www.samsung.com/')
        brand.save()

        # test brand was saved
        self.assertEqual(brand, Brand.objects.get(name='samsung'))

    def test_create_unique_brand(self):
        """
        test creating a unique brand
        """
        brand1 = Brand(name='Sony', website='http://www.sony.com/prod123/')
        brand1.save()

        # brand name should be unique
        brand2 = Brand(name='Sony', website='http://www.sony.com/prod123/')
        self.assertRaises(Exception, brand2.save)


class ReviewTestCase(TestCase):
    """
    test cases for brand model
    """

    category     = None
    sub_category = None
    brand        = None
    currency     = None
    product      = None

    def setUp(self):
        """
        create a test category, sub-category and a brand for a test product
        """
        # creating test category
        self.category = Category(title='Tablets and Phones')
        self.category.save()

        # creating test sub category
        self.sub_category = SubCategory(title='Smartphones', category=self.category)
        self.sub_category.save()

        # creating test brand
        self.brand = Brand(name='Sony', website='http://www.sony.com/prod123/')
        self.brand.save()

        # creating currency
        self.currency = Currency(name='EUR')
        self.currency.save()

        # test creating a product, before adding a review for it
        self.product = Product(name='Sony VAIO', brand=self.brand, 
                sub_category=self.sub_category, description="some description",
                price=200.35, currency=self.currency, url="www.sonyvaio.com")
        self.product.save()

    def test_create_review(self):
        """
        test creating a review
        """

        review = Review(product=self.product, rating=4)
        self.assertRaises(review.save)

class OfferTestCase(TestCase):
    """
    test cases for offer model
    """
	
    category     = None
    sub_category = None
    brand        = None
    currency     = None
    product      = None

    def setUp(self):
	"""
	create a test category, sub-category and a brand for a test product
	"""
	# creating test category
	self.category = Category(title='Tablets and Phones')
	self.category.save()
		
	# creating test sub category
	self.sub_category = SubCategory(title='Smartphones', category=self.category)
	self.sub_category.save()
		
	# creating test brand
	self.brand = Brand(name='Sony', website='http://www.sony.com/prod123/')
	self.brand.save()
		
	# creating currency
	self.currency = Currency(name='EUR')
	self.currency.save()

	# test creating a product, before adding a offer for it
	self.product = Product(name='Sony VAIO', brand=self.brand, 
		sub_category=self.sub_category, description="some description",
			price=200.35, currency=self.currency, url="www.sonyvaio.com")
	self.product.save()

	def test_create_offer(self):
	    """
	    test creating a offer
	    """
		
	    offer = Offer(product=self.product, name='movieticket')
	    self.assertRaises(Exception, offer.save)
