from django.contrib import admin
from .models import MsureUnit ,FoodMix ,DoctorProfile


# Register your models here.
admin.site.register(FoodMix)
admin.site.register(MsureUnit)
admin.site.register(DoctorProfile)