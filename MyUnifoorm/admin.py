from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Review, User, Order, Product

# Register your models here.
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)


# SUPER USER ACCOUNT 
# USERNAME : Ammar12 
# PASSWORD : 12345