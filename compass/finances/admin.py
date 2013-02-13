from django.contrib import admin
from .models import *

admin.site.register(Individual)
admin.site.register(Business)
admin.site.register(BusinessDonation)
admin.site.register(IndividualDonation)
admin.site.register(IndividualAsk)
admin.site.register(BusinessAsk)
admin.site.register(Campaign)
