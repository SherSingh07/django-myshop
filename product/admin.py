from django.contrib import admin

from product.models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Currency)
admin.site.register(Offer)
admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(Review)


